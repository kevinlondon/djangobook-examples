from django.conf.urls import patterns, include, url
from mysite.views import hello, current_datetime, hours_ahead, display_meta
from django.contrib import admin
from contact import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^meta/$', display_meta),
#   url(r'^search/$', views.search),
    url(r'^contact/$', views.contact),
    
    # Uncomment the admin/doc line below to enable admin documentation:
      url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
      url(r'^admin/', include(admin.site.urls)),
)
