from django.contrib import admin
from django.urls import path, include # เพิ่ม include ลิ้งค์ project กับ app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('mywebsite.urls')) # ลิ้งค์กับแอพและให้เข้าถึงไฟล์ urls.py ที่สร้างขึ้นมา
]
