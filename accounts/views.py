from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy


def user_signup(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("user_signin")
	else:
		form = UserCreationForm()
	return render(request, "signup_page.html", {"form": form})


class UserSigninView(LoginView):
	template_name = "signin_page.html"

	def get_success_url(self):
		return reverse_lazy("dashboard")


class UserSignoutView(LogoutView):
	next_page = reverse_lazy("user_signin")


@login_required
def dashboard_view(request):
	return render(request, "dashboard.html", {"user": request.user})
