from django.shortcuts import render
from django.http import HttpResponse
menu =[{'title':"Главная",'url_name':'home'},
       {'title':"Книги",'url_name':'book'},
       {'title':"Заказы",'url_name':'order'},
       {'title':"Войти",'url_name':'login'},]

def main(request):
    return render(request,'book/main.html',{'title':"Main",'menu':menu} )

def book(request):
    return render(request,'book/book.html',{'title':"Books",'menu':menu} )


def order(request):
    return render(request,'book/order.html',{'title':"Order",'menu':menu} )

def login(request):
    return render(request,'book/login.html',{'title':"Login",'menu':menu} )