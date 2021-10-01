from django import forms
from .models import Order, Product

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = '__all__'

class UpdateOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            # 'order_date',
            # 'customer_id',
            'customer_name',
            'customer_phone',
            'customer_address',
            'customer_email',
            'status',
            'total_product_price',
            'estimated_total_weight',
            'estimated_ship_fee',
            'estimated_total_fee',
            'fix_total_weight',
            'fix_ship_fee',
            'fix_total_fee',
            'domestic_delivery_method',
            'payment_method',
            'memo',
            # 'delivery_date',
            # 'delivery_time',
        ] 

        widgets = {
            'memo': forms.Textarea(attrs={'placeholder': 'Order memo'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(UpdateOrderForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['total_product_price'].required = False
            self.fields['total_product_price'].widget.attrs['disabled'] = 'disabled'
            self.fields['estimated_total_weight'].required = False
            self.fields['estimated_total_weight'].widget.attrs['disabled'] = 'disabled'
            self.fields['fix_total_weight'].required = False
            self.fields['fix_total_weight'].widget.attrs['disabled'] = 'disabled'
            self.fields['estimated_ship_fee'].required = False
            self.fields['estimated_ship_fee'].widget.attrs['disabled'] = 'disabled'
            self.fields['fix_total_fee'].required = False
            self.fields['fix_total_fee'].widget.attrs['disabled'] = 'disabled'
        
    def save(self, commit=True):
        order_model = self.instance
        order_model.customer_name = self.cleaned_data['customer_name']
        order_model.customer_phone = self.cleaned_data['customer_phone']  
        order_model.customer_address = self.cleaned_data['customer_address']
        order_model.customer_email = self.cleaned_data['customer_email']  
        order_model.status = self.cleaned_data['status']
        order_model.total_product_price = self.cleaned_data['total_product_price']  
        order_model.estimated_total_weight = self.cleaned_data['estimated_total_weight']
        order_model.estimated_ship_fee = self.cleaned_data['estimated_ship_fee']  
        order_model.fix_total_weight = self.cleaned_data['fix_total_weight']  
        order_model.fix_ship_fee = self.cleaned_data['fix_ship_fee']
        order_model.fix_total_fee = self.cleaned_data['fix_total_fee']  
        order_model.domestic_delivery_method = self.cleaned_data['domestic_delivery_method']  
        order_model.payment_method = self.cleaned_data['payment_method']
        order_model.memo = self.cleaned_data['memo']  

        if commit:
            order_model.save()
        return order_model




class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'product_name',
            'quantity',
            'product_url',
            'price',
            'total_price',
            'estimated_weight',
            'measurement_weight',
            'status',
            'ship_company',
            'comfirm_notifed_fig',
            'memo_from_customer',
            'pack'
        ] 

        widgets = {
            'memo_from_customer': forms.Textarea(attrs={'placeholder': 'Memo from customer'}),
        }
        
    def save(self, commit=True):
        product_model = self.instance
        product_model.product_name = self.cleaned_data['product_name']
        product_model.quantity = self.cleaned_data['quantity']  
        product_model.product_url = self.cleaned_data['product_url']
        product_model.price = self.cleaned_data['price']  
        product_model.total_price = self.cleaned_data['total_price']
        product_model.estimated_weight = self.cleaned_data['estimated_weight']  
        product_model.measurement_weight = self.cleaned_data['measurement_weight']
        product_model.status = self.cleaned_data['status']  
        product_model.ship_company = self.cleaned_data['ship_company']  
        product_model.comfirm_notifed_fig = self.cleaned_data['comfirm_notifed_fig']
        product_model.memo_from_customer = self.cleaned_data['memo_from_customer']  

        if commit:
            product_model.save()
        return product_model