from piston.handler import BaseHandler
from drugs.models import Drug

class DrugHandler(BaseHandler):
   allowed_methods = ('GET', 'POST') 
   fields = ('name', 'uid')
   model = Drug   

   def read(self, request, query=None):
	print "in"
	limit = 50
	if not query:
		if 'q' in request.GET:
			query=request.GET['q']
			if 'limit' in request.GET:
				limit = request.GET['limit']
		elif 'q' in request.POST:
			query=request.POST['q']
			if 'limit' in request.POST:
				limit = request.POST['limit']
	if query:
		return Drug.objects.filter(name__icontains=query)[:limit]
	else: 
		return [] 
    
	def update(self, request, query=None):
		return self.read(request, query)
