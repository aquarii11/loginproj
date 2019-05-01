from django.conf.urls import url
from loginapp import views
app_name ='loginapp'
urlpatterns = [
    url("^register$",views.register,name="register"),
    url("^$",views.index,name="index"),
    
]
