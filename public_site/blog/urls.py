from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('start/', views.BlogStartView.as_view(), name='blogStartPage'),
    path('start/post/<pk>/<slug:slug>', views.PostStartView.as_view(), name='blogStartPost'),
    path('run/', views.BlogRunView.as_view(), name='blogRunPage'),
    path('run/post/<pk>/<slug:slug>', views.PostRunView.as_view(), name='blogRunPost'),
    path('exit/', views.BlogExitView.as_view(), name='blogExitPage'),
    path('exit/post/<pk>/<slug:slug>', views.PostExitView.as_view(), name='blogExitPost'),
]