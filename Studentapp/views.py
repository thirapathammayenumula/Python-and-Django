from django.shortcuts import render
from .forms import ContactForm,LoginForm,RegisterForm
from .models import ContactModel,RegisterModel
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth


# Create your views here.
def Thanks(request):
	return HttpResponse("<h1>thank you</h1>")
def Home(request):
	context={}
	return render(request,"studentapp/home.html",context)
def About(request):
	context={}
	return render(request,"about.html",context)
def RegisterView(request):
	form_class=RegisterForm
	context={'form':form_class}
	if request.method=="POST":
		print("hiiiiiiiiiiiiiii")
		form=RegisterForm(request.POST)
		if form.is_valid():
			x1=form.cleaned_data['name']
			x2=form.cleaned_data['email']
			x3=form.cleaned_data['password']
			x4=form.cleaned_data['phno']
			RegisterModel.objects.create(name=x1,email=x2,password=x3,phno=x4)
	return render(request,"register.html",context)

def ContactView(request):
	form_class=ContactForm
	context={'form':form_class}
	if request.method=="POST":
		form=ContactForm(request.POST)
		if form.is_valid():
			x=form.cleaned_data['YourName']
			y=form.cleaned_data['YourEmail']
			z=form.cleaned_data['YourMessage']
			ContactModel.objects.create(YourName=x,YourEmail=y,YourMessage=z)
	return render(request,"contact.html",context)
def LoginView(request):
	form_class=LoginForm
	context={'form':form_class}
	if request.method=="POST" :
		form=LoginForm(request.POST)
		vname=request.POST['UserName']
		vpwd=request.POST['Password']
		x=RegisterModel.objects.all().filter(name=vname, password=vpwd).count()
		if x>0:
			print("UserName : ",vname)
			print("Password : ",vpwd)
			return render(request,'dashboard.html',{})
		else:
			print("invalid")
	return render(request,'login.html',context)

def  Dashboard(request):
	context={}
	return render(request,"dashboard.html",context)
from .models import AddstudentModel
from .forms import AddstudentForm
def AddstudentView(request):
	form_class=AddstudentForm
	context={'form':form_class}
	print(request.method)
	if request.method=="POST":
		form=AddstudentForm(request.POST)
		print(form.is_valid())
		if form.is_valid():
			print("Hello thiru")
			x1=form.cleaned_data['name']
			x2=form.cleaned_data['email']
			x3=form.cleaned_data['password']
			x4=form.cleaned_data['gender']
			x5=form.cleaned_data['phno']
			x6=form.cleaned_data['dob']
			x7=form.cleaned_data['city']
			x8=form.cleaned_data['state']
			x9=form.cleaned_data['pincode']
			x10=form.cleaned_data['course']
			x11=form.cleaned_data['add']
			#x12=form.cleaned_data['photo']
			print(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11)
			AddstudentModel.objects.create(name=x1,email=x2,password=x3,gender=x4,phno=x5,dob=x6,city=x7,state=x8,pincode=x9,course=x10,add=x11)
		return render(request,'dashboard.html',{})
	return render(request,"addstudent.html",context)
def StudentDetails(request):
	context={'student':AddstudentModel.objects.all()}
	
	return render(request,'studentdb.html',context)

