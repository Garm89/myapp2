from django.shortcuts import render
from datetime import datetime, timedelta
from .models import Client, Product
from django.http import HttpResponse

def client_orders(request, client_id):
    client = Client.objects.get(pk=client_id)
    
    # Определяем дни и даты для фильтрации заказов
    today = datetime.today()
    week_ago = today - timedelta(days=7)
    month_ago = today - timedelta(days=30)
    year_ago = today - timedelta(days=365)
    
    # Получаем уникальные товары в заказах клиента за последнюю неделю, месяц и год
    products_week = Product.objects.filter(order__client=client, order__order_date__gte=week_ago).distinct()
    products_month = Product.objects.filter(order__client=client, order__order_date__gte=month_ago).distinct()
    products_year = Product.objects.filter(order__client=client, order__order_date__gte=year_ago).distinct()
    
    context = {
        'client': client,
        'products_week': products_week,
        'products_month': products_month,
        'products_year': products_year
    }
    
    return render(request, 'client_orders.html', context)

def home(request):
    html = """
    <h1>Добро пожаловать на мой первый Django-сайт!</h1>
    <p>Здесь вы найдете много интересного о моем проекте и обо мне :)</p>
    """
    
    # Логируем посещение страницы
    
    
    return HttpResponse(html)

def about(request):
    html = """
    <h1>Привет</h1>
    <h2>Меня зовут Сергей и я начинающий Python-разработчик</h2>
    """
    
    # Логируем посещение страницы
    
    
    return HttpResponse(html)