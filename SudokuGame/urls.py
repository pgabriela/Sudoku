from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.chooser, name='chooser'),
    url(r'^check/(?P<solPk>\d+)/$', views.checkAns, name='checkAns'),
    url(r'^(?P<level>\d)/$', views.theGame, name='theGame'),
]
