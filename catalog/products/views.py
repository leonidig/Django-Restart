from datetime import datetime

from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseBadRequest
from django.utils.timezone import make_aware
from django.conf import settings

from .models import Product, Category, Cart, CartItem


def index(request):
    products = Product.objects.all()

    category_name = request.GET.get("category")
    filter_name = request.GET.get("filter")
    product_name = request.GET.get("search")
    min_price = request.GET.get("min_price")
    max_price = request.GET.get("max_price")
    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")

    categories = Category.objects.all()

    if product_name:
        products = products.filter(name__icontains=product_name)

    if min_price:
        products = products.filter(price__gte=min_price)

    if max_price:
        products = products.filter(price__lte=max_price)

    if category_name:
        category = Category.objects.get(name=category_name)
        products = products.filter(category=category)

    if start_date:
        start_date = make_aware(datetime.strptime(start_date, "%Y-%m-%dT%H:%M")).date()

    if end_date:
        end_date = make_aware(datetime.strptime(end_date, "%Y-%m-%dT%H:%M")).date()

    if start_date and end_date:
        products = products.filter(created_at__date__range=(start_date, end_date))
    elif start_date:
        products = products.filter(created_at__date=start_date)
    elif end_date:
        products = products.filter(created_at__date=end_date)

    match filter_name:
        case "price_increase":
            products = products.order_by("price")
        case "price_decrease":
            products = products.order_by("-price")
        case "rating_increase":
            products = products.order_by("rating")
        case "rating_decrease":
            products = products.order_by("-rating")

    products_count = products.count()

    context = {
        "products": products,
        "categories": categories,
        "products_count": products_count,
    }
    return render(request, "index.html", context=context)


def about(request):
    return render(request, "about.html")


def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "product_details.html", {"product": product})



def cart_add(request, product_id: int):
    product = get_object_or_404(Product, id=product_id)
    if not request.user.is_authenticated:
        cart = request.session.get(settings.CART_SESSION_ID, dict())
        if cart.get(product_id):
            cart[product_id] += 1
        else:
            cart[product_id] = 1
        request.session[settings.CART_SESSION_ID] = cart
    else:
        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if created:
            cart_item.amount = 1
        else:
            cart_item.amount += 1
        cart_item.save()
    return redirect("products:cart_detail")


def cart_remove(request, product_id: int):
    product = get_object_or_404(Product, id=product_id)
    if not request.user.is_authenticated:
        cart = request.session.get(settings.CART_SESSION_ID, dict())
        if str(product_id) in cart:
            if cart[str(product_id)] > 1:
                cart[str(product_id)] -= 1
            else:
                cart.pop(str(product_id))
            request.session[settings.CART_SESSION_ID] = cart
    else:
        try:
            cart = request.user.cart
            cart_item = CartItem.objects.get(cart=cart, product=product)
            if cart_item.amount > 1:
                cart_item.amount -= 1
                cart_item.save()
            else:
                cart_item.delete()
        except CartItem.DoesNotExist:
            ...
    
    return redirect("products:cart_detail")

def cart_detail_view(request):
    if not request.user.is_authenticated:
        cart = request.session.get(settings.CART_SESSION_ID, dict())
        product_ids = cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart_items = []
        total_price = 0
        for product in products:
            count = cart[str(product.id)]
            price = count * product.price
            total_price += price
            cart_items.append({"product": product, "amount": count, "price": price})
        return render(
            request,
            "cart_detail.html",
            context={"cart_items": cart_items, "total_price": total_price},
        )
    else:
        try:
            cart = request.user.cart
        except Cart.DoesNotExist:
            cart = None
        if not cart or not cart.items.count():
            cart_items = []
            total_price = 0
        else:
            cart_items = cart.items.select_related("product").all()
            total_price = sum(item.product.price * item.amount for item in cart_items)
        return render(
            request,
            "cart_detail.html",
            context={"cart_items": cart_items, "total_price": total_price},
        )


def remove_item_from_cart(request, item_id: int): # soon
    product = get_object_or_404(Product, id=item_id)

    if not request.user.is_authenticated:
        cart = request.session.get(settings.CART_SESSION_ID, dict())
        if str(item_id) in cart:
            del cart[str(item_id)]
            request.session[settings.CART_SESSION_ID] = cart
        return redirect("products:cart_detail")
    else:
        try:
            cart = request.user.cart
            item_for_delete = CartItem.objects.get(cart=cart, product=product)
            item_for_delete.delete()
        except CartItem.DoesNotExist:
            cart = None
        return redirect("products:cart_detail")