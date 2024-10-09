from django.shortcuts import render, redirect
from django.conf import settings

def vacas(request):
    return render(request, "cows/vacas.html")


def toros(request):
    return render(request, "cows/toros.html")

