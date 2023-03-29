from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import Product, Customer, Cart, Payment, OrderPlaced, Wishlist, Comment, CommentReply, Image, Rating
from .forms import CustomerRegistrationForm, CustomerProfileForm, CommentForm, ReplyForm, ContactForm
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def home(request):
    user = request.user
    totalitem = 0
    totalwishlist = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    product = Product.objects.all()  # truy vấn tất cả các sản phẩm từ database
    context = {'product': product, 'user': user, 'totalitem': totalitem, 'wishitem': wishitem}
    return render(request, 'app/home.html', context)


def about(request):
    user = request.user
    totalitem = 0
    totalwishlist = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, 'app/about.html', locals())


def contact(request):
    user = request.user
    totalitem = 0
    totalwishlist = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    form = ContactForm(request.POST)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form.send()
            return redirect(request.META.get('HTTP_REFERER', '/'))
        messages.success(request, "The contact was sent successfully")
    else:
        form = ContactForm()
    return render(request, 'app/contact.html', locals())


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    images = Image.objects.filter(product_images=pk)
    image_first = Image.objects.filter(product_images=pk).first()
    image_last = Image.objects.filter(product_images=pk).last()
    all_comments = Comment.objects.filter(product=product.id)
    wishlist = Wishlist.objects.filter(Q(product=product) & Q(user=request.user))
    parent_id = request.POST.get('parent_id')
    rating_stars = Rating.objects.filter(product=product)
    user = request.user
    totalitem = 0
    totalwishlist = 0
    rattingstar = Rating.objects.filter(product=product)
    star = rattingstar.values_list('value', flat=True)
    star_list = [s for s in star]
    len_start = len(star_list)
    average_rating = 0
    if len_start > 0:
        average_rating = sum(star_list) / len(star_list)
    else:
        pass
    test = int(average_rating)
    test1 = range(test)
    list_rating = Rating.objects.filter(product=product)
    test = list_rating.values_list('value')
    print(test)
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    if request.method == "POST":
        form1 = CommentForm(request.POST)
        form2 = ReplyForm(request.POST)
        if parent_id is None:
            if form1.is_valid():
                value = int(request.POST.get('rating',0))
                author = request.user
                product_id = product
                description = form1.cleaned_data["description"]
                req = Comment(author=author, product=product_id, description=description)
                req.save()
                rating = Rating(product=product, user=request.user, value=value, comment=req)
                rating.save()
                return redirect(request.META.get('HTTP_REFERER', '/'))
        else:
            if form2.is_valid():
                author = request.user
                parent_comment = Comment.objects.get(id=parent_id)
                description = form2.cleaned_data["description"]
                req = CommentReply(author=author, parent=parent_comment, description=description)
                req.save()
                return redirect(request.META.get('HTTP_REFERER', '/'))
    else:
        form1 = CommentForm()
        form2 = ReplyForm()

    context = {
        'product': product,
        'form1': form1,
        'form2': form2,
        'wishlist': wishlist,
        'all_comments': all_comments,
        'images': images,
        'image_first': image_first,
        'image_last': image_last,
        'totalitem': totalitem,
        'wishitem': wishitem,
        'totalwishlist': totalwishlist,
        'user': user,
        'rating_stars': rating_stars,
        'average_rating': average_rating,
        'len_start': len_start,
        'test': test1,
        'list_rating': test,
    }
    return render(request, "app/productdetail.html", context)


def delete_comment(request, pk):
    comment = Comment.objects.get(id=pk)
    if comment.author == request.user:
        comment.delete()
        return redirect(request.META.get('HTTP_REFERER', '/'))


def delete_reply(request, pk):
    reply = CommentReply.objects.get(id=pk)
    if reply.author == request.user:
        reply.delete()
        return redirect(request.META.get('HTTP_REFERER', '/'))


class CategoryView(View):
    def get(self, request, val):
        user = request.user
        totalitem = 0
        totalwishlist = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request, "app/category.html", locals())


class CategoryTitle(View):
    def get(self, request, val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request, "app/category.html", locals())


# class Product_sizeView(View):
#     def get(self, request, pk):
#         product = Product.objects.get(pk=pk)
#         product_sizes = Product_Size.objects.filter(parent_id=product)
#         title = product_sizes.objects.filter()


class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', locals())

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! User Register Successfully")
            return redirect('/accounts/login')
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request, 'app/customerregistration.html', locals())


class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        user = request.user
        totalitem = 0
        totalwishlist = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, 'app/profile.html', locals())

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        user = request.user
        if form.is_valid():
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            area = form.cleaned_data['area']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=user, name=name, locality=locality, mobile=mobile, city=city, area=area,
                           zipcode=zipcode)
            reg.save()
            messages.success(request, "Congratulation! Profile save successfully")
        else:
            messages.warning(request, "Invalid Input Data")

        return redirect('/address/')


def address(request):
    add = Customer.objects.filter(user=request.user)
    user = request.user
    totalitem = 0
    totalwishlist = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, 'app/address.html', locals())


class UpdateAddress(View):
    def get(self, request, pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        user = request.user
        totalitem = 0
        totalwishlist = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, 'app/UpdateAddress.html', locals())

    def post(self, request, pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.area = form.cleaned_data['area']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
        else:
            messages.warning(request, "Invalid Input Data")
        return redirect('/address/')


def remove_address(request, pk):
    add = Customer.objects.get(id=pk)
    add.delete()
    return redirect('/address/')


# @login_required()
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    if Cart.objects.filter(product=product_id).exists():
        c = Cart.objects.get(Q(product=product_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        amount = 0
        return redirect('/cart')
    else:
        product = Product.objects.get(id=product_id)
        Cart(user=user, product=product).save()
        return redirect('/cart')
    return quantity_change(request)


def buynow(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    if Cart.objects.filter(product=product_id).exists():
        return redirect('/checkout')
    else:
        product = Product.objects.get(id=product_id)
        Cart(user=user, product=product).save()
        return redirect('/checkout')


def quantity_change(request):
    product_id = request.GET.get('prod_id')
    if Cart.objects.filter(product=product_id).exists():
        c = Cart.objects.get(Q(product=product_id) & Q(user=request.user))
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            if p.product.discounted_price != 0:
                value = p.quantity * p.product.discounted_price
                amount = amount + value
            else:
                value = p.quantity * p.product.selling_price
                amount = amount + value
        totalamount = amount + 40
        # print(prod_id)
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount
        }
        return JsonResponse(data)


def plus_cart(request):
    product_id = request.GET.get('prod_id')
    if Cart.objects.filter(product=product_id).exists():
        c = Cart.objects.get(Q(product=product_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        return quantity_change(request)


def minus_cart(request):
    product_id = request.GET.get('prod_id')
    if Cart.objects.filter(product=product_id).exists():
        c = Cart.objects.get(Q(product=product_id) & Q(user=request.user))
        if c.quantity > 1:
            c.quantity -= 1
            c.save()
        else:
            c.quantity = 1
            c.save()
    return quantity_change(request)


def remove_cart(request):
    product_id = request.GET.get('prod_id')
    if Cart.objects.filter(product=product_id).exists():
        c = Cart.objects.get(Q(product=product_id) & Q(user=request.user))
        c.delete()
    return redirect('/cart/')


# @login_required()
def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    cart_empty = False
    user = request.user
    totalwishlist = 0
    if request.user.is_authenticated:
        wishitem = len(Wishlist.objects.filter(user=request.user))
    if cart.exists():
        for p in cart:
            if p.product.discounted_price != 0:
                value = p.quantity * p.product.discounted_price
                amount = amount + value
                cart_empty = False
            else:
                value = p.quantity * p.product.selling_price
                amount = amount + value
                cart_empty = False
    else:
        value = 0
        amount = amount + value
        cart_empty = True
    totalamount = amount + 40
    context = {
       'value': value,
        'user':user,
        'cart':cart,

    }
    return render(request, 'app/addtocart.html', context)


class checkout(View):
    def get(self, request):
        user = request.user
        totalwishlist = 0
        if request.user.is_authenticated:
            wishitem = len(Wishlist.objects.filter(user=request.user))
        add = Customer.objects.filter(user=user)
        cart_items = Cart.objects.filter(user=user)
        famount = 0
        for p in cart_items:
            if p.product.discounted_price != 0:
                value = p.quantity * p.product.discounted_price
                famount = famount + value
            else:
                value = p.quantity * p.product.selling_price
                famount = famount + value
        totalamount = famount + 40
        return render(request, 'app/checkout.html', locals())

    def post(self, request):
        user = request.user
        Cuss = Customer.objects.filter(user_id=user).first()
        payment = Payment()
        cart_items = Cart.objects.filter(user=user)
        famount = 0
        for p in cart_items:
            if p.product.discounted_price != 0:
                value = p.quantity * p.product.discounted_price
                famount = famount + value
            else:
                value = p.quantity * p.product.selling_price
                famount = famount + value
        totalamount = famount + 40
        payment.user = request.user
        payment.amount = totalamount
        payment.payment_option = request.POST.get('Payment')
        payment.payment_status = "pending"
        payment.paid = False
        payment.save()
        for c in cart_items:
            OrderPlaced(user=user, customer=Cuss, product=c.product, quantity=c.quantity, price=value,
                        payment=payment).save()
            c.delete()
        return redirect('/orders')


@login_required
def orders(request):
    user = request.user
    totalitem = 0
    totalwishlist = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
        order_placed = OrderPlaced.objects.filter(user=request.user)
        for op in order_placed:
            order_date = op.ordered_date
            current_time = timezone.now()
            time_difference = current_time - order_date
            import datetime
            new_time = order_date + datetime.timedelta(minutes=35)
            payment = Payment.objects.filter(Q(id=op.payment) and Q(status="Pending"))
            if time_difference > timedelta(minutes=1) and op.payment.status == "Pending":
                subject1 = f'No reply to email'
                msg1 = f'Hello {user} '
                msg1 += f'\nYou have 1 unpaid order\n'
                msg1 += f'Please pay within {new_time} after receiving this email\n'
                msg1 += f'Otherwise we will cancel your order\n'
                msg1 += f'Thank you for your seen.\n'
                msg1 += f'Your friend\n'
                msg1 += f'Neel'
                send_mail(
                    subject=subject1,
                    message=msg1,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[user.email]
                )
                payment.delete()
            else:
                pass
    return render(request, 'app/orders.html', locals())


def plus_wishlist(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        product = Product.objects.get(id=prod_id)
        user = request.user
        Wishlist(user=user, product=product).save()
        data = {
            'message': 'Wishlist added successfully'
        }
        return JsonResponse(data)


def minus_wishlist(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        product = Product.objects.get(id=prod_id)
        user = request.user
        wishlist = Wishlist.objects.filter(Q(product=product) & Q(user=request.user))
        wishlist.delete()
        data = {
            'message': 'Wishlist remove successfully'
        }
        return JsonResponse(data)


def search(request):
    query = request.GET['search']
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    product = Product.objects.filter(Q(title__icontains=query))
    return render(request, "app/search.html", locals())


# @login_required()
def show_wishlist(request):
    user = request.user
    totalitem = 0
    totalwishlist = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    product = Wishlist.objects.filter(user=user)
    return render(request, "app/wishlist.html", locals())
