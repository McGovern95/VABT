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
    path('', PostListView.as_view(), name='dashboard-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('home/', views.certifier_home, name='certifier-home'),
    path('about/', views.about, name='dashboard-about'),
    path('contact/', views.contact, name='dashboard-contact'),
    #path('checklist/', views.checklist, name='dashboard-checklist'), not sure how this'll be for file uploading and stuff
 

]
#<app>/<model>_<viewtype>.html