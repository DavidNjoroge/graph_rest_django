from django.urls import path,include
from . import views
# from 
urlpatterns = [
    path('',views.StoreInvetory.as_view()),
]