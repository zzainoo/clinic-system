from django.urls import path
from .views import *


urlpatterns = [
    path('offers',OfferView.as_view()),
    path('reports',ReportView.as_view()),
    path('register',RegisterView.as_view()),
    path('login',LoginView.as_view()),
    path('account',AccountView.as_view()),
    path('updateuser/<int:pk>',UserupdateView.as_view()),
    path('updatelib/<int:pk>',LibupdateView.as_view()),
    path('libname/<int:pk>',Libdet.as_view()),
    path('addtrain',TrainView.as_view()),
    path('addhouse',HouseView.as_view()),

]


