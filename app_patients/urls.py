from django.urls import path
from app_patients import views
urlpatterns=[
    path(r'view_profile/(?P<username>/$',views.view_profile,name='view_profile'),
    # path('',views.dashboard_handler,name='dashboard'),
]