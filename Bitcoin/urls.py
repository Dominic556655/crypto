from django.urls import path
from . import views


urlpatterns = [
        path('', views.index, name = 'index'),
        path('Home', views.dashboard, name= 'Home'),
        path('dashboard', views.dashboard, name='dashboard'),
        path('Register', views.Register, name = 'Register'),
        path('logout', views.logout, name='logout'),
        path('login', views.Login, name='login'),
        path('about', views.about, name='about'),
        path('plan', views.plan, name = 'plan'),
        path('deposit', views.deposit, name='deposit'),
        path('news', views.news, name='news'),
        path('single-blog.html', views.single_blog, name='single-blog'),

    ]