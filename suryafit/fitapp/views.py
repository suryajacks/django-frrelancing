from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from fitapp.models import Student1 ,Student_course,Question3,Admin_Questions

def Home(request):
    Student =Student1.objects.all()
    context ={"Student":Student}
    return render(request,"index.html",context)

def Signup(request):
    if request.method=="POST":
       username=request.POST.get('username')
       email  =request.POST.get('email')
       pass1  =request.POST.get('pass1')
       pass2  =request.POST.get('pass2')
       if pass1  != pass2:
          messages.info(request,"password not  matched")
          return redirect("/Signup")
       try:
          if User.objects.get(Username=username):
             messages.warning(request,"Username already taken")
             return redirect('/Signup')
             
         
       except Exception as identifiers:
          pass
       try:
          if User.objects.get(email=email):
             messages.warning(request,"email already taken")
             return redirect('/Signup')
         
       except Exception as identifier:
          pass
       
       
       
       
       myuser=User.objects.create_user(username,email,pass1)
       myuser.save()
       messages.success(request,"User is created Please Login")
       return redirect('/handlelogin')
    
    return render(request,"Signup.html")



def handlelogin(request):
   if request.method == "POST":
      username = request.POST.get('username')
      pass1    = request.POST.get('pass1')
      myuser   = authenticate(username=username,password=pass1)
      if myuser is not None:
         login(request,myuser)
         messages.success(request,"login succesfully")
         return redirect('/index')
      else:
         messages.warning(request,"invalid credentails")
         return redirect('/handlelogin')
         
   return render(request,"handlelogin.html")    

def handleLogout(request):
    logout(request)
    messages.success(request,"Logout Success")    
    return redirect('/handlelogin')  
   
   
def Student_enroll(request):
   if not request.user.is_authenticated:
      messages.warning(request,"Please Login and Try Again")
      return redirect('/handlelogin')
   
   course=Student_course.objects.all()
   context={"course":course}
      
   if request.method=="POST":
      name       =request.POST.get('name')
      fathername=request.POST.get('fathername')
      age        =request.POST.get('age')
      dateofbirth=request.POST.get('dob')
      address    =request.POST.get('address')
      college    =request.POST.get('college')
      course      =request.POST.get('course')
      degree     =request.POST.get('degree')
      email      =request.POST.get('email')
      mobilenumber=request.POST.get('mobilenumber')
      query=Student1(Name1=name,Father_name1=fathername,Age1=age,Date_of_birth1=dateofbirth,address1=address,College1=college, Course1 =course,Degree1=degree,Email1=email,Mobile_number1=mobilenumber)
      query.save()
      messages.info(request,"Student Enrollment Completed Sucessfully")
      return redirect('/Student_enroll')
   
   
   
   return render(request,"Student_enroll.html",context)



def Profile(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/handlelogin')
    Student =Student1.objects.all()
    context ={"Student":Student}
   
    return render(request,"profile.html",context)
 
 
 
def Questions(request):
    if not request.user.is_authenticated:
      messages.warning(request,"Please Login and Try Again")
      return redirect('/handlelogin')
    Adminques=Admin_Questions.objects.all()
    
    context = {"Adminques":Adminques}
    if request.method=="POST":
       q1=request.POST.get('contact')
       q2=request.POST.get('contact1')
       q3=request.POST.get('contact2')
       query=Question3(Answer1=q1,Answer2=q2,Answer3=q3)
       query.save()
    
   
    return render(request,"Questions.html",context)
  
   
   
    
      
      
       
    