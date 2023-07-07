from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.views.generic import CreateView, View
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Profile
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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

@login_required
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

            Profile.objects.create(user=new_user)
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


""" Creating signup 2nd way """
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'account/register.html'

""" Creating signup 3rd way """
# class SignUpView(View):

#     def post_view(request):
#         # Create an instance of UserRegistrationForm with the submitted form data
#         user_form = UserRegistrationForm(request.POST)

#         # Validate the form data
#         if user_form.is_valid():
#             # Create a new user object without saving it to the database yet
#             new_user = user_form.save(commit=False)

#             # Set the user's password securely by the meaning HASHING THE NEW PASSWORD INTO THE DATABASE
#             new_user.set_password(user_form.cleaned_data['password'])

#             # Save the new user to the database
#             new_user.save()

#             # Redirect to the login page after successful registration
#             # Replace 'login' with the appropriate URL pattern name
#             # return redirect('login')
#             context = {
#                 'new_user': new_user
#             }

#             return render(request, 'account/register_done.html', context)

#     def get_view(request):
#         # Create an instance of UserRegistrationForm without any data
#         user_form = UserRegistrationForm()

#         # Prepare the context data to be passed to the template
#         context = {'user_form': user_form}


#         # Render the registration form template with the context data
#         return render(request, 'account/register.html', context)

@login_required
def edit_user(request):

    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        # If the profile does not exist, create a new one for the user
        profile = Profile(user=request.user)
        profile.save()

    # Check if the request method is POST
    if request.method == 'POST':
        # Get the user form data from the request and the current user's data
        user_form = UserEditForm(instance=request.user, data=request.POST)
        # Get the profile form data from the request, including files, and the current user's profile data
        profile_form = ProfileEditForm(
            instance=request.user.profile, data=request.POST, files=request.FILES)

        # Check if both forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            # If the forms are valid, save the updated user and profile information
            user_form.save()
            profile_form.save()
            return redirect('profile')
        else:
            # If the forms are not valid, render the template with the error messages and the filled-in forms
            context = {
                'user_form': user_form,
                'profile_form': profile_form
            }
            return render(request, 'account/profile_edit.html', context)
    else:
        # If the request method is GET (not POST), display the form to the user with their current data pre-filled
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

        # Prepare the form data to be displayed in the template
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }

        # Render the template with the form data
        return render(request, 'account/profile_edit.html', context)

class EditUserView(LoginRequiredMixin, View):
    
    def get(self, request):
        # If the request method is GET (not POST), display the form to the user with their current data pre-filled
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

        # Prepare the form data to be displayed in the template
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }

        # Render the template with the form data
        return render(request, 'account/profile_edit.html', context)

    def post(self, request):
        # Get the user form data from the request and the current user's data
        user_form = UserEditForm(instance=request.user, data=request.POST)
        # Get the profile form data from the request, including files, and the current user's profile data
        profile_form = ProfileEditForm(
            instance=request.user.profile, data=request.POST, files=request.FILES)

        # Check if both forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            # If the forms are valid, save the updated user and profile information
            user_form.save()
            profile_form.save()
            return redirect('profile')
        else:
            # If the forms are not valid, render the template with the error messages and the filled-in forms
            context = {
                'user_form': user_form,
                'profile_form': profile_form
            }
            return render(request, 'account/profile_edit.html', context)