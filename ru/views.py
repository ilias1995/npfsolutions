# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import FeedProducts, Poultry, Distributor, DistributorShip


def index(request):
    return render(request, 'ru/index.html')


def feed_products(request):
    title = 'Виды корм'
    products = FeedProducts.objects.all()
    return render(request, 'ru/products.html', {'products': products, 'title': title})


def feed_products_info(request, id):
    feed_info = FeedProducts.objects.get(pk=id)
    return render(request, 'ru/products_info.html', {'feed_info': feed_info})


def poultry(request):
    title = 'Виды куриц'
    products = Poultry.objects.all()
    return render(request, 'ru/products.html', {'products': products, 'title': title})


def poultry_info(request):
    poultry_info = Poultry.objects.all()
    return render(request, 'ru/products_info.html', {'poultry_info': poultry_info})


def distributor_shipdistributor(request):
    distributor = Distributor.objects.all()
    return render(request, 'ru/', {'distributor': distributor})


def distributor_ship(request):
    distributor_ship = DistributorShip.objects.all()
    return render(request, 'ru/', {'distributor_ship': distributor_ship})