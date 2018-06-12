from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from .import views

urlpatterns = [
    url(r'^$', views.libs, name='home'),
    url(r'^$', views.all_images, name='allPhoto'),
    url(r'^lib/(?P<lib_title_slug>[\w\-]+)/', views.lib_detail, name='lib_detail'),
    url(r'^craft/(?P<craft_id>[0-9]+)/$', views.craft_detail, name='craft'),
    url(r'^about/$', views.about_me, name='aboutMe'),
    url(r'^location/(?P<location>\w+)/',views.image_by_location,name='locationPhoto'),
    url(r'^category/(?P<category>\w+)/',views.image_by_category,name='categoryPhoto'),
    url(r'^image/(?P<image_id>\d+)/$',views.display_details,name='photoDetails'),
    url(r'^search/',views.search_image,name='searchPhoto'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
