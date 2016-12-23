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
from en.views import index, feed_products, poultry, distributor, distributorship, royal_bread, dairy_development

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^feed_products/', feed_products, name='feed_products_en'),
    url(r'^poultry/', poultry, name='poultry_en'),
    url(r'^distributor/', distributor, name='distributor_en'),
    url(r'^distributorship/', distributorship, name='distributorship_en'),
    url(r'^royal_bread/', royal_bread, name='royal_bread_en'),
    url(r'^dairy_development/', dairy_development, name='dairy_development_en'),
]
