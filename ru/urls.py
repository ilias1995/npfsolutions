"""npfsolutions URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from ru.views import index, feed_products, poultry, distributor, distributor_ship, dairy_development, royal_bread

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^feed_products/', feed_products, name='feed_products_ru'),
    url(r'^poultry/', poultry, name='poultry_ru'),
    url(r'^distributors/', distributor, name='distributor_ru'),
    url(r'^distributorship/', distributor_ship, name='distributorship_ru'),
    url(r'^royal_bread/', royal_bread, name='royal_bread_ru'),
    url(r'^dairy_development/', dairy_development, name='dairy_development_ru'),
]
