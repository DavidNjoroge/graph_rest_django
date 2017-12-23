from django.urls import path,include
from . import views
# from 
urlspatterns = [
    path('',views.StoreInvetory.as_view())
]