# -*- coding: utf-8 -*-
from rest_framework import serializers
# from Image.models import Image
from Image.models import Images


class Image_List(serializers.ModelSerializer):
    class Meta:
        model = Images
        # model = Image
        fields = ('image',)