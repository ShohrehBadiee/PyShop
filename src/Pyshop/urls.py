from django.conf.urls import patterns, include, url
from django.contrib import admin
from product import urls as productUrls


urlpatterns = patterns('',

    # Examples:
    # url(r'^$', 'Pyshop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^product/',include(productUrls)),
    url(r'^admin/', include(admin.site.urls)),
)
