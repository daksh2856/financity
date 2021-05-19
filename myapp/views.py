from django.shortcuts import render, redirect
from myapp.models import user
from myapp.models import contactus
from myapp.models import services
from myapp.models import blog
from myapp.models import review
from datetime import date

# Create your views here.

def blo(request):
    if not request.session.has_key('email'):
        return redirect('/login')

    if request.method=='POST':
        title= request.POST.get('title')
        # image =  request.POST.get('img')
        message=  request.POST.get('msg')
        print(title, message)
        reges=blog()

        reges.subject = title
        # reges.image = image   
        reges.published_date = date.today()
        reges.description=message
        us = user.objects.get(email = request.session.get('email'))
        reges.user_id = us

        reges.save()

    return render(request,'blog.html',{})

def blog1(request):
    return render(request,'blog1.html',{})

def blog2(request):
    return render(request,'blog2.html',{})

def base(request):
    return render(request,'base.html',{})

def changepassword(request):
    if not request.session.has_key('email'):
        return redirect('/login')
    
    if request.method=='POST':
        usr=user.objects.get(email=request.session['email'])
        opw=(request.POST.get('opw'))
        npw=(request.POST.get('npw'))
        cnpw=(request.POST.get('cnpw'))
        if(npw==cnpw):
            p=usr.password
            if(opw==p):
                usr.password=npw
                usr.save()
                res="1"
                return render(request, 'chngepw.html', {'res':res})
            else:
                
                res = "2"
                return render(request,'chngepw.html', {'res':res})
        else:
            res = "3"
            return render(request,'chngepw.html',{'res':res})
    return render(request,'changepassword.html',{})


def contact(request):

    if request.method=='POST':
        full_name = request.POST.get('fn')
        email = request.POST.get('em')
        subject = request.POST.get('sub')
        message= request.POST.get('msg')
        
        rege=contactus()
        rege.name =  full_name
        rege.email = email
        rege.subject=subject
        rege.message=message

        rege.save()

    return render(request,'contactus.html',{})

def editprofile(request):
    if not request.session.has_key('email'):
        return redirect('/login')

    if request.method=='POST':
        fname= request.POST.get('fn')
        lname= request.POST.get('ln')
        no = request.POST.get('cn')
        date = request.POST.get('dob')
        gender = request.POST.get('gender')
        city= request.POST.get('city')
        state= request.POST.get('state')
        address= request.POST.get('address')


        
        email_id = request.session.get('email')
        regest =  user.objects.get(email = email_id)  

      
        regest.fname =  fname
        regest.lname =  lname
        regest.phone =  no
        regest.dob = date

        if gender == "Male":
            regest.gender="M"
        elif gender == 'Female':
            regest.gender = "F"
        else:
            regest.gender = 'O'
                    
        regest.city=city
        regest.state =  state
        regest.address = address

        regest.save()

    email_id = request.session.get('email')
    us =  user.objects.get(email = email_id) 
    date_string = us.dob.strftime("%Y-%m-%d")  
    return render(request,'editprofile.html',{'user':us, 'dob':date_string})

def eservices(request):

    ser = services.objects.all()
    # students.objects.filter(name='rahul')

    return render(request,'eservices.html',{'services':ser })

def financeminister(request):
    return render(request,'financeminister.html',{})

def forgotpassword(request):
    return render(request,'forgotpassword.html',{})

def footer(request):
    return render(request,'footer.html',{})

def header(request):
    return render(request,'header.html',{})

def index(request):
    print('index')
    if not request.session.has_key('email'):
        return redirect('/login')

    else:
        email_id = request.session.get('email')

        us =  user.objects.get(email = email_id)   
        return render(request,'index.html',{'user':us}) 

    return render(request,'index.html',{})

def help(request):
    return render(request,'help.html',{})

def login(request):
    #first of all we have to check for whether request is Post request or mot
    # how we will check let c

    if (request.method == 'POST'):
        #now request method will be POST when we are submitting the form.
        #now we have to get data from the form 
        print("Hello here")
        typ=request.POST.get('type')
        print(typ)
        if typ=="2":
            first_name = request.POST.get('fn')
            last_name = request.POST.get('ln')
            email = request.POST.get('em')
            password = request.POST.get('pas')
            # confirm_password =request.POST.get('cpass')

            #in this same way we will get all the data
            #after getting all the data we have to save the data in the model.

            reg = user()
            reg.fname =  first_name
            reg.lname = last_name
            reg.email = email
            reg.password = password

            #thats ho we will save all the data in the model 
            # at the end we will save it by using save() method
            reg.save()
        elif typ=="1":

            email = request.POST.get('email')
            password = request.POST.get('password')
            print(email)
            print(password)
            if user.objects.filter(email=email,password=password).exists():
                print('here')
                us =user.objects.get(email=email, password = password)
                print(us.email)
                request.session['email'] = us.email
                return redirect('/index')
            else:
               return render(request,'login.html', {'res':2})
           


        #login form method

        



    return render(request,'login.html',{})

def main(request):
    return render(request,'main.html',{})

def minister(request):
    return render(request,'minister.html',{})

def profile(request):
    return render(request,'profile.html',{})

def reset(request):
    return render(request,'reset.html',{})

def review(request):
    if not request.session.has_key('email'):
        return redirect('/login')
    
    if request.method=='POST':
        title= request.POST.get('subject')
        message=request.POST.get('message')

        reges=review()

        reges.subject = title
        reges.message=message
        us = user.objects.get(email = request.session.get('email'))
        reges.user_id = us

        reges.save()

    
    return render(request,'review.html',{})

def stateminister(request):
    return render(request,'stateminister.html',{})

def successfullychanged(request):
    return render(request,'successfullychanged.html',{})


def logout(request):
    request.session.clear()
    return redirect('/login')