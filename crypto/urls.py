from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('prices/', views.prices, name = "prices"),
]

# you give a name to the urls so that we can create links later on (url tagging)
