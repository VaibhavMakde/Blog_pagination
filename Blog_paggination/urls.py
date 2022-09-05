
from django.contrib import admin
from django.urls import path
from blog import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.PostListView.as_view(),name='blog_list'),
    path('detail/<int:pk>', views.PostDetailView.as_view(),name='detail'),
]
