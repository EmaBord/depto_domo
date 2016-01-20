from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as Login,logout as Logout

template_login = "autenticacion/login.html"
HOME = "lights"
HOME_LOGOUT = 'login'
def login(request):
	if request.user.is_authenticated():
		return redirect(HOME)
	else:
		if request.method == 'POST':
			username = request.POST['user']
			password = request.POST['pass']
			user = authenticate(username=username, password=password)
			if user is not None:
				Login(request, user)
				return redirect(HOME)
			else:
				return render(request,template_login,{'error_login_msg':1})
		else:
			return render(request,template_login)


def logout(request):
	Logout(request)
	return redirect(HOME_LOGOUT)


