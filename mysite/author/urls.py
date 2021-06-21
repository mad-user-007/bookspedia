from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_id>/', views.AuthorView.as_view(), name="user_profile"),
    path('sign_up/', views.CreateAuthor, name="sign_up")
]
