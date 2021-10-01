from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from .forms import OrderForm, UpdateOrderForm, UpdateProductForm
from .models import Order, Pack, Product

def order(request):
    orders = Order.objects.all().order_by('id')

    return render(request, 'OrderManager.html', {'orders': orders})

def order_edit(request):
    
    if request.GET.get('q') == 'create_new':
        order_model = None
        form = UpdateOrderForm()
    else:
        _id = request.GET.get('q')
        order_model = get_object_or_404(Order, id=_id)
        form = UpdateOrderForm(instance=order_model)
    if request.method == 'POST':
        form = UpdateOrderForm(request.POST or None, instance=order_model)
        if form.is_valid():
            form.save()

    form_by_loop = []
    products = None
    if request.GET.get('q') != 'create_new':
        products = Product.objects.filter(order = _id)
        for p in products:
            product_form = UpdateProductForm(instance=p)
            if request.method == 'POST':
                product_form = UpdateProductForm(request.POST or None, instance=p)
                if product_form.is_valid():
                    product_form.save()
            form_by_loop.append(product_form)


    return render(request, 'OrderEdit.html', {'form': form, 'products': products, 'multiple_forms': form_by_loop})




def product(request):
    products = Product.objects.all().order_by('id')

    return render(request, 'ProductManager.html', {'products': products})



def pack(request):
    packs = Pack.objects.all().order_by('id')

    return render(request, 'PackManager.html', {'packs': packs})