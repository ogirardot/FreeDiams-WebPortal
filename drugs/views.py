from django.http import HttpResponse, HttpResponseRedirect as redirect
from django.shortcuts import get_object_or_404, render_to_response as render
from django.core.urlresolvers import reverse
from drugs.models import *
                    
def index(request):
	return render('index.html')
	
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