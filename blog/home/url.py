from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^index', views.index, name = 'index'),
    url(r'^Saajan', views.hiSaajan, name = 'saajan'),
    url(r'^tracking_home', views.tracking_home, name='tracking_home'),
    url(r'^tracking', views.tracking, name='tracking'),
]
