from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm 

# Create your views here.
def register_request(request):
    if request.method == "POST":
        print(request.POST)
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("register")
    form = NewUserForm()
    return render (request=request, template_name="register.html", context={"form":form})


def login_request(request):
    if request.method == "POST":
        # check in the auth_user table withe username and password
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # check in the auth_session table and if true, return user object
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            # print(user)
            if user is not None:
                login(request, user)
				# messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                pass
        else:
			# messages.error(request,"Invalid username or password.")
            pass
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
    logout(request)
    return redirect("login_user")