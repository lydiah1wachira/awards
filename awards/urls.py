from . import views
from django.urls import path,re_path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
  path('', views.index, name="index"),
  path('signup/', views.signup, name='signup'),
  path('post/', views.post, name='post' ),
  path('profile/',views.profile,name='profile'),
  re_path('project/(\d+)/',views.detailed_project,name='details'),
  path('search/projects/results/',views.search,name="search"),
  path('api/projects/',views.ProjectList.as_view()),
  path('accounts/', include('django.contrib.auth.urls')),

  
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
