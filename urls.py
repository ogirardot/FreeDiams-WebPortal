from django.conf.urls.defaults import *
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',        
    (r'^api/', include('FreeDiamsWebPortal.api.urls')),
    (r'^admin/', include(admin.site.urls)),
)                                             
# drug part :
urlpatterns += patterns('FreeDiamsWebPortal.drugs.views',
    (r'^interaction/?$', 'drug_interaction'),   
	(r'^drug/(?P<uid>[0-9]*)/?$', 'drug_detail'),
	(r'^search/?$', 'search'),
	(r'^drug/api?$', 'api'),    
	(r'^/?$', 'index'),
)


#local urls for serving media files during development
if settings.LOCAL_DEVELOPMENT:
    urlpatterns += patterns("django.views",
        url(r"%s(?P<path>.*)/$" % settings.MEDIA_URL[1:], "static.serve", {
            "document_root": settings.MEDIA_ROOT,
        })
    )
