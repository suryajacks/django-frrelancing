
from django.urls import path 
from fitapp  import views

urlpatterns = [
    
    path('index', views.Home,name="Home"),
    path('Signup', views.Signup, name ="Signup"),
    path('Student_enroll',  views.Student_enroll, name="Student_enroll"),
    path('handlelogin',views.handlelogin, name = "handlelogin"),
    path("handlelogout",views.handleLogout, name = "handlelogout"),
    path("profile",views.Profile, name = "proile"),
    path("Questions",views.Questions, name = "Questions"),
]
