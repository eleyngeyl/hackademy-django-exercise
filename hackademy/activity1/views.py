from django.shortcuts import render
from .models import Profile

# Create your views here.

def profile(request):
    user = request.user
    context = {
        'user': user
    }

    return render(request, 'profile.html', context)
