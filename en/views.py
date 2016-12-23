# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import FeedProducts, Poultry, Distributor, DistributorShip, DairyDevelopment, RoyalBread


def index(request):
    return render(request, 'en/index.html')


def feed_products(request):
    title = 'Feed products'
    products = FeedProducts.objects.all()
    return render(request, 'en/feed_pro.html', {'products': products, 'title': title})


def poultry(request):
    title = 'Poultry'
    poultry = Poultry.objects.all()
    return render(request, 'en/poultry.html', {'poultry': poultry, 'title': title})


def dairy_development(request):
    title = 'Dairy Development'
    dairy_development = DairyDevelopment.objects.all()
    return render(request, 'en/poultry.html', {'dairy_development': dairy_development, 'title': title})


def royal_bread(request):
    title = 'Royal Bread'
    royal_bread = RoyalBread.objects.all()
    return render(request, 'en/poultry.html', {'royal_bread': royal_bread, 'title': title})


def distributorship(request):
    title = 'Distributorship'
    distributorship = DistributorShip.objects.all()
    return render(request, 'en/distributorship.html', {'distributorship': distributorship, 'title': title})


def distributor(request):
    title = 'Distributors'
    distributor = Distributor.objects.all()
    return render(request, 'en/distributors.html', {'distributor': distributor, 'title': title})