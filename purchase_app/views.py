from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
# from django.utils.http import urlencode

from .forms import UpdateOrderForm, UpdatePackForm, UpdateProductForm
from .models import Order, Pack, Product


def order(request):
    orders = Order.objects.all().order_by('id')

    return render(request, 'OrderManager.html', {'orders': orders})


def order_edit(request):

    list_of_product_form = []

    if request.GET.get('q') == 'None':
        '''
        This case active when staff has just created a new order
        '''
        return HttpResponseRedirect('../../')

    elif request.GET.get('q') == 'create_new':
        form = UpdateOrderForm()
        order_model = None
        _id = None

    else:
        _id = request.GET.get('q')
        order_model = get_object_or_404(Order, id=_id)
        form = UpdateOrderForm(instance=order_model)
        products = Product.objects.filter(order=order_model)
        for p in products:
            product_form = UpdateProductForm(instance=p)
            list_of_product_form.append(product_form)

    if request.method == 'POST':
        form = UpdateOrderForm(request.POST or None, instance=order_model)
        if form.is_valid():
            form.save()
            newurl = '?q=' + str(_id)

            return redirect("."+newurl)

    return render(request, 'OrderEdit.html', {'form': form, 'current_id': _id, 'products': list_of_product_form})


def update_product(request, product_id):
    product = Product.objects.get(id=product_id)
    oder_id = product.order.id
    product_form = UpdateProductForm(request.POST or None, instance=product)
    if product_form.is_valid():
        product_form.save()
        newurl = '?q=' + str(oder_id)

        return HttpResponseRedirect("../"+newurl)

    newurl = '?q=' + str(oder_id)

    return HttpResponseRedirect("../"+newurl)


def add_product(request, _id):
    order = Order.objects.get(id=_id)
    product = Product.objects.create(
        product_name='',
        order=order,
        product_url='',
    )

    newurl = '?q=' + str(_id)

    return redirect("../"+newurl)


def delete_product(request, _id, product_id):
    Product.objects.get(id=product_id).delete()
    newurl = '?q=' + str(_id)
    
    return redirect("../../"+newurl)


def product(request):
    products = Product.objects.all().order_by('id')

    return render(request, 'ProductManager.html', {'products': products})


def pack(request):
    packs = Pack.objects.all().order_by('id')

    return render(request, 'PackManager.html', {'packs': packs})


def pack_edit(request):

    if request.GET.get('q') == 'None':
        '''
        This case active when staff has just created a new pack
        '''
        return HttpResponseRedirect('../../pack/')
        
    elif request.GET.get('q') == 'create_new':
        form = UpdatePackForm()
        pack_model = None
        _id = None

    else:
        _id = request.GET.get('q')
        pack_model = get_object_or_404(Pack, id=_id)
        form = UpdatePackForm(instance=pack_model)

    if request.method == 'POST':
        form = UpdatePackForm(request.POST or None, instance=pack_model)
        if form.is_valid():
            form.save()
            newurl = '?q=' + str(_id)
            
            return redirect("."+newurl)

    return render(request, 'PackEdit.html', {'form': form, 'current_id': _id, })
