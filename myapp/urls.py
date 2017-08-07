from django.conf.urls import url
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # /myapp/
    url(r'^$', views.index, name='index'),
    # /myapp/id/
    url(r'^(?P<host_id>[0-9]+)/$', views.detail, name='detail'),
    #/myapp/host?=vpc-prod-vertex08-usw/
    url(r'^host_details$', views.host_details, name='host_details'),
    # /myapp/result
    #url(r'^results/$', views.results, name='result'),
    # /myapp/search
    url(r'^search/$', views.search, name='search'),
    #/myapp/relaod
    url(r'^reload/$', views.AutoUpload, name='AutoUpload'),
    #/myapp/Error_track  Log upload link
    url(r'^Error_track/$', views.Error_track, name='Error_track'),
    #/myapp/Log_track   Log Visualized link
    url(r'^Log_track/$', views.Log_track, name='Log_track'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)