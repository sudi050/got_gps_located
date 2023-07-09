from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path("signup/", views.signup, name="signup"),
    path('', views.login, name="login"),
    path("pricing/", views.pricing, name="pricing"),
    path("cars/", views.cars, name="cars"),
    path("profile/", views.profile, name="profile"),
    path('profile/<str:driver>/', views.profile, name='profile'),
    path("booking/", views.booking, name="booking"),
    path("restaurant/", views.restaurant, name="restaurant"),

]
