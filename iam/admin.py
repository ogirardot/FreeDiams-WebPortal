from django.contrib import admin
from iam.models import *

admin.site.register(Atc)
admin.site.register(DbSchemaVersion)
admin.site.register(Tree)
admin.site.register(Interaction)
admin.site.register(InteractionKnowledge)
admin.site.register(Source)