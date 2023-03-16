from django.contrib import admin
from .models import Product, Customer, Cart, Payment, OrderPlaced, Wishlist, Comment, CommentReply, Image, Contact
from django.contrib.auth.models import Group


# Register your models here.


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discounted_price', 'category']
    search_fields = ['id', 'title', 'discounted_price', 'category']
    list_filter = ['discounted_price', 'category']
    inlines = [ImageInline]

    def get_ordering(self, request):
        if request.user.is_superuser:
            return ('id', 'title', 'discounted_price', 'category')
        return ('id', 'title', 'discounted_price', 'category')


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'locality', 'city', 'area', 'zipcode']


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']


class OrderPlacedInline(admin.TabularInline):
    model = OrderPlaced
    extra = 1


@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'amount', 'status', 'payment_option',
                    'paid']
    list_filter = ['status', 'payment_option',
                    'paid',]
    inlines = [OrderPlacedInline]


@admin.register(Wishlist)
class WishlistModeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product']


admin.site.unregister(Group)


class CommentReplyInline(admin.TabularInline):
    model = CommentReply
    extra = 1


@admin.register(Comment)
class CommentModeAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'description']
    inlines = [CommentReplyInline]


@admin.register(Contact)
class ContactModeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'message']
