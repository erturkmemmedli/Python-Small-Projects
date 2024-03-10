from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
import random
import string


def home(request):
    return render(request, 'generator/home.html')


def about(request):
    return render(request, 'generator/about.html')


def password(request):
    chars = list(string.ascii_lowercase)

    length = int(request.GET.get('length', 12))

    if request.GET.get('uppercase'):
        chars.extend(list(string.ascii_uppercase))

    if request.GET.get('special_chars'):
        chars.extend(list(string.punctuation))

    if request.GET.get('numbers'):
        chars.extend(list(string.digits))

    _password = ""

    for i in range(length):
        _password += random.choice(chars)

    return render(request, 'generator/password.html', {'password': _password})