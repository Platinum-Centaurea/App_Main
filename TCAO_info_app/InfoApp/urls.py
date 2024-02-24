from django.contrib import admin
from django.urls import path, include
# views:画面遷移が主, culc:ステータス・ダメージ計算など, dataope:データ操作用
from . import views, culc, dataope