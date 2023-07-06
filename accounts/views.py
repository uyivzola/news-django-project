from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Muvaffaqiyatli login amalga oshirildi')
                else:
                    return HttpResponse('Sorry! You are inactive')
            else:
                return HttpResponse('Login yoki parolda xatolik bor!')
    else:
        form = LoginForm()
        context = {
            'form': form
        }
    return render(request, 'account/login.html', context)


def dashboard_view(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'pages/user_profile.html', context)


def user_register(request):
    # Handle the POST request when the user submits the registration form
    if request.method == 'POST':
        # Create an instance of UserRegistrationForm with the submitted form data
        user_form = UserRegistrationForm(request.POST)

        # Validate the form data
        if user_form.is_valid():
            # Create a new user object without saving it to the database yet
            new_user = user_form.save(commit=False)

            # Set the user's password securely by the meaning HASHING THE NEW PASSWORD INTO THE DATABASE
            new_user.set_password(user_form.cleaned_data['password'])

            # Save the new user to the database
            new_user.save()

            # Redirect to the login page after successful registration
            # Replace 'login' with the appropriate URL pattern name
            # return redirect('login')
            context = {
                'new_user': new_user
            }

            return render(request, 'account/register_done.html', context)

    # Handle the GET request when the user visits the registration page
    else:
        # Create an instance of UserRegistrationForm without any data
        user_form = UserRegistrationForm()
        
        # Prepare the context data to be passed to the template
    context = {'user_form': user_form}

    # Render the registration form template with the context data
    return render(request, 'account/register.html', context)
