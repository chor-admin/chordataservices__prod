from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('start/', views.BlogStartView.as_view(), name='blogStartPage'),
    path('start/post/<pk>/<slug:slug>', views.PostView.as_view(), name='blogStartPost'),
]