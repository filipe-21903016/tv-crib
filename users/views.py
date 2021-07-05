from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def login_view(request,user):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('tvcrib:home'))
        else:
            return render(request, "login.html", {'message': "Invalid Credentials."})
    return render(request, 'login.html', {'message': ""})


def logout_view(request):
    logout(request)
    return render(request, 'login.html', {'message': "Logged out."})
