from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'kitchencrashers.main.views.home', name='home'),
    url(r'^createEvent$', 'kitchencrashers.main.views.createEvent', name='createEvent'),
    url(r'^showEvent$', 'kitchencrashers.main.views.showEvent', name='showEvent')
)
