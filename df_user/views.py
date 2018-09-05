#coding=utf-8
from django.shortcuts import render,redirect
from .models import *
from hashlib import sha1
from django.http import JsonResponse,HttpResponseRedirect
from . import user_decorator
from df_goods.models import *
from df_order.models import *
from django.core.paginator import Paginator,Page


def register(request): 
	context={'title':'天天生鲜注册'}
	return render(request,'df_user/register.html',context)

#接收用户输入
def register_handle(request):
	post = request.POST
	uname = post.get('user_name')
	upwd = post.get('pwd')
	upwd2=post.get('cpwd')
	uemail=post.get('email')
	#判断两次密码是否相等
	if upwd!=upwd2:
		return redirect('/user/register/')
	#密码加密
	s1=sha1()
	s1.update(upwd.encode('utf-8'))
	upwd3=s1.hexdigest()
	#创建对象
	user = UserInfo()
	user.uname=uname
	user.upwd=upwd3
	user.uemail=uemail
	user.save()
	#注册成功，转到登陆页面
	return redirect('/user/login/')

def register_exist(request):
	#对应的是ajax请求
	uname = request.GET.get('uname')
	count = UserInfo.objects.filter(uname=uname).count()
	return JsonResponse({'count':count})

def login(request):
	uname = request.COOKIES.get('uname','')
	context={'title':'天天生鲜登录','error_name':0,'error_pwd':0,'uname':uname}
	return render(request,'df_user/login.html',context)

def login_handle(request):
    #接收请求信息
    post=request.POST
    uname=post.get('username')
    upwd=post.get('pwd')
    jizhu=post.get('jizhu',0)
    #根据用户名查询对象
    users=UserInfo.objects.filter(uname=uname)#[]
    #判断：如果未查到则用户名错，如果查到则判断密码是否正确，正确则转到用户中心
    if len(users)==1:
        s1=sha1()
        s1.update(upwd.encode('utf-8'))
        if s1.hexdigest()==users[0].upwd:
            url=request.COOKIES.get('url','/')
            red = HttpResponseRedirect(url)
            #记住用户名
            if jizhu!=0:
                red.set_cookie('uname',uname)
            else:
                red.set_cookie('uname','',max_age=-1)
            request.session['user_id']=users[0].id
            request.session['user_name']=uname
            return red
        else:
            context = {'title': '用户登录','error_name': 0,'error_pwd': 1,'uname':uname,'upwd':upwd}
            return render(request,'df_user/login.html',context)
    else:
        context = {'title': '用户登录','error_name':1,'error_pwd': 0,'uname':uname,'upwd':upwd}
        return render(request,'df_user/login.html',context)

def logout(request):
	#将所以的session清除
	request.session.flush()
	return redirect('/')

@user_decorator.login
def info(request):
	user_email=UserInfo.objects.get(id=request.session['user_id']).uemail
	#最近浏览
	goods_ids=request.COOKIES.get('goods_ids','')
	goods_ids1=goods_ids.split(',')

	goods_list=[]
	if goods_ids1[0]!='':
		for goods_id in goods_ids1:
			goods_list.append(GoodsInfo.objects.get(id=int(goods_id)))

	context={'title':'天天生鲜用户中心',
			 'user_email':user_email,
			  'user_name':request.session['user_name'],
			   'goods_list':goods_list}
	return render(request,'df_user/user_center_info.html',context)

@user_decorator.login
def order(request,pindex):
	order_list=OrderInfo.objects.filter(user_id=request.session['user_id']).order_by('-oid')
	paginator=Paginator(order_list,2)
	if pindex=='':
		pindex='1'
	page=paginator.page(int(pindex))

	context={'title':'天天生鲜用户中心',
			 'paginator':paginator,
			 'page':page,}
	return render(request,'df_user/user_center_order.html',context)

@user_decorator.login
def site(request):
	user = UserInfo.objects.get(id=request.session['user_id'])
	if request.method=='POST':
		post=request.POST
		user.ushouuser=post.get('ushou')
		user.uaddress=post.get('uaddress')
		user.uyoubian=post.get('uyoubian')
		user.uphone=post.get('uphone')
		user.save()
	context={'title':'天天生鲜用户中心','user':user,}
	return render(request,'df_user/user_center_site.html',context)
