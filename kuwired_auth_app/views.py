# accounts/views.py

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import CustomUser
from .forms import Registration_Form
import uuid

def register_view(request):
    if request.method == "POST":
        form = Registration_Form(request.POST)
        email = request.POST.get('email')
        if form.is_valid():
            user = form.save()
            user.confirmation_token = uuid.uuid4()  # Generate a unique confirmation token
            user.is_active = False  # Deactivate account until email is confirmed
            user.save()
            
            # Generate confirmation URL
            confirmation_url = reverse('confirm_email', args=[user.confirmation_token])
            # Send confirmation email
            subject = 'Please confirm your email address'
            message = render_to_string('registration/email_confirmation.html', {
                'user': user,
                'domain': get_current_site(request).domain,
                'confirmation_url': confirmation_url,
            })
            try:
                print(message)  # For debugging purposes
                send_mail(subject, message, 'info@kuwired.tech', [email])
            except Exception as e:
                messages.error(request, f'Error sending confirmation email: {str(e)}')
                return redirect('home')

            messages.success(request, 'Registration successful! Please check your email to confirm your account.')
            return redirect('registration_confirmation')  # Redirect to confirmation page
    else:
        form = Registration_Form()

    return render(request, 'registration/register.html', {'form': form})


def registration_confirmation(request):
    return render(request, 'registration/registration_confirmation.html')


def confirm_email(request, confirmation_link):
    try:
        # Attempt to find the user based on the confirmation link
        user = CustomUser.objects.get(confirmation_token=confirmation_link)
        user.is_active = True  # Or any other activation logic
        user.save()
        return render(request, 'registration/confirmation_success.html')  # Render a success page
    except CustomUser.DoesNotExist:
        return HttpResponse("Invalid confirmation link", status=400)
    

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next') or 'home'
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid credentials!')  # Use messaging framework
            return render(request, 'accounts/login/login.html')

    return render(request, 'accounts/login/login.html')


def logout_view(request):
    if request.method == 'POST':
        logout(request)  # Remove user from the request
        return redirect('login')
    else:
        return redirect('home')