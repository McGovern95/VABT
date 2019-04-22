from django.urls import path, include
from django.conf.urls import url 
from django.conf import settings
from django.conf.urls.static import static
from .views import (
        PostListView,
        UserPostListView,
        PostDetailView
        )
from . import views

urlpatterns = [
    path('',views.home, name='dashboard-home'),
    path('certifier_home', PostListView.as_view(), name='certifier-home'),
    path('student/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('student_home/', views.student_home,name='student-home'),
    path('about/', views.about, name='dashboard-about'),
    path('contact/', views.contact, name='dashboard-contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#<app>/<model>_<viewtype>.html