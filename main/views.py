from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from main.models import Cereal, manufacturer
from django.template import RequestContext
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from main.forms import CerealSearchForm, CerealCreateForm, CerealEditForm



# Create your views here.



def cerealedit(request, pk):
	request_context = RequestContext(request)
	context = {}
	cereal = Cereal.objects.get(pk=pk)
	context['cereal'] = cereal

	print request.POST

	form = CerealEditForm(request.POST or None, instance=cereal)
	print request.POST
	context['form'] = form

	if form.is_valid():
		form.save()
		return redirect('/search_cereals/')

	return render_to_response('cereal_edit.html', context, context_instance=request_context)





def cerealcreate(request):
	request_context = RequestContext(request)
	context = {}

	if request.method == 'POST':
		form = CerealCreateForm(request.POST)
		context['form'] = form

		if form.is_valid():
			form.save()
			return render_to_response('cerealcreate.html', context, context_instance=request_context)
		else:
			context['valid'] = form.errors
			return render_to_response('cerealcreate.html', context, context_instance=request_context)

	else:
		form = CerealCreateForm()
		context['form'] = form
		return render_to_response('cerealcreate.html', context, context_instance=request_context)

def cerealsearch(request):
	request_context = RequestContext(request)
	context = {}
	if request.method == 'POST':
		form = CerealSearchForm(request.POST)
		context['form'] = form

		if form.is_valid():
			name = form.cleaned_data['name']
			manufacturer = form.cleaned_data['manufacturer']

			context['cereal_list'] = Cereal.objects.filter(name__startswith=name)

			return render_to_response('searchresults.html',context , context_instance=request_context)
		else:
			context['valid'] = form.errors
			return render_to_response('search.html',context , context_instance=request_context)
	else:
		form = CerealSearchForm()
		context['form'] = form
		return render_to_response('search.html',context , context_instance=request_context)






def cereal_list(request):
	cereal_list = Cereal.objects.all()
	mylist = ['<html><Head><style> a { color : white ; background : black; } body { background : yellow; font-family: Georgia, Serif;} </style></Head><Body>']
	for cereal in cereal_list :
		mylist.append("<a href='/cereal_details/%s'> Go to | %s </a> <br>" % (cereal.name, cereal.name))

	mylist.append("</body>")
	return HttpResponse(mylist)

def cereal_details(request, name):
	cereal_detail = Cereal.objects.get(name=name)
	return HttpResponse(cereal_detail)

def manufacturerdetail(request, id):
	manu = manufacturer.objects.get(id=id)
	cereals = manu.cereal_set.all()
	string = ''
	for cereal in cereals:
		string += '%s <br>' % cereal.name

	return HttpResponse(string)

def manulist(request):
	manu = manufacturer.objects.all()
	mylist = []
	for item in manu:
		mylist.append("<a href='/manudetail/%s'> %s </a> <br>" % (item.id, item.manufacturer_name))
	return HttpResponse(mylist)

def search_cereal(request):
	my_var = request.GET.get('q',None)

	

	text_string = ""
	if my_var != None:

		text_string += "Searching for : %s <br>" % my_var
	
	text_string += """
	<form action='/search_cereals/' method='GET'>
	search cereal : <input type='text' name='q'><br>
	<input type='submit' value='search'><br>
	"""
	if my_var != None:
		my_cereal = Cereal.objects.filter(name__icontains=my_var)
		for item in my_cereal:
			text_string += '%s <br>' % item.name

	return HttpResponse(text_string)









