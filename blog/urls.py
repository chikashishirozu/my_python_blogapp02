# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # 修正：post_List を post_list に変更
    # 他のURLパターン
]
