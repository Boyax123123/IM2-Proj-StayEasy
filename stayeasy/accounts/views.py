from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_exempt
from .models import Accounts
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ValidationError
# Create your views here.
# @csrf_protect


def profile(request):
    return render(request, 'accounts/profile.html')

def test(request):
    accounts = Accounts.objects.all()
    return render(request, 'accounts/test.html', {'accounts': accounts})



@csrf_exempt
def signup_view(request):
    if request.method == "POST":
        if 'hostsignup' in request.POST:
            role = 'host'
        else:
            role = 'customer'     
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():   
            user = form.save(commit=False)
            user.role = role
            user.save()  
            if 'profile_picture' in request.FILES:
                user.profile_picture = request.FILES['profile_picture']
                user.save()
                
            return redirect('landingpage')
    else:
        form = SignupForm()

    return render(request, 'accounts/signup.html', {'form': form})
# @csrf_protect



@csrf_exempt
def login_view(request):
    if request.user.is_authenticated:
        redirect('landingpage')
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Retrieve the cleaned data from the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Authenticate user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Use the correct login method from django.contrib.auth
                return redirect('landingpage')  # Redirect to a homepage or dashboard
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")  # Optional success message
    return redirect('landingpage') 

def remove_account(request):
    if request.method == "POST":
        request.user.delete()
        messages.success(request, "Your account has been deleted.")
        return redirect('landingpage')
    return redirect('accounts:account_settings')

# wallet=====


# wallet===========
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required
def deposit(request):
    if request.method == "POST":
        try:
            amount = int(request.POST.get("amount"))
            if amount > 0:
                request.user.balance += amount
                request.user.save()
                return JsonResponse({
                    "status": "success",
                    "message": f"₱{amount} successfully added to your wallet!",
                    "new_balance": request.user.balance
                })
            else:
                return JsonResponse({"status": "error", "message": "Invalid amount entered."})
        except ValueError:
            return JsonResponse({"status": "error", "message": "Please enter a valid number."})
    return JsonResponse({"status": "error", "message": "Invalid request method."})



@login_required
def account_settings(request):
    if request.method == "POST":
        if "delete_picture" in request.POST:
            request.user.profile_picture.delete()
            request.user.profile_picture = 'images/iconProfileDefault.jpg'
            request.user.save()
        else:
            request.user.username = request.POST.get("username", request.user.username)
            request.user.first_name = request.POST.get("first_name", request.user.first_name)
            request.user.last_name = request.POST.get("last_name", request.user.last_name)
            request.user.email = request.POST.get("email", request.user.email)
            if "phone_number" in request.POST:
                phone_number = request.POST.get("phone_number", request.user.phone_number)
                if not phone_number.isdigit() or len(phone_number) < 10:
                    raise ValidationError("Invalid phone number")  # Validate the phone number
                request.user.phone_number = phone_number
            if password := request.POST.get("password"):
                request.user.set_password(password)
            if "profile_picture" in request.FILES:
                request.user.profile_picture = request.FILES["profile_picture"]
            request.user.save()
            return HttpResponseRedirect(reverse('accounts:account_settings'))

    return render(request, 'accounts/account_settings.html')


@csrf_exempt
@login_required
def remove_account(request):
    if request.method == "POST":
        request.user.delete()
        messages.success(request, "Your account has been deleted.")
        return redirect('landingpage')
    return redirect('accounts:account_settings')
