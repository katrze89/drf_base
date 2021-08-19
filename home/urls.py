from django.urls import path

from home import views

urlpatterns = [
    path("", views.test_application),
    path("restricted", views.authenticated_view),
    path("admin_view", views.admin_view),
]
