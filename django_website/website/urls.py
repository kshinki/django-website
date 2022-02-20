from django.urls import path
from .views import IndexViews, AboutViews

urlpatterns = [
    path('', IndexViews.as_view()),
    path('about/', AboutViews.as_view()),
]