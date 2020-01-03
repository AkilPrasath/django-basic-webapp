from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required


def login(request):


    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate( username=username, password=password )
        if user is not None :
            auth_login(request, user)
            request.session['username']=request.POST['username']
            return redirect('home')
        else:
            messages.error(request, "Invalid Login Credentials!" )
            return render( request, 'login.html' )
    try:
        if request.session['username'] is None:
            pass
        return render(request,'home.html')
    except :
        return render(request,'login.html')
        
def logout(request):
    auth_logout(request)
    messages.success(request, "Logged out!")
    return redirect('login')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['mail']
        password = request.POST['password']
        user = User.objects.create_user(username=username ,first_name=firstname, last_name = lastname, email= email, password=password)
        messages.success(request,"Account Registered Successfully!!")
        return redirect('login')
    return render(request,'register.html')


def home(request):
    if request.user.is_authenticated:
        print(request.user.first_name)
        print(datetime.datetime.now())

        return render(request,'home.html')
    else:
        messages.error(request, "Login to continue")
        return redirect('login')


def form(request):
    if request.method == 'POST':
        post = request.POST['post']
        category_name = request.POST['category']
        user = User.objects.get(username = request.session['username'])
        category = Category.objects.get( title = category_name )
        post = Post.objects.create( Posttext=post, category = category, user= user )
        print(post)

        return render(request,'home.html')
        
    return render( request, 'form.html' )

def table(request):
    forms = Post.objects.all()
    return render( request, 'table.html', {'forms':forms} )


def post_edit(request,pk):
    if request.method=="POST":
        post = request.POST['post']
        category_name = request.POST['category']
        user = User.objects.get(username = request.session['username'])
        category = Category.objects.get( title = category_name )
        post = Post.objects.filter(id=pk).update(date_time= datetime.datetime.now() ,Posttext=post, category = category, user= user )
        messages.success(request,'Updated Successfully!!')
        return redirect('/table')
    posts= Post.objects.filter(id=pk)
    for post in posts:
        pass
    return render( request, 'edit.html', {'post':post} )

def delete(request,pk):
    posts = Post.objects.filter(id=pk)
    for post in posts:
        post.delete()
    return redirect('table')
