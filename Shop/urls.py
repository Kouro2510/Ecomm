from django.urls import path, include
from . import views, admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm, MyPasswordResetForm, MyPasswordChangeForm, MySetPasswordForm, CustomerRegistrationForm
from django.contrib import admin
from .views import search

urlpatterns = [
                  path("", views.home, name="home"),
                  path("about", views.about, name="about"),
                  path("contact", views.contact, name="contact"),
                  path("category/<slug:val>", views.CategoryView.as_view(), name="category"),
                  path("product-detail/<int:pk>", views.product_detail, name="product-detail"),
                  path("category-title/<val>", views.CategoryTitle.as_view(), name="category-title"),
                  path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
                  path('remove-comment/<int:pk>', views.delete_comment, name='delete-comment'),
                  path('remove-reply/<int:pk>', views.delete_reply, name='delete-reply'),
                  path('buynow/', views.buynow, name='buynow'),
                  path('cart/', views.show_cart, name='showcart'),
                  path('checkout/', views.checkout.as_view(), name='checkout'),
                  path('orders/', views.orders, name='orders'),
                  path('pluscart/', views.plus_cart),
                  path('minuscart/', views.minus_cart),
                  path('removecart/', views.remove_cart),
                  path('search/', views.search, name='search'),
                  path('pluswishlist/', views.plus_wishlist),
                  path('minuswishlist/', views.minus_wishlist),
                  path('wishlist', views.show_wishlist, name='showwishlist'),
                  # login authentication
                  path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
                  path('accounts/login',
                       auth_view.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm),
                       name='login'),
                  path('password-reset/', auth_view.PasswordResetView.as_view(template_name='app/password_reset.html',
                                                                              form_class=MyPasswordResetForm),
                       name='password_reset'),
                  path('changepassword/', auth_view.PasswordChangeView.as_view(template_name='app/changepassword.html',
                                                                               form_class=MyPasswordChangeForm,
                                                                               success_url='/passwordchangedone'),
                       name='passwordchange'),
                  path('passwordchangedone/',
                       auth_view.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'),
                       name='passwordchangedone'),
                  path('profile/', views.ProfileView.as_view(), name='profile'),
                  path('address/', views.address, name='address'),
                  path('UpdateAddress/<int:pk>', views.UpdateAddress.as_view(), name='UpdateAddress'),
                  path('removeaddress/<int:pk>', views.remove_address, name='RemoveAddress'),
                  path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'),
                  path('password-reset/', auth_view.PasswordResetView.as_view(template_name='app/password_reset.html',
                                                                              form_class=MyPasswordResetForm),
                       name='password_reset'),
                  path('password-reset/done',
                       auth_view.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'),
                       name='password_reset_done'),
                  path('password-reset-complete/',
                       auth_view.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'),
                       name='password_reset_complete'),
                  path('password-reset-confirm/<uidb64>/<token>',
                       auth_view.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',
                                                                  form_class=MySetPasswordForm),
                       name='password_reset_confirm'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Shop Sell Page"
admin.site.site_title = "Shop Sell Page"
admin.site.site_index_title = "Welcome"
