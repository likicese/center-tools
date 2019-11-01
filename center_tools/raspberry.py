from django.http import HttpResponse
from django.shortcuts import render_to_response
import os

def raspberry(request):
    return render_to_response("raspberry.html")

def operation(request):
    request.encoding="utf-8"
    message = "啥也没有"
    if request.GET["op"] == "重启":
        # message = os.system("sudo reboot")
        message = os.system("date")
        message = "我要重启啦\n" + message
    if request.GET["op"] == "关机":
        # message = os.system("sudo shutdown now")
        message = os.system("echo nonono")
        message = "我要关机啦\n" + message
    return HttpResponse(message)