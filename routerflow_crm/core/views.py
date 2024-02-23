from django.shortcuts import redirect
from django.shortcuts import render


def home_view(request):
    return redirect("core_dashboard")


def dashboard_view(request):
    return render(request, "pages/dashboard.html")
