from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework import viewsets
from django.contrib.auth.models import User

from .forms import UserRegisterForm
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Your account has been created. You are now able to Log In.")
			return redirect('login')
	else:
		form = UserRegisterForm()

	return render(request, 'users/register.html', {'form': form})