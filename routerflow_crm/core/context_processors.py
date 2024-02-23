from django.urls import reverse


def site_urls(request):
    return {
        "home_url": reverse("core:home"),
        "dashboard_url": reverse("core:dashboard"),
    }
