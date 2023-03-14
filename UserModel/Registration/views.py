from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.save()
        return HttpResponse("User registered successfully")

    else:
        form = UserRegistrationForm()
        return render(request, 'Registration/register.html', {'form': form})



def displayy(requset):
    return HttpResponse("<h1>Let's register a new user</h1>")