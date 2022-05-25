from django.shortcuts import render

from django.http import HttpResponse
#def index (request):
#    return HttpResponse('<h1>Самая главная страница</h1>')
def index (request):
    return render(request, 'shop/index.html')
def contact (request):
    return HttpResponse('<p>Страница активных контактов</p>')
