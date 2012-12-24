from django.views.generic.list_detail import object_list
from django.shortcuts import *
from forms import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from models import *
import simplejson
from django.core.serializers import serialize
from django.core import serializers
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
import sha, random
def home(request):
	form = ImageUploadForm() 
	e1 = Zpicmodedict.objects.get(z_pk = 1)
	objectlist = Zpicmodedict.objects.filter(zparent_id = 0).order_by('zserial')
	if request.method == 'POST':
		form = ImageUploadForm(request.POST, request.FILES)
		if form.is_valid():
			
			obj.zpicture = "custom_images/"+request.FILES['upload_file'].name
			obj.save()
			form.save()
			return HttpResponseRedirect('/home/')
	return render_to_response('Home.html', locals(), context_instance = RequestContext(request))

def getChildren(request,foobar):
	if request.is_ajax():
		objs = None
		obj = Zpicmodedict.objects.get(z_pk = foobar)
		try:
			objs = list(Zpicmodedict.objects.filter(zparent_id = obj.zidentifier).order_by('zserial'))
		except Zpicmodedict.DoesNotExist:
			objs = None
		l = []
		json = serializers.serialize("json",objs)				
		json1 = simplejson.dumps(json)
    	return HttpResponse(json1, mimetype='application/json')
    	
	try:
		obj = Zpicmodedict.objects.get(z_pk = foobar)
	except Zpicmodedict.DoesNotExist:
		obj = None
	try:
		objs = Zpicmodedict.objects.filter(zparent_id = obj.zidentifier)
	except Zpicmodedict.DoesNotExist:
		objs = None
	return render_to_response('Children.html', locals(), context_instance = RequestContext(request))

def images(request):
	form = ImageUploadForm() 
	print form
	if request.method == 'POST':
		foobar = str(request.POST['foobar'])
		obj = Zpicmodedict.objects.get(z_pk = foobar)
		form = ImageUploadForm(request.POST, request.FILES)
		if form.is_valid():
			obj.zpicture = "custom_images/"+request.FILES['upload_file'].name
	    	obj.save()
	    	#return HttpResponse(obj.zpicture)
	    	form.save()
	    	return HttpResponseRedirect('/home/')
	context = {
        'form' : form,
        'obj'  : obj,
	}   
	return render_to_response('imageScroller.html', context, context_instance = RequestContext(request)) 
	
def removeImg(request,foobar):
	obj = Zpicmodedict.objects.get(z_pk = str(foobar))
	obj.zpicture = None;
	obj.save()
	return HttpResponseRedirect('/images/'+foobar)

def getSearch(request):
	if request.is_ajax():
		search_val = request.GET['search_value']
		try:
			search_query = Zpicmodedict.objects.filter(Q(ztag_name__icontains = search_val) | Q(zpicture__icontains = search_val)).distinct()
		except:
			search_query = None
		query1 = search_query
		json = serializers.serialize("json",query1)
		return HttpResponse(json)

def upload_file(request):
	if request.is_ajax():
		return HttpResponse("Hi")   

def searchupdate(request):
	if request.is_ajax():
		data = request.GET['x']
		pk = str(request.GET['foobar'])
		obj = Zpicmodedict.objects.get(z_pk = pk)
		obj.zpicture = data.replace("http://localhost:8000/media/png/","")
		obj.save()
		return HttpResponse(obj.zpicture)
		
@csrf_exempt        
def test(request):
    if request.is_ajax():
        form = ImageUploadForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Saved !")
        return HttpResponse("Not Saved !!!!")
    return HttpResponse("Hi")            
                        
@csrf_exempt
def editsave(request):
	if request.is_ajax():
		zpk = str(request.POST['zpk'])
		zname = request.POST['zname']
		obj = Zpicmodedict.objects.get(z_pk = zpk)
		obj.ztag_name = zname
		obj.save()
		return HttpResponse(obj.zcategory_or_template)
		
@csrf_exempt		
def create(request):
	if request.is_ajax():
		data = request.POST['select']
		zparentid = request.POST['parentid']
		parent = Zpicmodedict.objects.get(z_pk = zparentid)
		obj = Zpicmodedict()
		obj.ztag_name = "untitled"
		obj.zpicture = "descriptives/how.png"
		if data == 'category':
			obj.zcategory_or_template  =  "D"
		else:
			obj.zcategory_or_template  =  "T"
		x = parent.zserial
		last = Zpicmodedict.objects.latest("z_pk")
		y = last.z_pk
		#return HttpResponse(y)
		obj.z_pk = y+1
		obj.zserial = x+1
		'''
		objects = Zpicmodedict.objects.filter(zserial__gte  = x)
		
		for obj in objects:			
			obj.zserial = obj.zserial + 1

			print obj.zserial
		for obj in objects:	
			obj.save()
		return HttpResponse("")	
		obj.zserial = x+1
		obj.z_pk = y+1'''
		if parent.zcategory_or_template == "D":
			obj.zparent_id = parent.zidentifier
		else:
			obj.zparent_id = parent.zparent_id
		salt = sha.new(str(random.random())).hexdigest()[:5]
		obj.zidentifier = sha.new(salt).hexdigest()
		obj.save()
		l = []
		l.append(obj)
		l.append(parent)		
		json = serializers.serialize("json",l)
		return HttpResponse(json)
	else:		
		zparentid = 5
		parent = Zpicmodedict.objects.get(z_pk = zparentid)
		json = serializers.serialize("json",[parent])
		last = Zpicmodedict.objects.latest('z_pk')		
		return HttpResponse(last.z_pk)
		
def audio(request):
	return render_to_response('Audio.html', locals(), context_instance = RequestContext(request))
