from django.shortcuts import render ,redirect
from django.contrib.auth.models import User

# Create your views here.
def Home(request):
    return render(request,"index.html")

def Signup(request):
        if request.method =="Post":
           username =request.Post.get('username')
           email  =request.Post.get('email')
           pass1 = request.Post.get('pass1')
           pass2  =request.Post.get('pass2')
           if pass1==pass2:
              message.info(request,"password matched")
              return redirect("/index")
           else:
              message.warning(request,"password not matched")
              return redirect("/signup")
       
        try:
               if user.objects.get(username=username):
                 message.warning(request,"username already taken")
                 return redirect("/signup")
             
        except Exception as identifier:
               pass 
           
        try:
               if user.objects.get(email=email):
                 message.warning(request,"email already taken")
                 return redirect("/signup")
             
        except Exception as identifier:
               pass 
           myuser=User.objects,create_user(username,email,pass1)
           myuser.first_name=firstname
           myuser.lastname=lastname
           myuser.save()
           message.success(request,"user is created Please Login")
           return redirect("/login")
       
        return redirect(request,"/signup")


def handlelogin(request):
    return render(request,"Login.html")

