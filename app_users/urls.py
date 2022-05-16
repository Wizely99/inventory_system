from django.urls import path
from app_users import views
urlpatterns=[
    # path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('add_patient/',views.AddPatient.as_view(),name='add_patient'),
    
]