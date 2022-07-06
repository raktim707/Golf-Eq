from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import FilterForm
from .models import MyDashApp
import plotly.graph_objects as go
from plotly.offline import plot

def home(request):
    return render(request, 'shop/home.html')
    
def product_list(request, category_slug=None):
    
    form = FilterForm(request.GET or None)
    products = Product.objects.all()
    all_apps = MyDashApp.objects.all()
    category = None
    categories = Category.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    if request.method == 'POST':
        form = FilterForm(request.POST)
        if form.is_valid():
            print(form.data)
            brand = form.data['brand']
            loft = form.data['loft']
            category = form.data['category']
            print("loft is ", loft)
            if 'leftHand' in form.data:
                lefthand = form.data['leftHand']
            else:
                lefthand = None
            
            if category:
                selected_category = get_object_or_404(Category, id=category)
                products = products.filter(category=category)
            if brand:
                products = products.filter(brand=brand)
            if lefthand:
                if lefthand == 'True':
                    print('lefthanded products: ', products)
                    products = products.filter(leftHand=True)
                    
                else:
                    products = products.filter(leftHand=False)
            
            if loft:
                if loft == 'A':
                    products = products.filter(loft__lte=8).filter(loft__gte=5)
                    print("filtere by loft: ", products)
                elif loft == 'B':
                    products = products.filter(loft__lte=10.5).filter(loft__gte=8)
                    print("filtere by loft B: ", products)
                elif loft == 'C':
                    products = products.filter(loft__lte=16).filter(loft__gte=11)
                elif loft == 'D':
                    products = products.filter(loft__lte=19.5).filter(loft__gte=16)
                elif loft == 'E':
                    products = products.filter(loft__lte=24).filter(loft__gte=20)
                elif loft == 'F':
                    products = products.filter(loft__lte=29).filter(loft__gte=24)
                elif loft == 'G':
                    products = products.filter(loft__gte=30)
    
    query = request.GET.get('search')
    results = []
    if query:
        products = Product.objects.filter(name__contains=query)
    
    paginator = Paginator(products, 10)
    page = request.GET.get('page')
    
    try:
        my_products = paginator.page(page)
    except PageNotAnInteger:
        my_products = paginator.page(1)
    except EmptyPage:
        my_products = paginator.page(paginator.num_pages)
    return render(request, 'shop/product/detail1.html', {'form': form, 'category': category, 'categories': categories, 'products': my_products, 'query': query, 'all_apps': all_apps})


def product_detail(request, id, slug):
    categories = Category.objects.all()
    product = get_object_or_404(Product, id=id, slug=slug)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product, 'cart_product_form': cart_product_form, 'categories': categories})


def dashApps(request, id):
    my_app = get_object_or_404(MyDashApp, id=id)
    return render(request, 'shop/new_dash.html', {'app_name': my_app.name})