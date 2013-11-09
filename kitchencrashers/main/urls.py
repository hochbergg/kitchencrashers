from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from kitchencrashers import settings

urlpatterns = patterns('',
    url(r'^$', 'kitchencrashers.main.views.home', name='home'),
    url(r'^accounts/login.*$', 'kitchencrashers.main.views.login', name='login'),
    url(r'^search$', 'kitchencrashers.main.views.search', name='search'),
    url(r'^createEvent$', 'kitchencrashers.main.views.createEvent', name='createEvent'),
    url(r'^showEvent/(?P<eventID>\d+)$','kitchencrashers.main.views.showEvent', name='showEvent'),
    url(r'^MyEvents', 'kitchencrashers.main.views.MyEvents', name='MyEvents')
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
