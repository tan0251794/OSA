from django import forms
from .models import Order, Pack, Product

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = '__all__'

class UpdateOrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = [
            'id',
            'order_no',
            'order_date',
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
            self.fields['order_no'].required = False
            self.fields['order_no'].widget.attrs['disabled'] = 'disabled'
            self.fields['order_date'].required = False
            self.fields['order_date'].widget.attrs['disabled'] = 'disabled'
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
            'id',
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
            'pack',
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



class UpdatePackForm(forms.ModelForm):
    class Meta:
        model = Pack
        fields = [
            'pack_no',
            'total_price',
            'total_weight',
            'oversea_ship_fee',
            'foreign_domestic_fee',
            'vn_domestic_fee',
            'status',
            'to_start_ship_date',
            'arrived_date',
            'memo'
        ] 

        widgets = {
            'memo': forms.Textarea(attrs={'placeholder': 'Memo of pack'}),
        }

    
    def __init__(self, *args, **kwargs):
        super(UpdatePackForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['pack_no'].required = False
            self.fields['pack_no'].widget.attrs['disabled'] = 'disabled'
        
    def save(self, commit=True):
        pack_model = self.instance
        pack_model.total_price = self.cleaned_data['total_price']
        pack_model.total_weight = self.cleaned_data['total_weight']  
        pack_model.oversea_ship_fee = self.cleaned_data['oversea_ship_fee']
        pack_model.foreign_domestic_fee = self.cleaned_data['foreign_domestic_fee']  
        pack_model.vn_domestic_fee = self.cleaned_data['vn_domestic_fee']
        pack_model.to_start_ship_date = self.cleaned_data['to_start_ship_date']  
        pack_model.arrived_date = self.cleaned_data['arrived_date']
        pack_model.status = self.cleaned_data['status']  
        pack_model.memo = self.cleaned_data['memo']  

        if commit:
            pack_model.save()

        return pack_model