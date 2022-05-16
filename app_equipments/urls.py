from django.urls import path
from app_equipments import views
urlpatterns=[
    path('add_equipment',views.add_equipment_handler,name='add_equipment'),
    path('',views.dashboard_handler,name='dashboard'),
]