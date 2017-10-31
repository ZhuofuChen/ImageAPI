# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from mongoengine import *
# Create your models here.
# from Image.serializers import Image_List



# Design database fields

# connect('blog')
# # connect('blog', host='127.0.0.1', username='root', password='')
#
# from ImageAPI.settings import DBNAME

#
class Images(Document):
	image = ImageField()
	# image = StringField()
	add_time = DateTimeField(default=datetime.now,verbose_name='add_time')
	# class Meta:
	# 	ordering = ('add_time',)
	# def __unicode__(self):
	# 	return self.image


# makemigrations
# migrate

#
# all_images = User.objects()
# for u in all_images:
#     print(u.image)
#
# serializer = Image_List(all_images, many=True)
# z1 = JSONResponse(serializer.data)
# page = User(image='zzdahuidhas')
# print(page.id)
#
# page.save()
# print(page.id)
# # station = User.objects(id = page.id).first()
#
# # print(station)
# print(all_images)
# user1 = User(
#     image='zzdahuidhas',
# )
# user1.save()
# print(user1.image)
# user1.image = 'zz11'
# user1.save()
# station = User.objects(_id = '59f5b0c1ad6e2d2f446d2ea5').first()
# print(station)
# print(user1._id)
# class Images(models.Model):
# 	image = models.ImageField(max_length=100,verbose_name='image',default='',upload_to='images/%Y')
# 	add_time = models.DateTimeField(default=datetime.now,verbose_name='add_time')
# 	class Meta:
# 		ordering = ('add_time',)
# 	def __unicode__(self):
# 		return self.image


# from django.db import models
# from mongoengine import *
#
#
# connect('test', host='localhost', port=27017)
# # connect(DBNAME)
#
# # Create your models here.
# class Questions(Document):
#
#     _id = IntField(primary_key=True)
#     url = URLField()
#     title = StringField()
#     content = StringField()
#     is_solved = BooleanField(default=0)
#     answer_count = IntField()
#     view_count = StringField()
#     vote_count = StringField()
#     tags = ListField()
#     answers = ListField()
#     source = StringField()
#
#     meta = {'collection': 'questions'}  # 指明连接数据库的哪张表
#
# for i in Questions.objects[:10]:  # 测试是否连接成功
#     print(i._id)

