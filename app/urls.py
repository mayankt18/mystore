from app.forms import LoginForm
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('product-detail/<int:id>', views.product_detail, name="product-detail"),
    path('mobiles/', views.mobiles, name="mobiles"),
    path('products', views.products, name="products"),
    path('products/<slug:tag>', views.products, name="filter-products"),
    path('accounts/login/', auth_views.LoginView.as_view(template_name="app/user/login.html",
    authentication_form=LoginForm),
    name="login"),
    path('register/', views.register, name="register")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
