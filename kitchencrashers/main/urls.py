from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from kitchencrashers import settings

urlpatterns = patterns('',
    url(r'^$', 'kitchencrashers.main.views.home', name='home'),
    url(r'^createEvent$', 'kitchencrashers.main.views.createEvent', name='createEvent'),
    url(r'^showEvent/(?P<eventID>\d+)$','kitchencrashers.main.views.showEvent', name='showEvent')
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)