from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
# Create your views here.

# class SignUpView(CreateView):
#     form_class = UserCreationForm
#     template_name = 'accounts/signup.html'

def SignUpView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog/registration/login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})