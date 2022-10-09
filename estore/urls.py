"""estore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views import ProductsView, ProductModelViewsetView
from api.views import AddView
from api.views import NumberChkView,ProductDetailsView,ReviewsView,ReviewDetailsView,ProductModelViewsetView,UsersView
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
# router.register("api/v1/products",ProductsViewSetView,basename="products")
router.register("api/v2/products",ProductModelViewsetView,basename="books")
router.register("register",UsersView,basename="users")

#

urlpatterns = [
    path('admin/', admin.site.urls),
    path("products",ProductsView.as_view()),
    path("add",AddView.as_view()),
    path("chk",NumberChkView.as_view()),
    path("products/<int:id>",ProductDetailsView.as_view()),
    path("reviews",ReviewsView.as_view()),
    path("reviews/<int:id>",ReviewDetailsView.as_view())




]
