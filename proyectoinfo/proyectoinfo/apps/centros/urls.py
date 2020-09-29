from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
  path('lugares/', views.Centers.as_view(), name='lugares'),
  path('<slug:pk>/detail_center/', views.CenterDetail.as_view(), name='detail_center'),
  path('<slug:pk>/delete_center/', views.CenterDelete.as_view(), name='delete_center'),
  path('<slug:pk>/update_center/', views.CenterUpdate.as_view(), name='update_center'),
  path('create_center/', views.CreateCenter.as_view(), name='create_center'),
]

