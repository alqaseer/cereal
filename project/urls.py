from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^cereal_list/$', 'main.views.cereal_list'),
    url(r'^cereal_details/(?P<name>.+)/$', 'main.views.cereal_details'),
    url(r'^manulist/$', 'main.views.manulist'),
    url(r'^manudetail/(?P<id>.+)/$', 'main.views.manufacturerdetail'),
    url(r'^search_cereals/$', 'main.views.search_cereal'),
    url(r'^cerealsearch/$', 'main.views.cerealsearch'),
    url(r'^cerealcreate/$', 'main.views.cerealcreate'),
    url(r'^cerealedit/(?P<pk>[0-9]+)/$', 'main.views.cerealedit'),
]
