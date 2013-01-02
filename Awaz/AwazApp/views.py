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
from ajaxuploader.views import AjaxFileUploader
from django.middleware.csrf import get_token
import string
from xlwt import *
from settings import *
from xlwt import *
import sys
from struct import pack, unpack
import StringIO
from django.template.loader import render_to_string
import ho.pisa as pisa
import os
import tarfile
import subprocess
from subprocess import Popen,PIPE
import urllib2
def home(request):
	form = ImageUploadForm() 
	e1 = Zpicmodedict.objects.get(z_pk = 1)
	objectlist = Zpicmodedict.objects.filter(zparent_id = 0).order_by('zserial')
	'''
	if request.method == 'POST':
		form = ImageUploadForm(request.POST, request.FILES)
		if form.is_valid():			
			obj.zpicture = "custom_images/"+request.FILES['upload_file'].name
			obj.save()
			form.save()
			return HttpResponseRedirect('/home/')'''
	csrf_token = get_token(request)
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
	
def clearImage(request):
	if request.is_ajax():
		foobar = request.GET['zpk']
		obj = Zpicmodedict.objects.get(z_pk = str(foobar))
		obj.zpicture = None;
		obj.save()
		return HttpResponse("Success")
	return HttpResponseRedirect('/images/'+foobar)

def getSearch(request):
	if request.is_ajax():
		search_val = request.GET['search_value']
		try:
			search = Zimagedata.objects.filter(zkey_words__icontains = search_val)
			search_query = Zpicmodedict.objects.filter(Q(ztag_name__icontains = search_val) | Q(zpicture__icontains = search_val)).distinct()
		except:
			search = None
			search_query = None
		query1 = search
		json = serializers.serialize("json",query1)
		return HttpResponse(json)
		
@csrf_exempt
def upload_file(request):
	return render_to_response('import.html', context_instance = RequestContext(request))
	  

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
    	  #form = ImageUploadForm(data=request.POST, files=request.FILES)
    	  fd =request.FILES['fd']
    	  return HttpResponse(" ")
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
		zcolor = request.POST['zcolor']
		enable = request.POST['enable']
		audio_data = request.POST['audio_data']
		obj = Zpicmodedict.objects.get(z_pk = zpk)
		obj.ztag_name = zname
		obj.zcolor = zcolor
		obj.zis_enabled = enable
		obj.zaudio_data = audio_data
		obj.save()
		l = []
		l.append(obj)
		json = serializers.serialize("json",l)
		return HttpResponse(json)
		
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

def word(request):
	if request.is_ajax():
		search = request.GET['search']
		try:
			search_query = Zpicmodedict.objects.filter(ztag_name__icontains = search)
		except:
			search_query = None
		json = serializers.serialize("json",search_query)
		return HttpResponse(json)

def getParent(request):
	if request.is_ajax():
		x = request.GET['x']
		obj = Zpicmodedict.objects.filter(zidentifier = x)
		json = serializers.serialize("json",obj)
		return HttpResponse(json)
		
def start(request):
    csrf_token = get_token(request)
    return render_to_response('import.html',
        {'csrf_token': csrf_token}, context_instance = RequestContext(request))

import_uploader = AjaxFileUploader(UPLOAD_DIR = 'custom_images')
import_db = AjaxFileUploader(UPLOAD_DIR = 'Files')
def upload(request):
	if request.is_ajax():
		zpk = request.GET['zpk']
		name = request.GET['file_name']
		obj = Zpicmodedict.objects.get(z_pk = zpk)
		obj.zpicture = 'custom_images/'+name
		obj.save()
		img = Zimagedata()
		x = ""
		x = name[:-len(".png")]
     	img.zfile_name = x
     	img.zdirectory_path = 'custom_images'
     	for char in string.punctuation:
     		x = x.replace(char, ' ')
     	print x
     	img.zkey_words = x
     	img.save()
     	return HttpResponse(obj.zpicture)


     	
def xls(request):
	
    requirements=Zpicmodedict.objects.all()
    a=1
    foobar = "1"
    if foobar == "1":
        #print "hello"
        w=Workbook()
        ws = w.add_sheet('Items')
        cols=19
        #ws.write(0,0,'Event Name')
        for colx,heading in enumerate(('Z_PK','Z_ENT','Z_OPT','ZIS_ENABLED','ZIS_SENTENCE_BOX_ENABLED','ZSERIAL','ZVERSION','ZAUDIO_DATA','ZCATEGORY_OR_TEMPLATE','ZCOLOR','ZIDENTIFIER','ZPARENT_ID','ZPICTURE','ZTAG_NAME')*1):
            ws.write(0,colx,heading)
		
        rx=0
        for r in requirements:
            rx+=1
            ws.write(rx,0,r.z_pk)
            ws.write(rx,1,r.z_ent)
            ws.write(rx,2,r.z_opt)
            ws.write(rx,3,r.zis_enabled)
            ws.write(rx,4,r.zis_sentence_box_enabled)         
            ws.write(rx,5,r.zserial)
            ws.write(rx,6,r.zversion)
            ws.write(rx,7,r.zaudio_data)
            ws.write(rx,8,r.zcategory_or_template)
            ws.write(rx,9,r.zcolor)
            ws.write(rx,10,r.zidentifier)
            ws.write(rx,11,r.zparent_id)
            ws.write(rx,12,r.zpicture)
            ws.write(rx,13,r.ztag_name)	        
        fname = 'Avaz.xls'
        response = HttpResponse(mimetype="application/vnd.ms-excel")
        response['Content-Disposition'] = 'attachment; filename=%s' % fname
        w.save(response)
        return response

def printChildren(obj,htmls):
	children = Zpicmodedict.objects.filter(zparent_id = obj.zidentifier)
	htmls.write("<ol>")
	for c in children:
		x = str(c.zpicture)
		word = x[:3]
		if word == "ci_":
			y = os.path.join(os.path.dirname(__file__), 'Media/custom_images/')
		else: 
			y = os.path.join(os.path.dirname(__file__), 'Media/png/')
		z = y+x
		if os.path.exists(z):
			f = open(z,'r')
			try:
				f1 = f.read()
				a = os.path.join(os.path.dirname(__file__), 'Media/Download/Images/')
				x = x.replace('/','_')
				print x
				b = a+x 
				w = open(b,"w")
				try:
					w.write(f1)
				finally:
					w.close()
			finally:
				f.close()
				
		htmls.write("<li>"+c.ztag_name+"<img style = 'width:60px;' src = Images/"+x+"></li>")
		printChildren(c,htmls)
	htmls.write("</ol>")
        
def export(request):
	if request.is_ajax():
		name = os.path.join(os.path.dirname(__file__), 'Media/Download/view.html')
		htmls = open(name,"w")
		objs = Zpicmodedict.objects.filter(zparent_id = 0)
		htmls.write("<html>")
		htmls.write("<ol>")
		for obj in objs :
			x = str(obj.zpicture)
			word = x[:3]
			if word == "ci_":
				y = os.path.join(os.path.dirname(__file__), 'Media/custom_images/')
			else: 
				y = os.path.join(os.path.dirname(__file__), 'Media/png/')
			#y = os.path.join(os.path.dirname(__file__), 'Media/png/')
			z = y+x
		
			f = open(z,'r')
			try:
				f1 = f.read()
				a = os.path.join(os.path.dirname(__file__), 'Media/Download/Images/')
				x = x.replace('/','_')
				print x
				b = a+x 
				w = open(b,"w")
				try:
					w.write(f1)
				finally:
					w.close()
			finally:
				f.close()
			htmls.write("<li>"+obj.ztag_name+"<img style = 'width:60px;' src = Images/"+x+"></li>")
			printChildren(obj,htmls)		
			htmls.write("</ol>")
		htmls.write("</html>")		
		response = HttpResponse(htmls,mimetype="application/html")
		response['Content-Disposition'] = 'attachment; filename=idiot'
		return HttpResponse("Exported succesfully")
	
def download(request):
	dir1 = os.path.join(os.path.dirname(__file__),'Media','Download')
	response = HttpResponse(mimetype='application/x-gzip')
	response['Content-Disposition'] = 'attachment; filename=Html.tar.gz'
	tarred = tarfile.open(fileobj=response, mode='w:gz')
	tarred.add(dir1, arcname="TarName")
	tarred.close()
	return response    
	
def img(request):
	if request.is_ajax():
		img_url = request.GET['url']
		zpk = request.GET['zpk']
		obj =  Zpicmodedict.objects.get(z_pk = zpk)
		try:
			img = urllib2.urlopen(img_url)
		except:
			return HttpResponse("Invalid url !")
		a = os.path.join(os.path.dirname(__file__), 'Media/custom_images/')
		name = os.path.basename(img_url)
		fname  = "ci_"+name
		path  =  a+fname
		f = open(path,"w")
		f.write(img.read())
		f.close()
		obj.zpicture  = fname
		obj.save()
		return HttpResponse(obj.zpicture)
	img_url = "http://i59.photobucket.com/albums/g300/wizzer520/hello.png"
	img = urllib2.urlopen(img_url)
	name = os.path.basename(img_url)
	a = os.path.join(os.path.dirname(__file__), 'Media/custom_images/')
	path  =  a+fname
	f = open(path,"w")
	f.write(img.read())
	f.close()
	return HttpResponse("Done")
