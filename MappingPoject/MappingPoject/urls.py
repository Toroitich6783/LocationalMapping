"""
URL configuration for MappingPoject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from MappingAPP import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.map.as_view(), name='map'),
    path('about',views.about.as_view(),name='about'),
    
    path('error',views.error.as_view(),name='error'),
    path('Allclients',views.Allclients.as_view(),name='Allclients'),
    path('BasicClient',views.BasicClient.as_view(),name='BasicClient'),
    path('blackgray',views.blackgray.as_view(),name='Black_Gray'),
    path('Black_Grayclients',views.Black_Grayclients.as_view(),name='Black_Grayclients'),
    
    
    path('contact',views.contact.as_view(),name='contact'),
    path('Datamanagement',views.Datamanagement.as_view(),name='Datamanagement'),
    path('ecomClients',views.ecomClients.as_view(),name='ecomClients'),
    path('feature',views.feature.as_view(),name='feature'),
    path('Goldclients',views.Goldclients.as_view(),name='Goldclients'),
    path('login',views.login.as_view(),name='login'),
    

    
    
    
    path('Japanese',views.Japanese.as_view(),name='Japanese'),
    path('Japaneseclients',views.Japaneseclients.as_view(),name='Japaneseclients'),
    path('MappingClients',views.MappingClients.as_view(),name='MappingClients'),
    path('Minimalist',views.Minimalist.as_view(),name='Minimalist'),
    path('Minimalistclients',views.Minimalistclients.as_view(),name='Minimalistclients'),


    path('Neo_Traditional',views.Neo_Traditional.as_view(),name='Neo_Traditional'),
    path('Neo_Traditionalclients',views.Neo_Traditionalclients.as_view(),name='Neo_Traditionalclients'),
    path('Realism',views.Realism.as_view(),name='Realism'),
    path('realismclients',views.realismclients.as_view(),name='realismclients'),
    path('service',views.service.as_view(),name='service'),
    path('Traditionalclients',views.Traditionalclients.as_view(),name='Traditionalclients'),
    path('Signup',views.Signup.as_view(),name='Signup'),
    path('SilverClients',views.SilverClients.as_view(),name='SilverClients'),
    path('team',views.team.as_view(),name='team'),
    path('testimonial',views.testimonial.as_view(),name='testimonial'),
    path('Traditional',views.Traditional.as_view(),name='Traditional'),
    

    path('Watercolor',views.Watercolor.as_view(),name='Watercolor'),
    path('Watercolorclients',views.Watercolorclients.as_view(),name='Watercolorclients'),
  
    


]
