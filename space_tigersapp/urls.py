from django.urls import path
from . import views

#  {% url 'namehere' %} <- put this as the href in the html files

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new_user, name='new_user'), 
    path('users/', views.user_table, name='user_table')
]