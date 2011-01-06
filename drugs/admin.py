from django.contrib import admin
from drugs.models import *

admin.site.register(Drug)
admin.site.register(Composition)
admin.site.register(DbSchemaVersion)
admin.site.register(DrugRoute)
admin.site.register(Information)
admin.site.register(LkMolAtc)
admin.site.register(Packaging)
admin.site.register(Route)
admin.site.register(RouteAbbrev)
admin.site.register(RouteSynonym)
admin.site.register(SearchEngine)
