from django.conf.urls import url
from .views import Home,About,ContactView,LoginView,Thanks,Dashboard,AddstudentView,StudentDetails,RegisterView
urlpatterns = [
    url(r'^home/',Home,name='home'),
    url(r'^about/',About,name='about'),
    url(r'^contact/',ContactView,name='contact'),
    url(r'^login/',LoginView,name='login'),
    url(r'^thanks/',Thanks,name='thanks'),
    url(r'^dash/',Dashboard,name='dash'),
    url(r'^add/',AddstudentView,name='add'),
    url(r'^register/',RegisterView,name='register'),
    url(r'^studentdb/',StudentDetails,name='studentdb'),





]