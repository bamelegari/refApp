"""refApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from refdb import views
from accounts import views as accounts_views


urlpatterns = [
    url(r'^$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
	url(r'^login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
	url(r'^home/', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^reports/', views.reports, name='reports'),
    url(r'^stats/', views.stats, name='stats'),
    url(r'^referees/', views.referees, name='referees'),
    url(r'^account/', accounts_views.account, name='account'),
    url(r'^logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    url(r'^assignments/', views.assignments, name='assignments'),
    url(r'^assign/', views.assign, name='assign'),
    url(r'^assess/', views.assess, name='assess'),
    url(r'^testScores/', views.testscores, name='testScores'),
    url(r'^addUser/', views.adduser, name='addUser'),
    url(r'^denied/', accounts_views.denied, name='denied'),
]