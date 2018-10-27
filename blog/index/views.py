from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
from django.contrib import messages
from django.db.models import Exists
# Create your views here.
def blog_main_views(request):
    return render(request,'blog_main.html')

def login_views(request):
    if request.method == 'GET':
        return render(request,"login.html")
    else:
        uemail = request.POST['email']
        upassword = request.POST['password']
        # user = User.query.filter(User.username == username, User.password == password).first()
        user = User.objects.get(email = uemail)
        if user and upassword == user.password:
            request.session['user_id'] = user.id
            request.session['user_email'] = user.email
            request.session['IS_LOGIN'] = True
            #判断是否存进cookie
            # if 'isSaved' in request.POST:
            #     resp.set_cookie('uid',user.id,60*60*60*7)
            return render(request,"blog_main.html")
        else:
            messages.add_message(request, messages.INFO, '用户名或密码不正确,请检查!')
            return render(request,'login.html')
    

def register_views(request):
    if request.method == "POST":
        #获取数据
        uemail = request.POST['email']
        # utruename = request.form.get('truename')
        upassword = request.POST['password']
        # uage = request.form.get('age')
        print(uemail)
        print(upassword)
        print(User.objects.filter(id=1))
        if User.objects.filter(email = uemail):
            messages.add_message(request, messages.ERROR, "账号已存在，请重新注册")
        else:
            #转存数据库
            newmes = User(email=uemail, password=upassword)
            newmes.save()
            #提示注册成功和返回登陆页面
            messages.add_message(request, messages.SUCCESS, "注册成功请登录")
            return redirect('/login')
    return render(request,"register.html")
    
