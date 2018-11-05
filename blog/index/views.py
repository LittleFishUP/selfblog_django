from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator
from .models import *
from django.contrib import messages
import json
# Create your views here.
def blog_main_views(request):
    #加入博客信息数据库读取
    blog = Blog.objects.all()
   
    #推送最新更新取最后3个
    new = Blog.objects.all()[:3]

    return render(request,'blog_main.html',locals())

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
            return redirect('/blog_main/')
        else:
            messages.add_message(request, messages.INFO, '邮箱或密码不正确,请检查!')
            return render(request,'login.html')
    

def register_views(request):
    if request.method == "POST":
        #获取数据
        uusername = request.POST['username']
        uemail = request.POST['email']
        uage = request.POST['age']
        if request.POST['myurl']:
            umyurl = request.POST['myurl']
        else:
            umyurl=''
        upassword = request.POST['password']
        
        # print(uemail)
        # print(upassword)
        # print(User.objects.filter(id=1))

        # if User.objects.filter(email = uemail):
        #     messages.add_message(request, messages.ERROR, "账号已存在，请重新注册")

        # if User.objects.filter(email=uemail):
        #     messages.add_message(request, messages.ERROR, "用户名已存在，请重新注册")
               
        #转存数据库
        newmes = User(username=uusername,email=uemail,age=uage,myurl=umyurl,password=upassword)
        newmes.save()
        #提示注册成功和返回登陆页面
        messages.add_message(request, messages.SUCCESS, "注册成功请登录")
        return redirect('/login')
    return render(request,"register.html")
    
def check_input_views(request):
    # 接收前端传递过来的数据 - username 
    username = request.GET['username']
    users = User.objects.filter(username=username)
    if users:
        status = 1
        msg = '用户名已经存在'
    else:
        status = 0
        msg = ''
    dic = {
        'status': status,
        'msg': msg,
    }
    return HttpResponse(json.dumps(dic))
def check_input_views2(request):
    #邮箱检查
    email = request.GET['email']
    users1 = User.objects.filter(email=email)
    if users1:
        status = 1
        msg = '邮箱已经存在'
    else:
        status = 0
        msg = ''
        

    dic = {
        'status': status,
        'msg': msg,
    }
    return HttpResponse(json.dumps(dic))
def check_input_views3(request):
    #个人主站地址检查
    myurl = request.GET['myurl']
    users2 = User.objects.filter(myurl=myurl)
    if users2:
        status = 1
        msg = '主站地址已被使用'
    else:
        status = 0
        msg=''
       

    dic = {
        'status': status,
        'msg': msg,
    }
    return HttpResponse(json.dumps(dic))


    return render(request,"writings.html")

def about_me_views(request):
    return render(request,"about_me.html")

def blog_page_views(request):
    page_num = request.GET.get('page',1) #获取url的页面参数（GET请求）
    blog_all_list = Blog.objects.order_by('id').all()
    paginator = Paginator(blog_all_list,1)#每一个进行分页
    page_of_blogs=paginator.get_page(page_num) 

    
    return render(request,"blog_page_views.html",locals())
