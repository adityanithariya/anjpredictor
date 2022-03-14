from django.urls import path
from AdmissionPredictor import views

urlpatterns = [
    path('', views.index, name='Admission'),
    path('signin/', views.signIn, name='SignIn'),
    path('signup/', views.signUp, name='SignUp'),
    path('getdata/', views.getData, name='CollegeData'),
    path('predict/', views.predict, name='Predict')
]
