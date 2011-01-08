from django.http import HttpResponse, HttpResponseRedirect as redirect
from django.shortcuts import get_object_or_404, render_to_response as render
from django.core.urlresolvers import reverse
from drugs.models import *    
from iam.models import *

                    
def index(request):
	return render('index.html')
def api(request):
	return render('api.html')
	
def search(request):
	if request.method == 'POST': 
		search_text = request.POST['q']
		print "q %s" % search_text
		drugs = Drug.objects.filter(name__icontains=search_text)
		return render('drug_search.html', {'query':search_text, 'drugs' : drugs, 'forms' : [DrugForm(instance=drug) for drug in drugs]})   
	else:
		return render('index.html')            
		
def drug_detail(request, uid):
	drug = get_object_or_404(Drug, uid=uid)
	return render('drug_detail.html', {'drug':drug})       
	
	
def drug_interaction(request):
	if request.method == 'POST':
		uids = [drug.strip() for drug in request.POST['drugs'].split(',') if len(drug.strip()) != 0]
		print "got uids %s " % uids
		atcs = set()
		compositions = Composition.objects.filter(uid__in=uids)
		for comp in compositions:
			atcs.update([res.atc_id for res in LkMolAtc.objects.filter(molecule_code=comp.molecule_code)]) 
		print "got atcs %s " % str(atcs) 
		interactions = set()
		#its proper atc
		interactions.update(Interaction.objects.filter(atc_id1__in=atcs).filter(atc_id2__in=atcs))           
		print "inter 1 : %s " % str(interactions)
		# then its classes :
		classes = [classed.id_class for classed in Tree.objects.filter(id_atc__in=atcs)]
		interactions.update(Interaction.objects.filter(atc_id1__in=classes).filter(atc_id2__in=classes))   
		print "inter 2 : %s and classes %s " % (str(interactions), str(classes))
		out_inter = InteractionKnowledge.objects.filter(pk__in=[it.id for it in interactions])
		return render('interactions.html', {'interactions': out_inter, 'drugs' : Drug.objects.filter(uid__in=uids)})
	else:
		return render('drug_selection.html')
	
	