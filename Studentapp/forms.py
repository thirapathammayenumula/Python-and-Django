from django import forms
from .models import ContactModel,AddstudentModel,RegisterModel
import datetime
from django.forms.widgets import RadioSelect
class ContactForm(forms.ModelForm):
	class Meta:
		model=ContactModel
		fields=('YourName','YourEmail','YourMessage')


class RegisterForm(forms.ModelForm):
	class Meta:
		model=RegisterModel
		fields=('name','email','password','phno')


class LoginForm(forms.Form):
	UserName=forms.CharField(max_length=30)
	Password=forms.CharField(widget=forms.PasswordInput(),max_length=30)
city=[('ongole','ongole'),('addanki','addanki'),('darsi','darsi'),('podili','podili')]
states=[('Ap','Ap'),('Telengana','Telengana'),('gujarat','gujarat'),('karnataka','karnataka')]
courses=[('python','python'),('django','django'),('sql','sql'),('linux','linux')]


class AddstudentForm(forms.ModelForm):
	name=forms.CharField(max_length=100,widget= forms.TextInput(attrs={'placeholder':'Enter your first name'}))
	email=forms.EmailField(max_length=100,widget= forms.EmailInput(attrs={'placeholder':'Enter your email'}))
	password=forms.CharField(widget=forms.PasswordInput(),max_length=30)
	gender=forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=(('Female','Female'),('Male','Male'),('Others','Others')))
	phno=forms.IntegerField()
	dob =forms.DateField(initial=datetime.date.today,help_text='please enter yyyy-mm-dd format')
	city=forms.ChoiceField(choices=city)
	state=forms.ChoiceField(choices=states)
	pincode=forms.IntegerField()
	course=forms.ChoiceField(label="Course Name",choices=courses)
	add=forms.TextInput()
	#photo = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
	class Meta:
		model=AddstudentModel
		fields=('name','email','password','gender','phno','dob','city','state','pincode','course','add')
	



		
			
