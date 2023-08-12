from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def login_page(request):
    # # We make the method's name login_page because 'login' is already taken by Django
    # if request.user.is_authenticated and request.session['username']:  # If already logged in, login page in not available anymore
    #     return redirect('index')
    # if request.method == "POST":
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     user = authenticate(request, username=username, password=password)
    #     request.session['username'] = username
    #     if user is not None:
    #         # if user successfully logged in
    #         login(request, user)
    #         return redirect('index')
    context = {}
    return render(request, "login.html", context)


def logout_page(request):
    request.session.clear()     # Clear session
    logout(request)
    return redirect('login')
