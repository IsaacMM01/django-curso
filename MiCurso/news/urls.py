from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name = "index"),
    path("login/", views.login, name = "login"),
    path("signUp/", views.signUp, name = "signup"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
