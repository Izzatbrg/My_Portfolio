from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog import views
app_name = 'blog'
urlpatterns = [
    path('', views.all_blogs, name="all_blogs"),
    path('<int:blog_id>',views.blog, name="blog"),

]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
