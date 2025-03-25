from django.shortcuts import render, get_object_or_404

from .models import Product, Category


def index(request):
    products = Product.objects.all()
    category_name = request.GET.get("category")
    filter_name = request.GET.get("filter")

    categories = Category.objects.all()
    if category_name:
        products = products.filter(category_name)
    
    if filter_name == "price_increase":
        products = products.order_by("price")
    elif filter_name == "price_decrease":
        products = products.order_by("-price")
        

    context = {
                "products": products,
                "categories": categories
            }
    return render(request, "index.html", context=context)

def about(request):
    return render(request, "about.html")


def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "product_details.html", {"product": product})