from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Customer, Saler, Genre, Good
from django.views import generic
from django.core.paginator import Paginator

# Create your views here.

class GoodListView(generic.ListView):
    model = Good

class GoodDetailView(generic.DetailView):
    model = Good
    
class SalerDetailView(generic.DetailView):
    model = Saler

def index(request):
    tag = 0
    itemList1=Good.objects.all()#[:2]
    paginator = Paginator(itemList1, 4)
    
    pindex = 1
    
        
    page = paginator.page(pindex)  # 传递当前页的实例对象到前端
    
    
    
    
    itemList2=Good.objects.filter(genre="2")
    current_customer = Customer.objects.first()
    current_saler = Saler.objects.first()
    current_user = request.user
    
    
    
    if request.user.is_authenticated:
        if current_user.groups.filter(name="Customers").exists():
            tag = 1
            current_customer = Customer.objects.get(user=current_user)
        if current_user.groups.filter(name="Salers").exists():
            current_saler = Saler.objects.get(user=current_user)
            tag = 2
    return render(
        request,
        'index.html',
        context={
            'tag': tag,
            'current_customer': current_customer,
            'current_saler': current_saler,
            'itemList1':itemList1,
            'itemList2':itemList2,
            'page':page
        },
    )
    
def indexp(request,pindex):
    tag = 0
    itemList1=Good.objects.all()#[:2]
    paginator = Paginator(itemList1, 4)
    if pindex == "":  # django中默认返回空值，所以加以判断，并设置默认值为1
        pindex = 1
    else:  # 如果有返回在值，把返回值转为整数型
        int(pindex) 
    page = paginator.page(pindex)  # 传递当前页的实例对象到前端
    
    
    
    
    itemList2=Good.objects.filter(genre="2")
    current_customer = Customer.objects.first()
    current_saler = Saler.objects.first()
    current_user = request.user
    
    
    
    if request.user.is_authenticated:
        if current_user.groups.filter(name="Customers").exists():
            tag = 1
            current_customer = Customer.objects.get(user=current_user)
        if current_user.groups.filter(name="Salers").exists():
            current_saler = Saler.objects.get(user=current_user)
            tag = 2
    return render(
        request,
        'index.html',
        context={
            'tag': tag,
            'current_customer': current_customer,
            'current_saler': current_saler,
            'itemList1':itemList1,
            'itemList2':itemList2,
            'page':page
        },
    )
    
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

import uuid

def registerCustomer(request):
    customers = Group.objects.get(name='Customers')
    genreList=Genre.objects.all()
    if request.method == 'POST':
        uname=request.POST['name']
        pwd=request.POST['password1']
        user = User.objects.create_user(username=uname,email=None,password=pwd)
        
        customers.user_set.add(user)
        current_prefer1=Genre.objects.get(name=request.POST['prefer1'])
        current_prefer2=Genre.objects.get(name=request.POST['prefer2'])
        current_prefer3=Genre.objects.get(name=request.POST['prefer3'])
        current_user = user
        current_name=request.POST['name']
        current_id=uuid.uuid4()
        current_age=int(request.POST['age'])
        current_photo=request.FILES.get('photo')
        current_credit=5
        current_grade=0
        current_resume=request.POST['resume']
        Customer.objects.create(
                id=current_id,
                user=current_user,
                name=current_name,
                #age=current_age,
                photo=current_photo,
                credit=current_credit,
                grade=current_grade,
                resume=current_resume,
                )
        return HttpResponseRedirect('/catalog')  
    return render(
        request,
        'registerCustomer.html',
        context={
            'genreList': genreList,
        },
    )
    

    
'''    
def register(request):
    salers = Group.objects.get(name='Salers') 
    customers = Group.objects.get(name='Customers') 
    if request.method == 'POST':
        uname=request.POST['name']
        pwd=request.POST['password1']
        user = User.objects.create_user(username=uname,email=None,password=pwd)
        choice=request.POST['choice']
        if choice=="option1":
            customers.user_set.add(user)
        if choice=="option2":
            salers.user_set.add(user)
        #user.save()
        return HttpResponseRedirect('/catalog')
    return render(request, "register.html")
'''

def viewCustomer(request):
    current_user = request.user
    current_customer = Customer.objects.get(user=current_user)
    tag=1
        

    return render(
        request,
        'viewCustomer.html',
        context={
            'tag': tag,
            'current_customer': current_customer,
        },
    )
    
def viewSaler(request):
   
    current_user = request.user
    tag = 1
    current_saler = Saler.objects.get(user=current_user)
    
    return render(
        request,
        'viewSaler.html',
        context={
            'tag': tag,
            'current_saler': current_saler,
        },
    )
 
def category(request, pk):
    # 记得在开始部分导入 Category 类
    cate = get_object_or_404(Genre, pk=pk)
    good_list = Good.objects.filter(genre=cate)#.order_by('-created_time')
    return render(request, 'good_list.html', context={'good_list': good_list}) 
    
'''   
def completeCustomerInfo(request):
    tag = 0
    current_customer = Customer.objects.first()
    current_user = request.user
    if request.user.is_authenticated:
        if current_user.groups.filter(name="customer").exists():
            tag = 1
            current_customer = Customer.objects.get(user=current_user)
        

    return render(
        request,
        'viewCustomer.html',
        context={
            'tag': tag,
            'current_customer': current_customer,
        },
    )   
'''   
 
