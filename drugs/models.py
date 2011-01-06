# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models  
from django import forms

class Composition(models.Model):
    uid = models.CharField(max_length=60, db_column='UID') # Field name made lowercase.
    molecule_form = models.CharField(max_length=300, db_column='MOLECULE_FORM', blank=True) # Field name made lowercase.
    molecule_code = models.IntegerField(db_column='MOLECULE_CODE') # Field name made lowercase.
    molecule_name = models.CharField(max_length=600, db_column='MOLECULE_NAME') # Field name made lowercase.
    molecule_atc = models.CharField(max_length=21, db_column='MOLECULE_ATC', blank=True) # Field name made lowercase.
    dosage = models.CharField(max_length=300, db_column='DOSAGE', null=True, blank=True) # Field name made lowercase.
    dosage_ref = models.CharField(max_length=150, db_column='DOSAGE_REF', null=True, blank=True) # Field name made lowercase.
    nature = models.CharField(max_length=6, db_column='NATURE') # Field name made lowercase.
    lk_nature = models.IntegerField(db_column='LK_NATURE') # Field name made lowercase.
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.

class DbSchemaVersion(models.Model):
    version = models.CharField(max_length=30, db_column='VERSION', blank=True) # Field name made lowercase.
    date = models.DateField(null=True, db_column='DATE', blank=True) # Field name made lowercase.
    comment = models.CharField(max_length=1500, db_column='COMMENT', blank=True) # Field name made lowercase.
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.

class Drug(models.Model):
    uid = models.CharField(primary_key=True, max_length=60, db_column='UID') # Field name made lowercase.
    name = models.CharField(max_length=3000, db_column='NAME') # Field name made lowercase.
    form = models.CharField(max_length=1500, db_column='FORM', blank=True) # Field name made lowercase.
    route = models.CharField(max_length=300, db_column='ROUTE', blank=True) # Field name made lowercase.
    atc = models.CharField(max_length=21, db_column='ATC', null=True, blank=True) # Field name made lowercase.
    global_strength = models.CharField(max_length=120, db_column='GLOBAL_STRENGTH', null=True,  blank=True) # Field name made lowercase.
    type_mp = models.CharField(max_length=3, db_column='TYPE_MP', blank=True) # Field name made lowercase.
    authorization = models.CharField(max_length=3, db_column='AUTHORIZATION', blank=True) # Field name made lowercase.
    marketed = models.IntegerField(db_column='MARKETED') # Field name made lowercase.
    link_spc = models.CharField(max_length=750, db_column='LINK_SPC', null=True, blank=True) # Field name made lowercase.
             
class DrugForm(forms.ModelForm):
	class Meta:
		model = Drug
		
class DrugRoute(models.Model):
    drug_uid = models.CharField(max_length=60, db_column='DRUG_UID') # Field name made lowercase.
    route_id = models.IntegerField(db_column='ROUTE_ID') # Field name made lowercase.
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.

class Information(models.Model):
    version = models.CharField(max_length=30, db_column='VERSION') # Field name made lowercase.
    name = models.CharField(max_length=6000, db_column='NAME', null=True, blank=True) # Field name made lowercase.
    identifiant = models.CharField(max_length=150, db_column='IDENTIFIANT', blank=True) # Field name made lowercase.
    compat_version = models.CharField(max_length=30, db_column='COMPAT_VERSION', blank=True) # Field name made lowercase.
    provider = models.CharField(max_length=600, db_column='PROVIDER', blank=True) # Field name made lowercase.
    weblink = models.CharField(max_length=1500, db_column='WEBLINK', blank=True) # Field name made lowercase.
    complementary_website = models.CharField(max_length=600, db_column='COMPLEMENTARY_WEBSITE', blank=True) # Field name made lowercase.
    author = models.CharField(max_length=600, db_column='AUTHOR', blank=True) # Field name made lowercase.
    license = models.TextField(db_column='LICENSE', blank=True) # Field name made lowercase.
    license_terms = models.TextField(db_column='LICENSE_TERMS', blank=True) # Field name made lowercase.
    date = models.CharField(max_length=60, db_column='DATE', blank=True) # Field name made lowercase.
    drug_uid_name = models.CharField(max_length=150, db_column='DRUG_UID_NAME', blank=True) # Field name made lowercase.
    pack_main_code_name = models.CharField(max_length=150, db_column='PACK_MAIN_CODE_NAME', blank=True) # Field name made lowercase.
    atc = models.IntegerField(db_column='ATC') # Field name made lowercase.
    interactions = models.IntegerField(db_column='INTERACTIONS') # Field name made lowercase.
    mol_link_completion = models.IntegerField(null=True, db_column='MOL_LINK_COMPLETION', blank=True) # Field name made lowercase.
    author_comments = models.TextField(db_column='AUTHOR_COMMENTS', blank=True) # Field name made lowercase.
    language_country = models.CharField(max_length=15, db_column='LANGUAGE_COUNTRY', blank=True) # Field name made lowercase.
    drugs_name_constructor = models.CharField(max_length=600, db_column='DRUGS_NAME_CONSTRUCTOR', blank=True) # Field name made lowercase.
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.

class LkMolAtc(models.Model):
    molecule_code = models.IntegerField(db_column='MOLECULE_CODE') # Field name made lowercase.
    atc_id = models.IntegerField(db_column='ATC_ID') # Field name made lowercase.
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.

class Packaging(models.Model):
    uid = models.CharField(max_length=60, db_column='UID') # Field name made lowercase.
    package_uid = models.IntegerField(db_column='PACKAGE_UID') # Field name made lowercase.
    label = models.CharField(max_length=1500, db_column='LABEL') # Field name made lowercase.
    status = models.CharField(max_length=3, db_column='STATUS', blank=True) # Field name made lowercase.
    marketing = models.IntegerField(db_column='MARKETING') # Field name made lowercase.
    date = models.CharField(max_length=75, db_column='DATE', blank=True) # Field name made lowercase.
    optional_code = models.IntegerField(null=True, db_column='OPTIONAL_CODE', blank=True) # Field name made lowercase.
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'drugs_packaging'

class Route(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    fr = models.CharField(max_length=150, db_column='FR', blank=True) # Field name made lowercase.
    en = models.CharField(max_length=150, db_column='EN', blank=True) # Field name made lowercase.
    de = models.CharField(max_length=150, db_column='DE', blank=True) # Field name made lowercase.

class RouteAbbrev(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    route_id = models.IntegerField(null=True, db_column='ROUTE_ID', blank=True) # Field name made lowercase.
    lang = models.CharField(max_length=150, db_column='LANG', blank=True) # Field name made lowercase.
    abbrev = models.CharField(max_length=150, db_column='ABBREV', blank=True) # Field name made lowercase.

class RouteSynonym(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    route_id = models.IntegerField(null=True, db_column='ROUTE_ID', blank=True) # Field name made lowercase.
    lang = models.CharField(max_length=150, db_column='LANG', blank=True) # Field name made lowercase.
    synonym = models.CharField(max_length=150, db_column='SYNONYM', blank=True) # Field name made lowercase.

class SearchEngine(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    label = models.CharField(max_length=75, db_column='LABEL', blank=True) # Field name made lowercase.
    url = models.CharField(max_length=3000, db_column='URL', blank=True) # Field name made lowercase.

