# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import FeedProducts, Poultry, Distributor, DistributorShip, DairyDevelopment, RoyalBread


def index(request):
    return render(request, 'ru/index.html')


def feed_products(request):
    title = 'Виды корм'
    products = FeedProducts.objects.all()
    return render(request, 'ru/feed_pro.html', {'products': products, 'title': title})


def poultry(request):
    title = 'Виды куриц'
    poultry = Poultry.objects.all()
    return render(request, 'ru/poultry.html', {'poultry': poultry, 'title': title})


def dairy_development(request):
    title = 'Развитие молочная'
    dairy_development = DairyDevelopment.objects.all()
    return render(request, 'ru/poultry.html', {'dairy_development': dairy_development, 'title': title})


def royal_bread(request):
    title = 'Royal Порода'
    royal_bread = RoyalBread.objects.all()
    return render(request, 'ru/poultry.html', {'royal_bread': royal_bread, 'title': title})


def distributor(request):
    title = 'Продавцы'
    distributor = Distributor.objects.all()
    return render(request, 'ru/distributors.html', {'distributor': distributor, 'title': title})


def distributor_ship(request):
    distributor_ship = DistributorShip.objects.all()
    return render(request, 'ru/distributorship.html', {'distributor_ship': distributor_ship})