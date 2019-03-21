from django.urls import path
from .views import (
        PostListView,
        PostDetailView,
        PostCreateView,
        PostUpdateView,
        PostDeleteView,
        )
from . import views

urlpatterns = [
    path('',views.home, name='dashboard-home'),
    path('certifier_home', PostListView.as_view(), name='certifier-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('student_home/', views.student_home,name='student-home'),
    path('about/', views.about, name='dashboard-about'),
    path('contact/', views.contact, name='dashboard-contact'),
    
 

]
#<app>/<model>_<viewtype>.html