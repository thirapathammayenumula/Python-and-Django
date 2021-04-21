from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^Imgupload/',UploadView.as_view()),
    #url(r'^imgdisplay/',CompleteView.as_view()),
    url(r'^imgdisplay/',GetImage.as_view()),
]
    