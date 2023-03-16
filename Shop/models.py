from django.db import models
from django.contrib.auth.models import User
from django.forms import inlineformset_factory

# Create your models here.
CATEGORY_CHOICES = (
    ('CR', 'Curd'),
    ('ML', 'Milk'),
    ('LS', 'Lassi'),
    ('MS', 'MilkShake'),
    ('PN', 'Paneer'),
    ('GH', 'Ghee'),
    ('CZ', 'Cheese'),
    ('IC', 'Ice-Creams'),
)
AREA_CHOICES = (
    ('B', 'Bắc'),
    ('T', 'Trung'),
    ('N', 'Nam'),
    ('ĐBSCL', 'Đồng Bằng Sông Cửu Long'),
)

STATUS_CHOICES = {
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel'),
    ('Pending', 'Pending'),
}

PAYMENT_CHOICES = {
    ('Wallet', 'Wallet'),
    ('Card', 'Card'),
    ('MoMo', 'MoMo'),
}


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product/banner')

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to='product')
    product_images = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')


ImageFormSet = inlineformset_factory(Product, Image, fields=('image',), extra=1)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    area = models.CharField(choices=AREA_CHOICES, max_length=100)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    payment_option = models.CharField(max_length=100, choices=PAYMENT_CHOICES, default="")
    paid = models.BooleanField(default=False)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')


class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    ordered_date = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, default="")

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price


OrderPlacedFormSet = inlineformset_factory(Payment, OrderPlaced, fields=('payment',), extra=1)


class PaymentOption(models.Model):
    name = models.CharField(choices=PAYMENT_CHOICES, max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Comment(models.Model):
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product)


class CommentReply(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    reply_date = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies', null=True, blank=True)

    def __str__(self):
        return str(self.parent)


CommentReplyFormSet = inlineformset_factory(Comment, CommentReply, fields=('parent',), extra=1)


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
