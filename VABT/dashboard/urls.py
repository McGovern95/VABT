from django.urls import path
from .views import (
        PostListView,
        UserPostListView
        )
from . import views

urlpatterns = [
    path('',views.home, name='dashboard-home'),
    path('certifier_home', PostListView.as_view(), name='certifier-home'),
    path('student/<str:username>', UserPostListView.as_view(), name='user-posts'),

    path('student_home/', views.student_home,name='student-home'),
    path('about/', views.about, name='dashboard-about'),
    path('contact/', views.contact, name='dashboard-contact'),
    
 

]
#<app>/<model>_<viewtype>.html