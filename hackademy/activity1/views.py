from django.shortcuts import render
from urllib import request
from .models import Profile

from django.http import HttpResponse

HTML_STRING = """
<h1> Welcome to home page!</h1>
"""

def home(request):
    return HttpResponse(HTML_STRING)

def profile(request):

    user = request.user
    context = {
        'user': user
    }

    return render(request, 'profile.html', context)


from django.http import HttpResponseRedirect
from .forms import OverrideRegistrationForm
from django.contrib.auth.views import LoginView

def registration(request):
    if request.method == 'POST':
        form = OverrideRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = OverrideRegistrationForm()
    context = {
        'form': form
    }

    return render(request, 'registration.html', context)

class Login(LoginView):
    template_name = 'login.html'
 