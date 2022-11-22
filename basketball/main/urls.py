
from django.urls import path
from . import views
urlpatterns = [
  path('', views.index, name='home'),
  path('about', views.about, name='timetable'),
  path('cont/', views.cont, name='cont'),
  path('training/', views.training, name='training')
]