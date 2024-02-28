from django.contrib import admin
from django.urls import path

# views
from posts import views as posts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("category/<tag>/", posts_views.home_view, name="category"),
    path('',posts_views.home_view, name='home'),
    path('post/create/', posts_views.post_create_view, name='post-create'),
    path('post/delete/<pk>/', posts_views.post_delete_view, name='post-delete'),
    path("post/edit/<pk>/", posts_views.post_edit_view, name="post-edit"),
    path('post/<pk>/', posts_views.post_page_view, name='post'),
]
