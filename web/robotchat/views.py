# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import random
import json

from django.views.decorators.csrf import csrf_exempt
from robotchat.models import user_info
from django.core.mail import send_mail

@csrf_exempt
def email_check(request):
  resData = {'isOk': False, 'errmsg': '未知错误'}
  # print(request.POST)
  if request.method == 'POST':
    email = request.POST.get("email")
    if user_info.objects.filter(email=email):
      resData['errmsg'] = '该邮箱已注册'
    else:
      number = str(random.randrange(1000, 9999))
      send_mail('树洞聊天机器人', '您的验证码为'+number+'，若非本人请忽略。', 'shuaipoem@163.com',
                [email], fail_silently=False)
      resData['number'] = number
      resData['isOk'] = True
    jsonData = json.dumps(resData)
    return HttpResponse(jsonData, content_type="application/json")

@csrf_exempt
def SignUp(request):
    resData = {'isOk': False, 'errmsg': '未知错误'}
    if request.method =='POST':
        username = request.POST.get("name")
        password = request.POST.get("psw")
        email = request.POST.get("email")
        print(username)
        if user_info.objects.filter(username=username):
            resData['errmsg'] = '用户名已存在!'
        else:
            resData['isOk'] = True
            user_info.objects.create(username=username, password=password, email=email)
        jsonData = json.dumps(resData)
        return HttpResponse(jsonData, content_type="application/json")

@csrf_exempt
def SignIn(request):
    resData = {'isOk': False, 'errmsg': '未知错误'}
    if request.method =='POST':
        username = request.POST.get("name")
        password = request.POST.get("psw")
        print(username)
        print(password)
        # 对username去查在数据库中是否存在于username字段或者email字段
        res1 = user_info.objects.filter(email=username, password=password)
        res2 = user_info.objects.filter(username=username, password=password)
        if res1 or res2:
            resData['isOk'] = True
        else:
            resData['errmsg'] = '用户名或密码错误'
        jsonData = json.dumps(resData)
        return HttpResponse(jsonData, content_type="application/json")