from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

#user add
import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',views.index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$',views.index),
)
