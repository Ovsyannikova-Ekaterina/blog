from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.home, name='home'),
    path('new_post/', views.new_post, name='new_post'),
    path('post_detals/<int:post_id>/', views.post_details, name='post_details'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('my_posts/', views.my_posts, name='my_posts'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),

]
