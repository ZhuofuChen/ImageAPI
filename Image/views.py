# -*- coding: utf-8 -*-
import os
from PIL import Image
from django.http.response import HttpResponse
# from Image.models import Image
# from Image.serializers import Image_List
from Image.models import Images
from mongoengine import connect
from Image.serializers import Image_List
from ImageAPI.settings import MEDIA_ROOT
from ImageInfo.ImageInfo import get_exif_data, get_image_data, filetype, random_name
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view

connect('images', host='localhost', port=27017)
# Heavy duty JsonResponse
class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        content='{"image":'+content+'}'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def AllImages(request):

    # Processing GET requests
    if request.method == 'GET':
        # all_images = Image.objects.all()
        all_images = Images.objects.all()
        serializer = Image_List(all_images, many=True)
        return JSONResponse(serializer.data)

    # Processing POST requests
    if request.method == 'POST':
        # You can upload multiple image at the same time
        files = request.FILES.getlist('images')
        if files :
            for f in files:
                # image = Image()
                image = Images()
                # try:
                save_img = Image.open(f)
                image_name = MEDIA_ROOT+'\\'+"%s.jpg"%random_name()
                save_img.save(image_name)#保存图片
                img = open(image_name,'rb')
                image.image.put(img, content_type = 'image/jpg')
                image.save()

                # if filetype(str(image.image)):
                return HttpResponse("{'state':'ready'}", content_type='application/json')
                # else:
                #     image.delete()
                # return HttpResponse("{'state':'TypeError'}", content_type='application/json')
                # except:
                #     return HttpResponse("{'state':'TypeError'}", content_type='application/json')

        else:
            return HttpResponse("{'state':'fail'}", content_type='application/json')

@csrf_exempt
def ImageDetails(request,image_id):
    # Processing GET requests
     if request.method == 'GET':
        # image = Image.objects.get(id=image_id)
        image = Images.objects.get(id=image_id)
        tem_image = get_image_data(str(image.image))
        fileName = MEDIA_ROOT+'\\'+tem_image
        image_data = open(fileName,"rb").read()
        return HttpResponse(image_data,content_type="image/png")
     else:
         return HttpResponse("{'state':'fail'}", content_type='application/json')

@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def ImageId(request,image_id):
    # Processing GET requests
     if request.method == 'GET':
        # image = Image.objects.get(id=image_id)
        image = Images.objects.get(id=image_id)
        image_dirs=str(image.image).replace('/','\\')
        data = get_exif_data(image_dirs)
        return HttpResponse("{'ImageData':%s}"%data,content_type='application/json')

    # Processing PUT requests
     if request.method == 'PUT':
        #  Find if ID exists
        image = Images.objects.get(id=image_id)
        # image = Image.objects.get(id=image_id)
        # tem_image = Image()
        tem_image = Images()
        tem_image.image=image.image
        tem_image.save()
        data=request.data
        files = data.get('images')
        if files and image:
            # replace
            image.image=files
            image.save()
            if filetype(str(image.image)):
                file = MEDIA_ROOT+'\\'+str(tem_image.image).replace('/','\\')
                fileName = unicode(file,"utf-8")
                os.remove(fileName)
                tem_image.delete()
                return HttpResponse("{'state':'ready'}", content_type='application/json')
            else:
                image.image = tem_image.image
                image.save()
            return HttpResponse("{'state':'TypeError'}", content_type='application/json')
        else:
            return HttpResponse("{'state':'fail'}", content_type='application/json')

def page_not_found(request):
    return HttpResponse("{'state':'404'}", content_type='application/json')

def page_error(request):
    return HttpResponse("{'state':'503'}", content_type='application/json')


def page_prohibit(request):
    return HttpResponse("{'state':'403'}", content_type='application/json')