from django.shortcuts import render, render_to_response
from django.views.decorators import csrf
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect    #防止出现403问题
import json


@csrf_exempt
def judge(request):
    if request.POST:
        #调用地图构建函数
        return HttpResponse()
    else:
        return render(request, "judge/home.html")

@csrf_exempt
def send(request):
    room_num=request.POST['room_num']
    print(room_num)
    #根据房间号查找对应串口指令并发送给小车

    return HttpResponse()
