import django
from django.shortcuts import render
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.forms.models import model_to_dict
from django.http import JsonResponse
import json
from .models import K_Day, Stock, Order, ShareHolding
from django.db.models import Q
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

import traceback
import sys
from decimal import Decimal


# Create your views here.
@require_http_methods(["GET"])
def show_stock(request):
    response = {}
    try:
        search_input = request.GET['search']
        stocks = []
        if not search_input:
            stocks = K_Day.objects.filter()
        else:
            stocks = K_Day.objects.filter(Q(code__icontains=search_input) | Q(code_name__icontains=search_input))
        result = []
        for s in stocks:
            json_dict = model_to_dict(s)
            result.append(json_dict)
        response['list'] = result
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def get_index(request):
    response = {}
    try:
        stocks = K_Day.objects.filter(code='sh.000001')
        result = model_to_dict(stocks[0])
        response['index'] = result
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def get_stock(request):
    response = {}
    try:
        stocks = Stock.objects.filter()
        result = []
        for s in stocks:
            json_dict = {"value": s.code_name + "_" + s.code}
            result.append(json_dict)
        response['list'] = result
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["POST"])
def login(request):
    response = {}
    try:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            response['msg'] = 'success'
            response['error_num'] = 0
        else:
            response['msg'] = 'login fail'
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["POST"])
def register(request):
    response = {}
    try:
        username = request.POST.get('username')
        password = request.POST.get('password')
        User.objects.create(username=username, password=password)
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def get_shareholdings(request):
    response = {}
    try:
        username = request.GET['username']
        dic = {'username': username, 'sell_or_buy': 0, 'status': ''}
        shareholdings = Order.objects.filter(**dic)

        result = []
        for s in shareholdings:
            json_dict = model_to_dict(s)
            result.append(json_dict)
        print(result)
        response['list'] = result
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def get_portfolio(request):
    response = {}
    try:
        username = request.GET['username']
        dic = {'username': username}
        shareholdings = ShareHolding.objects.filter(**dic)

        result = []
        for s in shareholdings:
            json_dict = model_to_dict(s)
            result.append(json_dict)
        print(result)
        response['list'] = result
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


def get_csrf_token(request):
    token = django.middleware.csrf.get_token(request)
    return JsonResponse({'token': token})


@require_http_methods(["POST"])
def buy(request):
    response = {}
    try:
        stock = request.POST.get('stock')
        code = stock.split('_')[1]
        code_name = stock.split('_')[0]
        username = request.POST.get('username')
        price = request.POST.get('price')
        volume = request.POST.get('volume')
        order = Order.objects.create(code=code, code_name=code_name, username=username, price=price, volume=volume,
                                     sell_or_buy=0)
        if order:
            response['msg'] = 'success'
            response['error_num'] = 0
        else:
            response['msg'] = 'buy fail'
    except  Exception as e:
        print(e.__str__())
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["POST"])
def sell(request):
    response = {}
    try:
        code = request.POST.get('code')
        code_name = request.POST.get('code_name')
        username = request.POST.get('username')
        price = request.POST.get('price')
        cost = request.POST.get('cost')
        volume = request.POST.get('volume')
        order_id = request.POST.get('order_id')
        print(price)
        order = Order.objects.create(code=code, code_name=code_name, username=username, price=price, volume=volume,
                                     sell_or_buy=1)
        Order.objects.filter(id=order_id).update(status="selled")

        price_in_decimal = Decimal(price)
        cost_in_decimal = Decimal(cost)
        profit = (price_in_decimal - cost_in_decimal) * Decimal(volume)
        ShareHolding.objects.create(code=code, code_name=code_name, username=username, volume=volume, cost=cost,
                                    sell_price=price, profit=profit)
        if order:
            response['msg'] = 'success'
            response['error_num'] = 0
        else:
            response['msg'] = 'sell fail'
    except  Exception as e:
        exc_type, exc_value, exc_traceback_obj = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_traceback_obj, limit=2, file=sys.stdout)
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
