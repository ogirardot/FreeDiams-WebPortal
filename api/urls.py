from django.conf.urls.defaults import *
from piston.resource import Resource
from FreeDiamsWebPortal.api.handlers import DrugHandler

drug_handler = Resource(DrugHandler)

urlpatterns = patterns('',
   url(r'drugs.(?P<emitter_format>[a-z]*)/(?P<query>[^/\?]+)/?$', drug_handler),  
   url(r'drugs.(?P<emitter_format>[a-z]*)', drug_handler), 
)
