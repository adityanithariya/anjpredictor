from django.urls import path
from JobPredictor import views

urlpatterns = [
    path('', views.index, name='index'),
]
