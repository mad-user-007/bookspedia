from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from .models import Author
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
class AuthorView(DetailView):
    template_name = 'author/profile_view.html'
    model = User

    def get_object(self):
        return User.objects.get(id=self.kwargs.get('user_id'))

class LoginAuthor(FormView):
    template_name = 'author/login.html'
    success_url = '/catalog/home'
    form_class = AuthenticationForm()

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        authenticate(username, password)

        return redirect('home')

def CreateAuthor(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                username = form.cleaned_data['username'],
                email = form.cleaned_data['email'],
                password = form.cleaned_data['password']
            )
            user.save()
            logout(request)
            login(request, user)

            return redirect('home')
        else:
            return render(request, 'author/sign_up.html', context={'form': form})

    else:
        form = SignUpForm()

    if not request.user.is_anonymous:
        author = Author.objects.get(user=request.user)
    else:
        author = None
    return render(request, 'author/sign_up.html', context={'form': form, 'user': request.user, 'author': author})