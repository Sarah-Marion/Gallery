from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.libs, name='home'),
    url(r'^lib/(?P<lib_title_slug>[\w\-]+)/', views.lib_detail, name='lib_detail'),
    url(r'^craft/(?P<craft_id>[0-9]+)/$', views.craft_detail, name='craft'),
    url(r'^about/$', views.about_me, name='aboutMe'),
    url(r'^location/',views.image_by_location,name='locationPhoto'),
]