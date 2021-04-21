from django.shortcuts import render
from PIL import Image
# Create your views here.
from django.shortcuts import render
from .models import ImgModel
from django.http import HttpResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
import pdb
import json
#import Image
from django.http import HttpResponseRedirect
import os
from django.conf import settings
from django.conf.urls.static import static
from django.core.files.storage import default_storage

class UploadView(View):
     @method_decorator(csrf_exempt)
     def dispatch(self, *args, **kwargs):
        return super(UploadView,self).dispatch(*args,**kwargs)
     def get(self,request, *args, **kwargs):
        print("gggggggggggggggg")
        r=ImgModel.objects.all()
        return render(request,'upload.html',locals())
     def post(self,request, *args, **kwargs):
        #import pdb;
        #pdb.set_trace();
        print('ppppppppppppppppppp')
        for i in request.FILES.getlist("fileUpload"):
           print(i)
           img1=i
           imgname =(str(img1.name)).split('.')[0]+'.JPEG'
           img_path=os.path.join(os.path.join(os.path.join(settings.BASE_DIR, 'media'),'Images'),imgname)
           default_storage.save(str(img_path), img1)
           r=ImgModel()
           r.iname = imgname#'Images/'+
           r.images = img_path#'Images/'+
           r.save()
        resp = HttpResponse(content_type="application/json", status=200)
        #return resp
        return HttpResponseRedirect('/imgupload/imgdisplay/') 


class GetImage(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(GetImage,self).dispatch(*args,**kwargs)
    def get(self,request, *args, **kwargs):
        print("gggggggggggggggg")
        r=ImgModel.objects.filter(flag='0')
        #if r.flag==0:
           #r.flag=1
		
		#order_by("id").reverse()
        return render(request,'images.html',locals())
      
'''	    
class CompleteView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(CompleteView,self).dispatch(*args,**kwargs)
    def get(self,request, *args, **kwargs):
        print("gggggggggggggggg")
        g=ImgModel.objects.order_by("id").reverse()[:1]
        return render(request,'imgdisplay.html',locals())
'''