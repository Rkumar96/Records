
from django.urls import path,include
from . import views
#from . import myapp


urlpatterns = [
    path('', views.index,name='form'),
]
