# -*- coding: latin1 -*-

from django.db import models
    
class Atc(models.Model):
    id = models.IntegerField(null=True, primary_key=True, db_column=u'ID', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=7, db_column=u'CODE', blank=True) # Field name made lowercase.
    english = models.CharField(max_length=127, db_column=u'ENGLISH', blank=True) # Field name made lowercase.
    french = models.CharField(max_length=127, db_column=u'FRENCH', blank=True) # Field name made lowercase.
    deutsch = models.CharField(max_length=127, db_column=u'DEUTSCH', blank=True) # Field name made lowercase.

class DbSchemaVersion(models.Model):   
	id = models.IntegerField(null=True, primary_key=True, db_column=u'ID', blank=True) # Field name made lowercase.
	version = models.CharField(max_length=10, db_column=u'VERSION', blank=True) # Field name made lowercase.
	date = models.DateField(null=True, db_column=u'DATE', blank=True) # Field name made lowercase.
	comment = models.CharField(max_length=500, db_column=u'COMMENT', blank=True) # Field name made lowercase.

class Tree(models.Model):
    id_class = models.IntegerField(db_column=u'ID_CLASS') # Field name made lowercase.
    id_atc = models.IntegerField(db_column=u'ID_ATC') # Field name made lowercase.
    source_link = models.IntegerField(null=True, db_column=u'SOURCE_LINK', blank=True) # Field name made lowercase.

class Interaction(models.Model):
    id = models.IntegerField(null=True, primary_key=True, db_column=u'ID', blank=True) # Field name made lowercase.
    atc_id1 = models.IntegerField(db_column=u'ATC_ID1') # Field name made lowercase.
    atc_id2 = models.IntegerField(db_column=u'ATC_ID2') # Field name made lowercase.
    interaction_knowledge_id = models.IntegerField(null=True, db_column=u'INTERACTION_KNOWLEDGE_ID', blank=True) # Field name made lowercase.
    
INTERACTION_TYPE=dict({
	"I": "Information",
	"P": "Precaution d'utilisation",
	"T": "A prendre en compte",
	"D": "Déconseillé",
	"C": "Contre-indication"})
class InteractionKnowledge(models.Model):
    id = models.IntegerField(null=True, primary_key=True, db_column=u'ID', blank=True) # Field name made lowercase.
    type = models.CharField(max_length=10, db_column=u'TYPE') # Field name made lowercase.
    risk_fr = models.CharField(max_length=2000, db_column=u'RISK_FR') # Field name made lowercase.
    management_fr = models.CharField(max_length=2000, db_column=u'MANAGEMENT_FR', blank=True) # Field name made lowercase.
    risk_en = models.CharField(max_length=2000, db_column=u'RISK_EN') # Field name made lowercase.
    management_en = models.CharField(max_length=2000, db_column=u'MANAGEMENT_EN', blank=True) # Field name made lowercase.
    references_link = models.CharField(max_length=100, db_column=u'REFERENCES_LINK', blank=True) # Field name made lowercase.
    def getInteractionType(self):
		return INTERACTION_TYPE[self.type]
		

class Source(models.Model):
    id = models.IntegerField(null=True, primary_key=True, db_column=u'ID', blank=True) # Field name made lowercase.
    source_link = models.IntegerField(db_column=u'SOURCE_LINK') # Field name made lowercase.
    type = models.CharField(max_length=20, db_column=u'TYPE', blank=True) # Field name made lowercase.
    link = models.CharField(max_length=200, db_column=u'LINK', blank=True) # Field name made lowercase.
    textual_reference = models.CharField(max_length=1000, db_column=u'TEXTUAL_REFERENCE', blank=True) # Field name made lowercase.
    abstract = models.CharField(max_length=4000, db_column=u'ABSTRACT', blank=True) # Field name made lowercase.
    explanation = models.CharField(max_length=4000, db_column=u'EXPLANATION', blank=True) # Field name made lowercase.

