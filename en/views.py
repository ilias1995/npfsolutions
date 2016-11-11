# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import FeedProducts, Poultry, Distributor, DistributorShip


def index(request):
    return render(request, 'en/index.html')


def feed_products(request):
    title = 'Виды корм'
    products = FeedProducts.objects.all()
    return render(request, 'en/feed_pro.html', {'products': products, 'title': title})


def poultry(request):
    title = 'Виды куриц'
    products = Poultry.objects.all()
    return render(request, 'en/poultry.html', {'products': products, 'title': title})


def distributorship(request):
    distributorship = Distributor.objects.all()
    return render(request, 'en/distributorship.html', {'distributorship': distributorship})


def distributor(request):
    distributors = DistributorShip.objects.all()
    return render(request, 'en/distributors.html', {'distributors': distributors})