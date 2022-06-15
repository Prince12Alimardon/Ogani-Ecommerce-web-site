from django.shortcuts import render
from .models import Profile

# Create your views here.


def profile(request):
    prof = Profile.objects.get(user=request.user)
    ctx = {
        'profile': prof
    }
    return render(request, 'profile.html', ctx)
