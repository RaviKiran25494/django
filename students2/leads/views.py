# from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, render_to_response
from.models import Registers,Joinings,Course_names
from .forms import RegistrationForm


# Create your views here.


# def index(request):
# 	return HttpResponse('<h1>this is Leads app</h1>')
#2 def index(request):
# 	all_registers=Registers.objects.all()
# 	html = ''
# 	for registers in all_registers:
# 		url='/leads/'+str(registers.id)+ '/'
# 		html+='<a href="'+url+'">'+registers.st_name+'</a><br>'
# 	return HttpResponse(html)
def index11(request):
	all_registers=Registers.objects.all()
	template=loader.get_template('leads/index.html')
	context={
	'all_registers':all_registers,
	}
	return render(request,'leads/index.html',context)
	# return HttpResponse(template.render(context,request))



#1 def detail(request,register_id):
# 	return HttpResponse('<h2>Details for album_id:'+ str(register_id) +'</h2>')

def detail(request,register_id):
	try:
		registers = Registers.objects.get(pk=register_id)
	except Registers.DoesNotExist:
		raise Http404("please Register .................")
	return render(request,'leads/detail.html',{'registers':registers})

def registers(request):
	form_class=RegistrationForm
	form = form_class(request.POST or None)
	print ("hi")
	if request.method =="POST":
		print ("hi")
		if form.is_valid():
			name = request.POST.get('name')
			mobile = request.POST.get('mobile')
			email = request.POST.get('email')
			course = request.POST.get('course')
			sourse = request.POST.get('sourse')
			lead_status = request.POST.get("lead_status")
			demo_date = request.POST.get("demo_date")
			counsler = request.POST.get("counsler")
			remarks = request.POST.get("remarks")
			print ('hi')
			context={'name':name,'mobile':mobile,'course':course}
			return render(request,'leads/demo1.html',context)
			print ('hi')
	return render(request, "leads/registers.html",{'form':form})

def joinings(request):
	template=loader.get_template('leads/joinings.html')
	return render(request,'leads/joinings.html')

def walkins(request):
	all_registers=Registers.objects.all()
	template=loader.get_template('leads/walkins.html')
	context={
	'all_registers':all_registers,
	}
	return render(request,'leads/walkins.html',context)
def currents(request):
	all_joinings=Joinings.objects.all()
	template=loader.get_template('leads/current.html')
	context={
	'all_joinings':all_joinings,
	}
	return render(request,'leads/current.html',context)
def callings(request):
	template=loader.get_template('leads/callings.html')
	return render(request,'leads/callings.html')

def counselling(request):
	all_courses=Course_names.objects.all()
	template=loader.get_template('leads/counselling.html')
	context={
	'all_courses':all_courses,
	}
	return render(request,'leads/counselling.html',context)



# def index1(request):
#     form_class=RegistrationForm
#     form = form_class(request.POST or None)
#     print ("hi")
#     if request.method =="POST":
#         print ("hi")
#         if form.is_valid():
#             name = request.POST.get('name')
#             mobile = request.POST.get('mobile')
#             email = request.POST.get('email')
#             course = request.POST.get('course')
#             sourse = request.POST.get('sourse')
#             lead_status = request.POST.get("lead_status")
#             demo_date = request.POST.get("demo_date")
#             counsler = request.POST.get("counsler")
#             remarks = request.POST.get("remarks")
#             print ('hi')
#             context={'name':name,'mobile':mobile,'course':course}

#             return render(request,'leads/demo1.html',context)
#             print ('hi')

#     return render(request, "leads/demo.html",{'form':form})

# def index2(request):
# 	if form.is_valid():
# 		name = request.POST.get('name')
# 		mobile = request.POST.get('mobile')
# 		email = request.POST.get('email')
# 		course = request.POST.get('course')
# 		sourse = request.POST.get('sourse')
# 		lead_status = request.POST.get("lead_status")
# 		demo_date = request.POST.get("demo_date")
# 		counsler = request.POST.get("counsler")
# 		remarks = request.POST.get("remarks")
# 		print ('mobile')
# 		a=Registers(st_name=name,st_mobile=mobile,st_email=email,st_course=course,st_sourse=sourse,st_lead_status=lead_status,st_demo_date=demo_date,st_counsler=counsler,st_remarks=remarks)
# 		a.save()

# 		context={'name':name,'mobile':mobile,'course':course}
# 		return render(request,'leads/demo1.html',context)
# 		print ('hi')
# 	template=loader.get_template('leads/demo1.html')
# 	return render(request,'leads/demo1.html')

#------------------------create -joinings ------------------------------
def index(request):
    register = Registers.objects.all()
    context = {'register': register}
    return render(request, 'leads/index11.html', context)

def create(request):
    registers = Registers(st_name=request.POST['name'],st_mobile=request.POST['mobile'],st_email=request.POST['email'],st_course=request.POST['course'],st_sourse=request.POST['source'],st_lead_status=request.POST['demo_call'],st_demo_date=request.POST['demo_date'],st_counsler=request.POST['counsler'],st_remarks=request.POST['remarks'])
    registers.save()
    return redirect('/leads')

def create1(request):
    joinings = Joinings(course=request.POST['course'],name=request.POST['name'],complection_date=request.POST['date_of_complected'],date_join=request.POST['date_of_joining'],course_fee=request.POST['course_fee'],instructor=request.POST['instructor'],aadhar_number=request.POST['aadhar_number'],mobile=request.POST['mobile'],email= request.POST['email'],remarks=request.POST['remarks'])
    joinings.save()
    return redirect('/current/curr1')

def edit(request, id):
    joining = Joinings.objects.get(id=id)
    context = {'joining': joining}
    return render(request, 'leads/edit.html', context)

def update(request, id):
    joining = Joinings.objects.get(id=id)
    joining.name = request.POST['name']
    joining.complection_date = request.POST['complection_date']
    joining.save()
    return redirect('/current/curr1/')

def complect(request, id):
    joining = Joinings.objects.get(id=id)
    joining.Status = "complected"
    joining.save()
    return redirect('/current/curr1/')

def delete(request, id):
    joining = Joinings.objects.get(id=id)
    joining.Status = "Discontinue"
    joining.save()
    return redirect('/current/curr1/')
#------------------------------curd - registers ---------------
def callings1(request):
	all_registers=Registers.objects.all()
	demo_call = request.POST['demo_call']
	demo_date = request.POST['demo_date']
	print(demo_date)
	context={
	'demo_call':demo_call,
	'demo_date':demo_date,
	'all_registers':all_registers,
	}
	return render(request, 'leads/walkins1.html', context)

def counselling1(request):
	all_registers=Registers.objects.all()
	demo_date = request.POST['demo_date']
	course = request.POST['course']
	print(demo_date)
	context={
	'course':course,
	'demo_date':demo_date,
	'all_registers':all_registers,
	}
	return render(request, 'leads/counselling1.html', context)

def edit1(request, id):
    register = Registers.objects.get(id=id)
    context = {'register': register}
    return render(request, 'leads/willin.html', context)

def update1(request, id):
    register = Registers.objects.get(id=id)
    register.st_name = request.POST['name']
    register.st_demo_date = request.POST['willing_date']
    register.save()
    return redirect('/walk/walk1/')

def delete1(request, id):
    register = Registers.objects.get(id=id)
    register.delete()
    return redirect('/leads/')


def students(request):
	joinings = Joinings.objects.all()
	context = {
	'joinings': joinings,

	}
	template=loader.get_template('leads/students.html')
	return render(request,'leads/students.html',context)

#---------------------------------------------------------------
