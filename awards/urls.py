from . import views
from django.urls import path,re_path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
  path('', views.index, name="index"),
  path('signup/', views.signup, name='signup'),
  path('post/', views.post, name='post' ),
  path(r'user/profile/',views.profile,name='profile'),

  
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
