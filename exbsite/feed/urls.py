from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:myid>/', views.echo, name='echo'),
    path('listFeed/', views.listFeed, name='listFeed'),
    path('postForm/', views.postForm, name='postForm'),
    path('thanks/', views.thanks, name='thanks'),
    path('pic/', views.pic, name = 'pic'), 
    path('success/', views.success, name = 'success'),
    path('display_image/', views.display_image, name = 'display_image'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)