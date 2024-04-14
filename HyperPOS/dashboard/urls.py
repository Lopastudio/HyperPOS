from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('fm/', views.fm, name='fm'),
    path('data', views.pivot_data, name='pivot_data'),
]