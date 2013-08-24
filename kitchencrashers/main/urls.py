from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'kitchencrashers.main.views.home', name='home'),
    url(r'^search$', 'kitchencrashers.main.views.search', name='search'),
)
