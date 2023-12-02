from django.contrib import admin
from django.urls import path , include


from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('meals/', include('meals.urls')),
    path('about/', include('About_Us.urls')),
    
]
