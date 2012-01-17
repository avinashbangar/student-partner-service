# Create your views here.
from ubuntuone.storageprotocol import request
from django.template import Template, Context, loader
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from models import Users, City, Request
from django.core.mail import EmailMessage
import datetime


def create(request):

    if request.method=='POST':
        name = request.POST['username']
        email = request.POST['email']
        sex = request.POST['sex']
        mobile_number = request.POST['mobile_number']
        exam_city = request.POST['exam_city']
        current_city = request.POST['current_city']
        exam_date = request.POST['exam_date']

        if exam_date == '' or name == '' or email == '' or mobile_number == '' :
            return render_to_response('share/create.html')
        else :
            new_obj = Users(name = name, email = email, sex = sex, mobile_number = mobile_number,exam_city_id = exam_city,exam_date = exam_date, current_city = current_city)
            new_obj.save()
            if "requested_to" in request.session:

                obj = Request(requester = new_obj.id,requested_to = request.session["requested_to"])
                obj.save()
                del request.session["requested_to"]
                return HttpResponseRedirect('/thanks/')
            return HttpResponseRedirect('/thankyou/')
    if "exam_city" in request.session:
        return render_to_response('share/create.html',{'exists':1,'exam_date':request.session["exam_date"]})

    return render_to_response('share/create.html',{'exists':0})


def profile(request,id):
    profile = Users.objects.get(id = id)
    return render_to_response('share/profile.html',{'profile':profile})


def search(request):
    return render_to_response('share/search.html')

def requests(request):
    allRequest = Request.objects.all()
    return render_to_response('share/requests.html',{'allRequests' : allRequest})

def results(request):

    if request.method=='POST':

        sex = request.POST['sex']
        exam_center = request.POST['exam_city']
        exam_date = request.POST['exam_date']

        if exam_date == '':
            return HttpResponseRedirect('/search/')
        else:
            request.session["exam_city"] = exam_center
            request.session["exam_date"] = exam_date
            request.session["gender"] = sex
            q = Users.objects.filter(sex = sex,exam_city = exam_center,exam_date = exam_date)
            if q.exists():
                exists = 1
            else:
                exists = 0
            return render_to_response('share/results.html',{'name':q,'exists':exists })
    return render_to_response('share/results.html',{'name':q,'exists':exists })

def message(request,id):
    #del request.session["requested_to"]
#    q = Users.objects.get(id = id)
#    cty = City.objects.get(id = q.exam_city_id)
#    exam_date = request.session["exam_date"]
    request.session["requested_to"] = id
    return HttpResponseRedirect('/sign-up/')
    #return render_to_response('share/message.html',{'exam_date' : exam_date})
    #__email__(q.name,q.email,q.exam_city.name)
    #return render_to_response('mail.html',{'name':q.name})

def __email__(name,email_id,city):
    t = loader.get_template('email.txt')
    c = Context({
        'name': name,
        'city': city
    })
    email = EmailMessage('Request to be partner',t.render(c),to=[email_id])
    email.send()

    return 

def thanks(request):
        return render_to_response('share/thanks.html')

def thankyou(request):
    ''' will thank user for submitting profile '''
    return render_to_response('share/thankyou.html')

#not to be considered
def checkFacebook(request):
    if request.method == 'POST':
        
        request.method['exam_date']
        request.method['sex']
        request.method['exam_city']
        
    else:
        
        request.method['name']
        request.method['email']
        request.method['mobile_number']
         
    return render_to_response('facebook.html',locals())


def mail(request):
    t = loader.get_template('email.txt')
    c = Context({ 
        'name': 'Mayur',
        'city': 'Mumbai'
    })
    email = EmailMessage('Request to be partner',t.render(c),to=['dmayur11@gmail.com'])
    email.send()

    return render_to_response('mail.html')


def about(request):
    return render_to_response('share/about.html')

def contact(request):
    return render_to_response('share/contact.html')

def login(request):

    return render_to_response('login.html')

#def token(request,access_token):

#    return render_to_response('access_token.html',{access_key : access_token})
