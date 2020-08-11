from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm,profileCreationForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context


##################################################################
####################index#######################################
def index(request):
    return render(request, 'user/index.html',{'title':'index'})

########################################################################
########### register here #####################################

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        print(form)
        if form.is_valid():

            '''
            username = request.POST['username']
            phone_no = request.POST['phone_no']
            user = form.save()
            profile = user.userprofile
            user_group = form.cleaned_data.get('user_type')
            gender = form.cleaned_data.get('gender')
            firstname = form.cleaned_data.get('firstname')

            profile.user_type = user_group
            profile.gender = gender
            profile.save()

            '''
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form,'title':'reqister here'})

###################################################################################
################login forms###################################################

def Login(request):
    if request.method == 'POST':

        #AuthenticationForm_can_also_be_used__

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request,user)
            messages.success(request, f' wecome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form':form,'title':'log in'})

########### profile creation here #####################################

def profile(request):
    if request.method == 'POST':
        form = profileCreationForm(request.POST)
        if form.is_valid():

            user = form.save()
            profile = user.userprofile
            Experience = form.cleaned_data.get('Experience')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')

            profile.Experience = Experience
            profile.first_name=first_name
            profile.last_name=last_name
            profile.save()


            form.save()
            messages.success(request, f'Profile details created')
            return redirect('login')
    else:
        form = profileCreationForm()
    return render(request, 'user/profile.html', {'form': form,'title':'Profile Submit'})

