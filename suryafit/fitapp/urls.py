
from django.urls import path 
from fitapp  import views

urlpatterns = [
    
    path('',views.Home,name="Home"),
    path('Signup',views.Signup, name ="signup"),
    path('handlelogin',views.handlelogin, name ="handlelogin"),
    
]
