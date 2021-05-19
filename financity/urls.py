"""financity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',views.blo,name='b1'),
    path('blog1/',views.blog1,name='b2'),
    path('blog2/',views.blog2,name='b3'),
    path('base/',views.base,name="b"),
    path('changepassword/',views.changepassword,name="cp"),
    path('contactus/',views.contact,name="cu"),
    path('editprofile/',views.editprofile,name="ep"),
    path('eservices/',views.eservices,name="es"),
    path('financeminister/',views.financeminister,name="fm"),
    path('footer/',views.footer,name="f"),
    path('forgotpassword/',views.forgotpassword,name='fp'),
    path('header/',views.header,name="he"),
    path('help/',views.help,name="h"),
    path('index/',views.index,name="i"),
    path('login/',views.login,name="l"),
    path('main/',views.main),
    path('minister/',views.minister,name="m"),
    path('profile/',views.profile,name="pro"),
    path('reset/',views.reset,name='r'),
    path('review/',views.review,name="re"),
    path('stateminister/',views.stateminister,name="sm"),
    path('successfullychanged/',views.successfullychanged,name="sc"),
    path('logout/', views.logout, name='logout')
    
]
