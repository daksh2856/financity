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
from django.conf import settings
from django.conf.urls.static  import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',views.blo,name='b1'),
    path('blog1/',views.blog1,name='b2'),
    path('blog2/<int:id>',views.blog2,name='b3'),
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
    path('index1/',views.index1,name="i1"),
    path('login/',views.login,name="l"),
    path('main/',views.main),
    path('nse/',views.nse,name="n"),
    path('nse1/',views.nse1,name="n1"),
    path('nse2/',views.nse2,name="n2"),
    path('nse3/',views.nse3,name="n3"),
    path('minister/',views.minister,name="m"),
    path('pridiction/',views.p1,name="p1"),
    path('profile/',views.profile,name="pro"),
    path('reset/',views.reset,name='r'),
    path('review/',views.review,name="re"),
    path('stateminister/',views.stateminister,name="sm"),
    path('setting/',views.setting,name="se"),
    path('successfullychanged/',views.successfullychanged,name="sc"),
    path('logout/', views.logout, name='logout'),
    path('gdp/', views.d1, name='dy1'),
    path('api1/', views.d2, name='dy2'),
    path('gold/', views.d3, name='dy3'),
    path('expense/', views.d4, name='dy4'),
    path('dashboard/', views.dashboard, name='dash'),
    path('graphic/', views.graphic, name='graph'),

    path('gdp1/', views.gdp1, name='g1'),
    path('gdp2/', views.gdp2, name='g2'),
    path('gdp3/', views.gdp3, name='g3'),
    path('gdp4/', views.gdp4, name='g4'),
    path('gdp5/', views.gdp5, name='g5'),
    path('gdp6/', views.gdp6, name='g6'),
    
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)