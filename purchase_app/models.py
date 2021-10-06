from django.db import models
from datetime import datetime as dt
from django.conf import settings


class Order(models.Model):

    STATUS_CHOICES = [
        ('REGISTER', 'Register Order'),
        ('CANCEL_BY_CUSTOMER', 'Cancel by Customer'),
        ('CANCEL_BY_EMPOLYEE', 'Cancel by Employee'),
        ('UNDER_SHIPPING', 'Under Shipping'),
        ('COMPLETED', 'Completed'),
    ]

    DOMESTIC_DELIVERY_METHOD_CHOICES = [
        ('CUSTOMER_HOME', 'To delivery to customer home'),
        ('BRANCH', 'To delivery to company branch'),
    ]

    PAYMENT_METHOD_CHOICES = [
        ('BANK_ACCOUNT', 'To transfer bank account'),
        ('CASH', 'Pay by cash'),
    ]

    order_no = models.CharField(max_length=50, blank=True, unique=True)
    order_date = models.DateTimeField(
        auto_now=False, default=dt.now(), null=False)

    customer_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        null=True
    )
    customer_name = models.CharField(max_length=50)
    customer_phone = models.CharField(max_length=12)
    customer_address = models.CharField(max_length=100)
    customer_email = models.EmailField(max_length=254)

    status = models.CharField(
        max_length=100,
        choices=STATUS_CHOICES,
        default='REGISTER',
    )
    total_product_price = models.DecimalField(
        max_digits=12, decimal_places=2, default=0)
    estimated_total_weight = models.FloatField(default=0)
    estimated_ship_fee = models.DecimalField(
        max_digits=12, decimal_places=2, default=0)
    estimated_total_fee = models.DecimalField(
        max_digits=12, decimal_places=2, default=0)
    fix_total_weight = models.FloatField(default=0)
    fix_ship_fee = models.DecimalField(
        max_digits=12, decimal_places=2, default=0)
    fix_total_fee = models.DecimalField(
        max_digits=12, decimal_places=2, default=0)
    domestic_delivery_method = models.CharField(
        max_length=100,
        choices=DOMESTIC_DELIVERY_METHOD_CHOICES,
        default='CUSTOMER_HOME',
    )
    payment_method = models.CharField(
        max_length=100,
        choices=PAYMENT_METHOD_CHOICES,
        default='BANK_ACCOUNT',
    )
    memo = models.TextField(blank=True)
    delivery_date = models.DateField(
        auto_now=False, auto_now_add=True, blank=True)
    delivery_time = models.TimeField(
        auto_now=False, auto_now_add=True, blank=True)

    def products(self):
        products = Product.objects.filter(order=self)
        return products

    def __str__(self):
        if (self.order_no != ''):
            return str(self.order_no)
        return str(self.order_date)

    def save(self, flag=True, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)
        if flag:
            self.order_no = str(dt.now().strftime(
                '%m%d')) + '-' + str(dt.now().strftime("%M%S")) + '-0' + str(self.id)

            '''
                Order price depend on child-product price
            '''
            products = Product.objects.filter(order=self)
            self.total_product_price = 0
            self.estimated_total_weight = 0
            self.estimated_ship_fee = 0
            self.fix_total_weight = 0
            self.fix_ship_fee = 0
            self.fix_total_fee = 0
            for p in products:
                self.total_product_price += p.total_price
                self.estimated_total_weight += p.estimated_weight
                self.estimated_ship_fee += p.total_price
                self.fix_total_weight += p.estimated_weight
                self.fix_ship_fee += p.total_price
                self.fix_total_fee += p.total_price



            self.save(flag=False, *args, **kwargs)


class Product(models.Model):

    STATUS_CHOICES = [
        ('REGISTER', 'Register Order'),
        ('CANCEL_BY_CUSTOMER', 'Cancel by Customer'),
        ('CANCEL_BY_EMPOLYEE', 'Cancel by Employee'),
        ('UNDER_SHIPPING', 'Under Shipping'),
        ('COMPLETED', 'Completed'),
    ]

    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    product_url = models.URLField(max_length=200)

    order = models.ForeignKey("purchase_app.Order", on_delete=models.CASCADE)
    pack = models.ForeignKey(
        "purchase_app.Pack", on_delete=models.DO_NOTHING, null=True, blank=True)

    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_price = models.DecimalField(
        max_digits=12, decimal_places=2, default=0)
    estimated_weight = models.FloatField(default=0)
    measurement_weight = models.FloatField(default=0)
    status = models.CharField(
        max_length=100,
        choices=STATUS_CHOICES,
        default='REGISTER',
    )
    ship_company = models.CharField(max_length=50, default='')
    comfirm_notifed_fig = models.BooleanField(default=False)
    memo_from_customer = models.TextField(blank=True)

    def get_order_no(self):
        return Order.objects.get(id=self.order.id).order_no

    def get_order_date(self):
        return Order.objects.get(id=self.order.id).order_date

    def __str__(self):
        return self.product_name

    def save(self, flag=True, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)
        if flag:
            '''
            When save a product, should save order(parent of current product too),
            Because order price depend on child-product price.
            1. parent is self.order 
            2. parent.save()
            '''
            self.order.save()
            #self.save(flag=False, *args, **kwargs)


class Pack(models.Model):

    STATUS_CHOICES = [
        ('REGISTER', 'Register Order'),
        ('CANCEL_BY_CUSTOMER', 'Cancel by Customer'),
        ('CANCEL_BY_EMPOLYEE', 'Cancel by Employee'),
        ('UNDER_SHIPPING', 'Under Shipping'),
        ('COMPLETED', 'Completed'),
    ]

    pack_no = models.CharField(
        max_length=50, blank=True, unique=True)
    total_price = models.DecimalField(
        max_digits=12, decimal_places=2, default=0)
    total_weight = models.FloatField(default=0)
    oversea_ship_fee = models.DecimalField(
        max_digits=12, decimal_places=2, default=0)
    foreign_domestic_fee = models.DecimalField(
        max_digits=12, decimal_places=2, default=0)
    vn_domestic_fee = models.DecimalField(
        max_digits=12, decimal_places=2, default=0)
    status = models.CharField(
        max_length=100,
        choices=STATUS_CHOICES,
        default='REGISTER',
    )
    to_start_ship_date = models.DateField(
        auto_now=False, default=dt.now(), null=False)
    arrived_date = models.TimeField(
        auto_now=False, default=dt.now(), null=False)
    memo = models.TextField(default='')

    def save(self, flag=True, *args, **kwargs):
        super(Pack, self).save(*args, **kwargs)
        if flag:
            self.pack_no = self.pack_no = 'PACK' + str(self.id)
            self.save(flag=False, *args, **kwargs)

    def __str__(self):
        return self.pack_no
