from django.shortcuts import render

# Create your views here.

# monitoring/views.py

from django.shortcuts import render, redirect
from .utils import authenticate_ldap

# monitoring/views.py

from django.shortcuts import render, redirect

def dashboard(request):
    if 'username' in request.session:
        return render(request, 'dashboard.html', {'username': request.session['username']})
    else:
        return redirect('login')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if authenticate_ldap(username, password):
            request.session['username'] = username
            return redirect('dashboard')
        else:
            error = 'Invalid credentials. Please try again.'
            return render(request, 'login.html', {'error': error})
    else:
        return render(request, 'login.html')

def logout(request):
    request.session.pop('username', None)
    return redirect('login')