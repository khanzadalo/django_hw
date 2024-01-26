from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse("Hello! Its my project")


def current_date(request):
    now = datetime.now()
    current_data = now.strftime("%Y-%m-%d")
    if request.method == 'GET':
        return HttpResponse(f"today is the {current_data}")


def goodby_view(request):
    if request.method == 'GET':
        return HttpResponse("Goodby user!")

