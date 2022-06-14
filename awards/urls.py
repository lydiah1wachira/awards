from . import views
from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views 

urlpatterns = [
  path('', views.index, name="index"),
  path('logout/', views.logout, {"next_page": '/'}),
  
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
