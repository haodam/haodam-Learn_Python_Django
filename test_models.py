import email
from enum import Flag
import os
import django
from numpy import place
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myweb.settings")
django.setup()

from myapp.models import Python2104 , Restaurant , Place , Article , Reporter
# temp1 = Python2104(ten="Tung", tuoi = 5, diachi = "Phu Khe")
# temp1.save()
# temp1 = Python2104(ten="Hao", tuoi =25, diachi = "Phu Khe")
# temp1.save()
# temp2 = Python2104(ten="Huy", tuoi =8, diachi = "Phu Khe")
# temp2.save()
# temp4 = Python2104(ten="Lan Anh", tuoi = 18, diachi = "Phu Khe")
# temp4.save()
# temp3 = Python2104.objects.get(id = 1)
# # print(temp3.ten, temp3.id)
# temp3.delete()

# all_data = Python2104.objects.all()
# for i in all_data:
#     print(i.ten, i.tuoi)

# temp = Place(name = "Ba Dinh" , address = "Ha Noi")
# temp.save()

# rest1 = Restaurant(place_id = 1, serves_hot_dogs = True, serves_pizza = False)
# rest1.save()

# p1 = Place.objects.get(name ="Ba Dinh")
# print(p1)

#place viet thuong
# all_rest = Restaurant.objects.all()
# for rest in all_rest:
#     print(rest.place.name)

# Quan he 1 - 1 thong qua field: OneToOneField
# Truy cap vao cai doi tuong class lien ket thi truy cap qua thuoc tinh <ten class viet thuong>
# place 1 - 1 Restaurant
# Bien duoc khoi tao tu Place ten place, Truy cap qua Restaurant thi goi place.restaurant
# va nguoc lai

# Quan he mot - nhieu
# 1 Repoter se co nhieu Articles
# reporter = Reporter.objects.create(first_name = "Cristiano" ,last_name ="Ronaldo", email="Ronaldo@gmail.com")
# article = Article(headline ="Ronaldo ghi hat chich vao luoi doi tuyen Phap - Bo", pub_date = datetime.datetime.now(),
# reporter_id =1)
# article.save()

# Cach 1: truyen chinh xac ten duoc dinh nghia trong table
# reporter1 = Reporter.objects.get(pk =1) #pk la khoa chinh
# article1 = Article(headline ="Ronaldo ghi hat chich vao luoi doi tuyen Phap - Bo", pub_date = datetime.datetime.now(),
# reporter_id = reporter1.id)
# article1.save()

# Cach 2: Truyen ten voi cac ten duoc dinh nghia trong models
# reporter1 = Reporter.objects.get(pk =1) #pk la khoa chinh
# article3 = Article(headline ="Ronaldo ghi hat chich vao luoi doi tuyen Phap - Bo", pub_date = datetime.datetime.now(),
# reporter = reporter1)
# article3.save()

#Lay thong tin ra
# cach 1:
# reporter1 = Reporter.objects.get(pk =1) #pk la khoa chinh
# print(reporter1.first_name , reporter1.last_name)
# article = Article.objects.filter(reporter_id = reporter1.id)
# for item in article:
#     print(item.headline)

#Cach 2:
# reporter1 = Reporter.objects.get(pk =1) #pk la khoa chinh
# print(reporter1.first_name , reporter1.last_name)
# for item in reporter1.article_set.all():
#     print(item.headline)

# Quan he 1 - many
# 1 SoMot - n So SoNhieu
# 1 bien tu class SoMot ten la somot. Truy cap qua cac data lien quan toi no
# thong qua somot.conhieu_set.all()
# 1 bien tu class SoNhieu ten sonhieu. Truy cap qua data class kia
# thong qua sohieu.somot








