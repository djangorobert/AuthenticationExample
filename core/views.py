
from django.views.generic.edit import CreateView, FormView
from .forms import CustomUserCreationForm, UserLoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class HomeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response({
            "email": request.user.email

        })



@login_required
def home(request):
    context = {

    }
    return render(request, 'home.html',  context)



class SignupView(CreateView):
    form_class = CustomUserCreationForm
    success_url = 'accounts/login'
    template_name = 'registration/signup.html'


#The Custom Login and Logout Views
def login_view(request):
    next = request.GET.get('next') #/premium/
    form = UserLoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            auth_user = authenticate(username=username, password=password)
            login(request, auth_user)
            messages.info(request, 'Succesfully Logged in.')
            if next:
                return redirect(next)
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, "registration/login.html", context)








def logout(request):
    return render(request, 'registration/logout.html')