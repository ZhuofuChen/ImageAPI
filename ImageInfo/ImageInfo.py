# -*- coding: utf-8 -*-
import os
from ImageAPI.settings import MEDIA_ROOT
from PIL import Image
import json
from PIL.ExifTags import TAGS
import struct
import random


def get_exif_data(fname):
    fileName = MEDIA_ROOT+'\\'+fname
    """Get embedded EXIF data from image file."""
    tag = {}
    try:
        img = Image.open(fileName)
        exifinfo = img._getexif()
        if exifinfo != None:
            for ta, value in exifinfo.items():
                decoded = TAGS.get(ta, ta)
                #Remove unnecessary EXIF attributes and simplify the amount of information
                # If you need a message below, you can remove him from below
                if decoded not in ('LightSource','FlashPixVersion','SceneCaptureType','BrightnessValue','Saturation',
                           'ExposureBiasValue','CustomRendered','SubsecTimeOriginal','FileSource',
                           'Orientation','ExifInteroperabilityOffset','Sharpness','GainControl','MeteringMode','ComponentsConfiguration',
                            'SubjectDistanceRange','Contrast'):
                    tag[decoded] = str(value)
        else:
            height = img.height
            width = img.width
            mode = img.mode
            format = img.format
            palette = img.palette
            info = img.info
            tag['height'] = str(height)
            tag['width'] = str(width)
            tag['mode'] = str(mode)
            tag['format'] = str(format)
            tag['palette'] = str(palette)
            tag['info'] = str(info)
    except IOError:
        print('IOERROR ' + fname)
    tags = json.dumps(tag)
    return tags

# Cut image
def get_image_data(fname):

    fileName = MEDIA_ROOT+'\\'+fname
    try:
        img = Image.open(fileName)
        x = 100
        y = 100
        w = 250
        h = 250
        region = img.crop((x, y, x+w, y+h))
        tem = '\\images\\tem.jpg'
        # Save pictures in temporary image
        region.save(MEDIA_ROOT+'\\images\\tem.jpg')
        return tem
    except:
        pass

# supported file types
# with 16 hexadecimal string to know the file header bytes
# file header is not the same length, less than half of the 2 characters, 8 characters long
def typeList():
    return {
        "FFD8FF": 'JPEG (jpg)',
        "89504E47": 'PNG (png)',
        "47494638": 'GIF (gif)',
        "424D": 'Windows Bitmap (bmp)',
    }

# 字节码转16进制字符串
def bytes2hex(bytes):
    num = len(bytes)
    hexstr = u""
    for i in range(num):
        t = u"%x" % bytes[i]
        if len(t) % 2:
            hexstr += u"0"
        hexstr += t
    return hexstr.upper()

def filetype(fname):
    file = MEDIA_ROOT+'\\'+str(fname).replace('/','\\')
    fileName = unicode(file,"utf-8")
    ftype = 'unknown'
    try:
        binfile = open(fileName, 'rb')
        tl = typeList()
        for hcode in tl.keys():
            numOfBytes = len(hcode) / 2
            binfile.seek(0)
            hbytes = struct.unpack_from("B"*numOfBytes, binfile.read(numOfBytes))
            f_hcode = bytes2hex(hbytes)
            if f_hcode == hcode:
                ftype = tl[hcode]
                break
        binfile.close()
    except:
        pass
    if ftype!='unknown':
        return True
    else:
        os.remove(fileName)
        return False

def random_name():
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
    sa = []
    for i in range(8):
        sa.append(random.choice(seed))
    salt = ''.join(sa)
    return salt