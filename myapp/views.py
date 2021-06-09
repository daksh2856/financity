from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from myapp.models import user
from myapp.models import contactus
from myapp.models import services
from myapp.models import blog
from myapp.models import review
from datetime import date


import matplotlib
from io import BytesIO
import io
import base64
from PIL import Image, ImageDraw
import PIL, PIL.Image
from io import StringIO
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib import pylab
from pylab import *

from PIL import Image, ImageDraw
import PIL, PIL.Image
from io import StringIO

import matplotlib
from io import BytesIO
import io
import base64




# Create your views here.

def blo(request):
    if not request.session.has_key('email'):
        return redirect('/login')

    if request.method=='POST':
        title= request.POST.get('title')
        image =  request.FILES.get('img')
        message=  request.POST.get('msg')
        print(title, message,image)
        reges=blog()

        reges.subject = title
        reges.image = image   
        reges.published_date = date.today()
        reges.description=message
        us = user.objects.get(email = request.session.get('email'))
        reges.user_id = us

        reges.save()

    bo = blog.objects.all()

    return render(request,'blog.html',{'blog':bo})

def blog1(request):
    if not request.session.has_key('email'):
        return redirect('/login')

    blogs = blog.objects.all().order_by('-id')

    return render(request,'blog1.html',{'blogs': blogs})


def blog2(request, id):
    if not request.session.has_key('email'):
        return redirect('/login')

    blg = blog.objects.get(id = id)
    return render(request,'blog2.html',{'blog':blg})

def base(request):
    return render(request,'base.html',{})

def changepassword(request):
    if not request.session.has_key('email'):
        return redirect('/login')
    
    if request.method=='POST':
        usr=user.objects.get(email=request.session['email'])
        opw=(request.POST.get('old'))
        npw=(request.POST.get('new'))
        cnpw=(request.POST.get('conpwd'))
        if(npw==cnpw):
            p=usr.password
            if(opw==p):
                usr.password=npw
                usr.save()
                res="1"
                return render(request, 'changepassword.html', {'res':res})
            else:
                
                res = "2"
                return render(request,'changepassword.html', {'res':res})
        else:
            res = "3"
            return render(request,'changepassword.html',{'res':res})
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

def dashboard(request):
    if not request.session.has_key('email'):
        return redirect('/login')

    return render(request,'dashboard.html',{})

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
    if us.dob:
        date_string = us.dob.strftime("%Y-%m-%d")  
        return render(request,'editprofile.html',{'user':us, 'dob':date_string})
    else:
        return render(request,'editprofile.html',{'user':us})

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

def index1(request):
    return render(request,'index1.html',{})


def help(request):
    if not request.session.has_key('email'):
        return redirect('/login')

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
            #confirm_password =request.POST.get('cpass')
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
                return redirect('/index1')
            else:
               return render(request,'login.html', {'res':2})
           


        #login form method
    return render(request,'login.html',{})

def main(request):
    return render(request,'main.html',{})

def minister(request):
    return render(request,'minister.html',{})

def profile(request):
    if not request.session.has_key('email'):
        return redirect('/login')

    if request.method == 'POST':
        print('here')
        img = request.FILES.get('img')
        print(img)
        email_id = request.session.get('email')
        us =  user.objects.get(email = email_id) 
        us.profile_image = img
        us.save()


    email_id = request.session.get('email')
    us =  user.objects.get(email = email_id) 
    return render(request,'profile.html',{'user':us})

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

def setting(request):
    if not request.session.has_key('email'):
        return redirect('/login')

    return render(request,'setting.html',{})

def successfullychanged(request):
    if not request.session.has_key('email'):
        return redirect('/login')

    return render(request,'successfullychanged.html',{})


def logout(request):
    request.session.clear()
    return redirect('/login')

def graphic(request):
    request.session.clear()
    return render(request,'graphic.html',{})

def nse(request):
    from nsetools import Nse
    nse = Nse()
    print (nse)

    #  NSE  Index List 
    s=nse.get_index_list()

    return render(request,'nse.html',{'s':s})

def nse1(request):
    
    from nsetools import Nse
    nse = Nse()
    print (nse)

    # Advances/ Declines 

    adv_dec = nse.get_advances_declines()
    print(adv_dec)
    l=[]
    for x in adv_dec:
        l.append(["INDICES ",x['indice'] ,' ADVANCES ', x['advances'],' declines ',x['declines']," UNCHANGED ", x['unchanged']])
        print("INDICES ",x['indice'] ,' ADVANCES ', x['advances'],' declines ',x['declines']," UNCHANGED ", x['unchanged'])


    return render(request,'nse1.html',{'l':l})

def nse2(request):
    from nsetools import Nse
    nse = Nse()
    print (nse)

    # NSE Top gainers 
    top_gainers = nse.get_top_gainers()
    print(top_gainers)

    df = pd.DataFrame(top_gainers)
    k=df.values.tolist()

    for x in k: 
        for x1 in x:
            print(x1, end="")
        print("")

    return render(request,'nse2.html',{'top_gainers':top_gainers})

def nse3(request):
    from nsetools import Nse
    nse = Nse()
    print (nse)

    top_losers = nse.get_top_losers()

    return render(request,'nse3.html',{'top_losers':top_losers})

def d1(request):
    if not request.session.has_key('email'):
        return redirect('/login')

    return render(request,'d1.html',{})

def d2(request):
    if not request.session.has_key('email'):
        return redirect('/login')

    return render(request,'d2.html',{})

def d3(request):
    if not request.session.has_key('email'):
        return redirect('/login')

    return render(request,'d3.html',{})

def d4(request):
    if not request.session.has_key('email'):
        return redirect('/login')

    return render(request,'d4.html',{})

def gdp1(request):
    if not request.session.has_key('email'):
        return redirect('/login')

    if request.method == 'POST':
        # imports 
        fig=plt.figure(figsize=(3, 5), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'

        #visualization
        df1=pd.read_csv('gdp.csv')
        df1=df1.fillna(0)
        x=request.POST.get('state')
        y=request.POST.get('state1')
        #x=input('Enter the country name :')
        #y=input('Enter the country name :')
        df4=df1[df1['Country Name'].isin([x,y])]
        df4=df4.set_index('Country Name')
        df4=df4.transpose()
        df4.iloc[3:,:].plot.line(title='GDP Growth of '+x+' and '+y)
        plt.axhline(0, color='k')

        #saving image
        buf =io.BytesIO()
        plt.margins(0.8)
        # Tweak spacing to prevent clipping of tick-labels
        plt.subplots_adjust(bottom=0.35)
        plt.savefig(buf, format='png')
    
        fig.savefig('abc.png')
        
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
        
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        #response = HttpResponse(buf.getvalue(), content_type='image/png')
        #return response
        return render(request, 'gdp1.html', {'graphic': graphic.decode('utf8')})

    else:

             return render(request,'gdp1.html',{})

def gdp2(request):
    if not request.session.has_key('email'):
        return redirect('/login')

    if request.method == 'POST':
    # imports 
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'

    #visualization
        df1=pd.read_csv('gdp.csv')
        df1=df1.fillna(0)
        x=request.POST.get('countt')
        y=request.POST.get('sy')
        z=request.POST.get('ly')
        #x=input('Enter the country name :')
        #y=input('Enter the starting year :')
        #z=input('Enter the ending year :')
        df4=df1[df1['Country Name']==x]
        df4=df4.set_index('Country Name')
        df4.loc[:,y:z].plot.bar(title='GDP Growth of '+x+' from '+y+' to '+z,rot=360)
        plt.axhline(0, color='k')

        #saving image
        buf =io.BytesIO()
        plt.margins(0.8)
        # Tweak spacing to prevent clipping of tick-labels
        plt.subplots_adjust(bottom=0.35)
        plt.savefig(buf, format='png')
    
        fig.savefig('abc.png')
        
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
        
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        #response = HttpResponse(buf.getvalue(), content_type='image/png')
        #return response
        return render(request, 'gdp2.html', {'graphic': graphic.decode('utf8')})

    else:
        return render(request,'gdp2.html',{})

def gdp3(request):
    if not request.session.has_key('email'):
        return redirect('/login')

    if request.method == 'POST':
    # imports 
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'

    #visualization
        df1=pd.read_csv('gdp.csv')
        df1=df1.fillna(0)
        x=request.POST.get('count1')
        y=request.POST.get('count2')
        z=request.POST.get('y')
        #x=input('Enter the country name :')
        #y=input('Enter the country name :')
        #z=input('Enter the year :')
        df4=df1[df1['Country Name'].isin([x,y])]
        df4=df4.set_index('Country Name')
        df4=df4.transpose()
        df4=df4.iloc[3:,:]
        df4.loc[z,:].plot.bar(title='GDP Growth of '+x+' and '+y+' in '+z , rot=360)
        plt.axhline(0, color='k')

        #saving image
        buf =io.BytesIO()
        plt.margins(0.8)
        # Tweak spacing to prevent clipping of tick-labels
        plt.subplots_adjust(bottom=0.35)
        plt.savefig(buf, format='png')
    
        fig.savefig('abc.png')
        
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
        
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        #response = HttpResponse(buf.getvalue(), content_type='image/png')
        #return response
        return render(request, 'gdp3.html', {'graphic': graphic.decode('utf8')})

    else:
        return render(request,'gdp3.html',{})
    

def gdp4(request):
    if not request.session.has_key('email'):
        return redirect('/login')

    if request.method == 'POST':
    # imports 
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'

    #visualization
        df5=pd.read_csv('gdp.csv')
        df5=df5.fillna(0)
        x=request.POST.get('c1')
        y=request.POST.get('c2')
        xx=request.POST.get('c3')
        yy=request.POST.get('c4')
        z=request.POST.get('y1')
        zz=request.POST.get('y2')

        #x=input('Enter the country name :')
        #y=input('Enter the country name :')
        #xx=input('Enter the country name :')
        #yy=input('Enter the country name :')
        #z=input('Enter the year :')
        #zz=input('Enter the year :')
        df5=df5[df5['Country Name'].isin([x,y,xx,yy])]
        df5=df5.set_index('Country Name')
        df5=df5.transpose()
        df5=df5.iloc[3:,:]
        ax=df5.loc[z:zz,:].plot.bar(title="Adjusted net savings, including particulate emission damage from "+z+" to "+zz,rot=360,grid=True,figsize=(10,5))
        plt.axhline(0, color='k')
        ax.set_xlabel('Years')
        ax.set_facecolor('bisque')

        #saving image
        buf =io.BytesIO()
        plt.margins(0.8)
        # Tweak spacing to prevent clipping of tick-labels
        plt.subplots_adjust(bottom=0.35)
        plt.savefig(buf, format='png')
    
        fig.savefig('abc.png')
        
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
        
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        #response = HttpResponse(buf.getvalue(), content_type='image/png')
        #return response
        return render(request, 'gdp4.html', {'graphic': graphic.decode('utf8')})

    else:
        return render(request,'gdp4.html',{})
    

def gdp5(request):
    if not request.session.has_key('email'):
        return redirect('/login')

    if request.method == 'POST':
    # imports 
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'

    #visualization
        df=pd.read_csv('gdp.csv')
        df=df.fillna(0)
        y=request.POST.get('y')
        #y=input('Enter the year :')
        df1=df.sort_values(y ,ascending=False)
        df1=df1.set_index('Country Name')
        df1=df1.iloc[0:10,:]
        ax=df1.loc[:,y].plot.bar(title="GDP Growth annual(%)"+y,grid=True,rot=45)
        ax.set_xlabel('GDP Growth annual(%)')
        plt.axhline(0, color='k')
        ax.set_facecolor('bisque')

        #saving image
        buf =io.BytesIO()
        plt.margins(0.8)
        # Tweak spacing to prevent clipping of tick-labels
        plt.subplots_adjust(bottom=0.35)
        plt.savefig(buf, format='png')
    
        fig.savefig('abc.png')
        
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
        
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        #response = HttpResponse(buf.getvalue(), content_type='image/png')
        #return response
        return render(request, 'gdp5.html', {'graphic': graphic.decode('utf8')})

    else:
        return render(request,'gdp5.html',{})

def gdp6(request):
    if not request.session.has_key('email'):
        return redirect('/login')

    if request.method == 'POST':
    # imports 
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'

    #visualization
        df=pd.read_csv('gdp.csv')
        df=df.fillna(0)
        y=request.POST.get('y')
        #y=input('Enter the year :')
        df1=df.sort_values(y ,ascending=True)
        df1=df1.set_index('Country Name')
        df1=df1.iloc[0:10,:]
        ax=df1.loc[:,y].plot.bar(title="GDP Growth annual(%)"+y,grid=True,rot=45)
        ax.set_xlabel('GDP Growth annual(%)')
        plt.axhline(0, color='k')
        ax.set_facecolor('bisque')

        #saving image
        buf =io.BytesIO()
        plt.margins(0.8)
        # Tweak spacing to prevent clipping of tick-labels
        plt.subplots_adjust(bottom=0.35)
        plt.savefig(buf, format='png')
    
        fig.savefig('abc.png')
        
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
        
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        #response = HttpResponse(buf.getvalue(), content_type='image/png')
        #return response
        return render(request, 'gdp6.html', {'graphic': graphic.decode('utf8')})

    else:
        return render(request,'gdp6.html',{})

def p1(request):
    if not request.session.has_key('email'):
        return redirect('/login')

    return render(request,'p1.html',{})
    