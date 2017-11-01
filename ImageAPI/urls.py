"""ImageAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.static import serve
from Image.views import AllImages, ImageId, ImageDetails
from ImageAPI.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^v1/image/$',AllImages),
    url(r'^v1/image/(?P<image_id>\d+)/$',ImageId),
    url(r'^v1/image/(?P<image_id>\d+)/data/$',ImageDetails),
    url(r'^media/(?P<path>.*)/$',serve,{'document_root':MEDIA_ROOT}),
]
handler404 = 'Image.views.page_not_found'
handler403 = 'Image.views.page_prohibit'
handler500 = 'Image.views.page_error'