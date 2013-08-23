from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'kitchencrashers.main.views.home', name='home'),
)
