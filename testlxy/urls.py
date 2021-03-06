"""testlxy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from applxy import views as applxy_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', applxy_views.index, name="index"),
    url(r'^add/(\d+)/(\d+)/$', applxy_views.add, name='add'),

    url(r'^v1/login$', applxy_views.login, name='login'),
    url(r'^v1/logOut$', applxy_views.logOut, name='logOut'),
    url(r'^v1/register', applxy_views.register, name='register'),
    url(r'^v1/changePasswd', applxy_views.changePasswd, name='changePasswd'),
    url(r'^v1/purchaseHistory', applxy_views.purchaseHistory, name='purchaseHistory'),
    url(r'^v1/product', applxy_views.product, name='product'),
]
