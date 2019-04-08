from django.shortcuts import render
from django.http import JsonResponse

def userinfo(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

    return JsonResponse({
        'status':'200'
    })