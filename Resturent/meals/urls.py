from django.urls import path , include


from . import views
urlpatterns = [
    path('meals/', views.meal , name='meals'),

]