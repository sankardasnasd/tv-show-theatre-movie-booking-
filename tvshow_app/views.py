import datetime

from django.core.files.storage import FileSystemStorage
from django.db.models import Avg
from django.http import JsonResponse
from django.shortcuts import render,HttpResponse

from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
from tvshow_app.models import *


def index(request):
    return HttpResponse('success')


# email exists json
def email_exist(request):
    email_ex = request.POST['email']
    if User.objects.filter(email=email_ex).exists():
        return JsonResponse({'status':'ok'})
    else:
        return JsonResponse({'status':'no'})

def forget_password(request):
    return render(request,'user/forget_password.html')

def forget_password_post(request):
    em = request.POST['em_add']
    import random
    password = random.randint(00000000, 99999999)
    log = Login.objects.filter(username=em)
    if log.exists():
        logg = Login.objects.get(username=em)
        message = 'temporary password is ' + str(password)
        send_mail(
            'temp password',
            message,
            settings.EMAIL_HOST_USER,
            [em, ],
            fail_silently=False
        )
        logg.password = password
        logg.save()
        return HttpResponse('<script>alert("success");window.location="/tvshow_app/login/"</script>')
    else:
        return HttpResponse('<script>alert("invalid email");window.location="/tvshow_app/login/"</script>')









def login(request):
    return render(request,'login_index.html')

def login_post(request):
    lusername=request.POST['username']
    lpassword=request.POST['password']
    result=Login.objects.filter(username=lusername,password=lpassword)
    if result.exists():
        result2=Login.objects.get(username=lusername,password=lpassword)
        request.session['lid']=result2.id
        if result2.type=='admin':
            return HttpResponse('''<script>alert('admin login success');window.location='/tvshow_app/admin_home/ '</script>''')
        elif result2.type=='user':
            return HttpResponse('''<script>alert('user login success');window.location='/tvshow_app/user_home_index/'</script>''')
        else:
            return HttpResponse('''<script>alert('invalid password or username');'</script>''')

    else:
        return HttpResponse('''<script>alert('invalid password or bad credential');window.location='/tvshow_app/login'</script>''')

def logout(request):
    del request.session['lid']
    return HttpResponse('''<script>alert('you are logout success');window.location='/tvshow_app/login'</script>''')


def admin_home(request):
    var=Tvshow.objects.all()
    return render(request,'admin/tvshow_home.html',{'var':var})

def category(request):
    return render(request,'admin/category.html')

def category_post(request):
    name1=request.POST['cate']
    var=Category()
    var.category_name=name1
    var.save()
    return HttpResponse('''<script>alert("category addedd");window.location='/tvshow_app/category/'</script>''')


def category_view(request):
    var=Category.objects.all()
    return render(request,'admin/category_view.html',{'var':var})

def category_view_search(request):
    search= request.POST['search']
    var=Category.objects.filter(category_name__contains=search)
    return render(request,'admin/category_view.html',{'var':var})

def catagory_delete(request,id):
    var=Category.objects.get(id=id)
    var.delete()
    return HttpResponse('''<script>alert("category deleted");window.location='/tvshow_app/category_view'</script>''')

def category_edit(request,id):
    var = Category.objects.get(id=id)
    return render(request,'admin/category_edit.html',{'var':var})

def category_edit_post(request):
    c_id=request.POST['id']
    c_name=request.POST['cate']
    var=Category.objects.get(id=c_id)
    var.category_name=c_name
    var.save()

    return HttpResponse('''<script>alert("category UPDATED");window.location='/tvshow_app/category_view'</script>''')


def tv_shows(request):
    var=Category.objects.all()
    return render(request,'admin/tv_show.html',{'var':var})

def tv_shows_post(request):
    name=request.POST['name']
    category=request.POST['category']
    from_time=request.POST['time']
    duration=request.POST['duration']
    language=request.POST['language']
    description=request.POST['description']
    channelname = request.POST['channelname']
    actors_name = request.POST['actors_name']
    actress_name = request.POST['actress_name']
    producer_name = request.POST['producer_name']
    director_name = request.POST['director_name']
    Date =request.POST['date']


    dates=datetime.datetime.now().strftime('%Y%m%d-%H%M%S')+".jpg"
    image=request.FILES['image']
    fs=FileSystemStorage()
    fs.save(dates,image)
    path=fs.url(dates)

    date2=datetime.datetime.now().strftime('%y%m%d-%H%M%S')+".mp4"
    demo_video1=request.FILES['video']
    fs1=FileSystemStorage()
    fs1.save(date2,demo_video1)
    path2=fs1.url(date2)

    var=Tvshow()
    var.name=name
    var.CATEGORY_id=category
    var.from_time=from_time
    var.duration=duration
    var.language=language
    var.description=description
    var.channelname=channelname
    var.actors_name=actors_name
    var.actress_name=actress_name
    var.producer_name=producer_name
    var.director_name=director_name
    var.Date=Date
    var.demo_video=path2
    var.image=path
    var.save()


    return HttpResponse('''<script>alert("tv show added");window.location='/tvshow_app/tv_shows'</script>''')

def tvshow_view(request):
    var=Tvshow.objects.all()
    return render(request,'admin/tvshow_view.html',{'var':var})

def tvshow_view_post(request):
    search = request.POST['search']
    var = Tvshow.objects.filter(name__icontains=search)
    return render(request,'admin/tvshow_view.html',{'var':var})


def tv_show_delete(request,id):
    var=Tvshow.objects.get(id=id)
    var.delete()
    return HttpResponse('''<script>alert("tv show added");window.location='/tvshow_app/tvshow_view'</script>''')



def tv_show_edit(request,id):
    var=Tvshow.objects.get(id=id)
    var2=Category.objects.all()
    return render(request,'admin/tv_show_edit.html',{'var':var,'var2':var2})



def tv_show_edit_post(request):
   id=request.POST['id']
   names=request.POST['name']
   times=request.POST['time']
   dates=request.POST['date']
   durations = request.POST['duration']
   language = request.POST['language']
   descriptions = request.POST['description']
   channelnames = request.POST['channelname']
   actors_names = request.POST['actors_name']
   actress_names = request.POST['actress_name']
   producer_names = request.POST['producer_name']
   director_names = request.POST['director_name']

   if 'image' in request.FILES:
       images=request.FILES['image']
       date1 = datetime.datetime.now().strftime('%Y%M%D-%H%M%S') + '.jpg'
       fs = FileSystemStorage()
       fs.save(date1, images)
       path = fs.url(date1)
       obj=Tvshow.objects.get(id=id)
       obj.name=names
       obj.from_time=times
       obj.Date=dates
       obj.duration=durations
       obj.language=language
       obj.description=descriptions
       obj.channelname=channelnames
       obj.actors_name=actors_names
       obj.actress_name=actress_names
       obj.producer_name=producer_names
       obj.director_name=director_names
       obj.image=path
       obj.save()

       return HttpResponse('''<script>alert(' updated');window.location='/tvshow_app/tvshow_view'</script>''')
   else:
       obj = Tvshow.objects.get(id=id)
       obj.name = names
       obj.from_time = times
       obj.Date = dates
       obj.duration = durations
       obj.language = language
       obj.description = descriptions
       obj.channelname = channelnames
       obj.actors_name = actors_names
       obj.actress_name = actress_names
       obj.producer_name = producer_names
       obj.director_name = director_names
       obj.save()
       return HttpResponse('''<script>alert(' updated');window.location='/tvshow_app/tvshow_view'</script>''')

   if 'video' in request.FILES['video']:
       videos=request.FILES['video']
       date2 = datetime.datetime.now().strftime('%Y%M%D-%H%M%S') + '.mp4'
       fs1 = FileSystemStorage()
       fs1.save(date1, images)
       path = fs.url(date2)

       obj1 = Tvshow.objects.get(id=id)
       obj1.name = names
       obj1.from_time = times
       obj1.Date = dates
       obj1.duration = durations
       obj1.language = language
       obj1.description = descriptions
       obj1.channelname = channelnames
       obj1.actors_name = actors_names
       obj1.actress_name = actress_names
       obj1.producer_name = producer_names
       obj1.director_name = director_names
       obj1.demo_video = path
       obj1.save()
       return HttpResponse('''<script>alert(' updated');window.location='/tvshow_app/tvshow_view'</script>''')
   else:
       obj1 = Tvshow.objects.get(id=id)
       obj1.name = names
       obj1.from_time = times
       obj1.Date = dates
       obj1.duration = durations
       obj1.language = language
       obj1.description = descriptions
       obj1.channelname = channelnames
       obj1.actors_name = actors_names
       obj1actress_name = actress_names
       obj1.producer_name = producer_names
       obj1.director_name = director_names
       obj1.save()
       return HttpResponse('''<script>alert(' updated');window.location='/tvshow_app/tvshow_view'</script>''')







def view_user(request):
    var=User.objects.all()
    return render(request,'admin/view_user.html',{'var':var})
def view_user_post(request):
    search=request.POST['search']
    var=User.objects.filter(name__contains=search)
    return render(request, 'admin/view_user.html', {'var': var})


def admin_change_password(request):
    return render(request,'admin/admin_change_password.html')

def admin_change_password_post(request):
    old = request.POST['old_password']
    new = request.POST['new_password']
    confirm = request.POST['con_password']
    var= Login.objects.get(id=request.session['lid'])
    if var.password==old:
        if new == confirm:
            var.password=confirm
            var.save()
            return HttpResponse(
                '''<script>alert("user password changed");window.location='/tvshow_app/login'</script>''')
        else:
            HttpResponse('INVALID CONFIRM PASSWORD')
    else:
       return HttpResponse('''<script>alert("INVALID PASSWORD");window.location='/tvshow_app/admin_change_password'</script>''')












def view_review(request,id):
    var=Review.objects.filter(TVSHOW_id=id)
    return render(request,'admin/view_review.html',{'var':var})

def complaint_reply(request,id):
    var=Complaint.objects.get(id=id)
    return render(request,'admin/complaint_reply.html',{'var':var})

def complaint_reply_post(request):
    var=request.POST['reply']
    var2=request.POST['id']
    a=Complaint.objects.get(id=var2)
    a.reply=var
    a.status='repied'
    a.save()
    return HttpResponse('''<script>alert("reply has been successfully sent");window.location='/tvshow_app/view_complaints'</script>''')








# =========================================================================================================================
def user_home_index(request):
    return render(request,'user/user_home_index.html')

def signup(request):
    return render(request,'user/signup_index.html')

def signup_post(request):
    name=request.POST['name']
    house=request.POST['house_name']
    post=request.POST['post_name']
    landmark=request.POST['landmark']
    street=request.POST['street_name']
    district=request.POST['district']
    email=request.POST['email']
    phone=request.POST['phone']
    gender=request.POST['gender']
    password=request.POST['password']

    date=datetime.datetime.now().strftime("%y%m%d-%H%M%S")+".jpg"
    file=request.FILES['image']
    fs=FileSystemStorage()
    fs.save(date,file)
    path=fs.url(date)


    var=Login()
    var.username=email
    var.password=password
    var.type='user'
    var.save()

    var2=User()
    var2.LOGIN_id=var.id
    var2.name=name
    var2.house_name=house
    var2.post_name=post
    var2.landmark=landmark
    var2.street_name=street
    var2.district=district
    var2.phone=phone
    var2.gender=gender
    var2.email=email
    var2.image=path
    var2.save()

    return HttpResponse('''<script>alert("user register success");window.location='/tvshow_app/login'</script>''')


def view_tv_shows(request):
    var=Tvshow.objects.all()

    return render(request, 'user/view_tv_shows.html',{'var':var})

def view_tv_shows_post(request):
    search = request.POST['search']
    var = Tvshow.objects.filter(name__icontains=search)
    return render(request,'user/view_tv_shows.html',{'var':var})


def view_user_profile(request):
    var = User.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'user/view_user_profile.html',{'var':var})


def user_change_password(request):

    return render(request,'user/user_change_password.html')

def user_password_post(request):
    old=request.POST['old_password']
    new=request.POST['new_password']
    confirm=request.POST['con_password']
    if Login.objects.filter(id=request.session['lid'],password=old).exists():
        if new ==confirm:
            Login.objects.filter(id=request.session['lid']).update(password=confirm)
            return HttpResponse(
                '''<script>alert("user password changed");window.location='/tvshow_app/login'</script>''')
        else:
            HttpResponse('INVALID CONFIRM PASSWORD')
    else:
        HttpResponse('INVALID OLD PASSWORD')



def sent_review(request,id):

    return render(request,'user/sent_review.html',{'id':id})

def sent_review_post(request):
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer as SIA

    var=request.POST['review']
    var2=request.POST['rid']

    print(var2)
    date=datetime.datetime.now().strftime('%Y-%m-%d')
    robj=Review()
    robj.review=var
    robj.date=date

    robj.TVSHOW= Tvshow.objects.get(id=var2)
    robj.USER_id=User.objects.get(LOGIN_id=request.session['lid']).id

    def sentiment_scores1(sentence):
        # Here, we will create a SIA object.
        sid_obj1 = SIA()

        # Now, we will create polarity_scores method of SIA object
        # gives a sentiment dictionary. which contains positive (pos), negative (neg), # neutral (neu), and compound scores.
        sentiment_dict1 = sid_obj1.polarity_scores(sentence)

        print("The overall sentiment dictionary is: ", sentiment_dict1)
        # print("The sentence has been rated as ", sentiment_dict1['neg'] * 100, "% Negative")
        # print("The sentence has been rated as ", sentiment_dict1['neu'] * 100, "% Neutral")
        print("The sentence has been rated as ", sentiment_dict1['pos'] * 100, "% Positive")

        # print("The sentence Overall Rated As ", end=" ")

        return sentiment_dict1['pos'] * 100

    s=sentiment_scores1(var)

    robj.score=s
    robj.save()

    return HttpResponse('''<script>alert(" succesfully sent");window.location='/tvshow_app/view_tv_shows'</script>''')

def user_view_review(request,id):
    var=Review.objects.filter(id=id)
    return render(request,'user/user_view_review.html',{'var':var})


def sent_complaint(request):
    return render(request,'user/sent_complaint.html')

def sent_complaint_post(request):
    var=request.POST['complaint']

    date=datetime.datetime.now().strftime('%Y-%m-%d')
    c_obj=Complaint()
    c_obj.complaint=var
    c_obj.date=date
    lid = request.session['lid']
    id = User.objects.get(LOGIN_id=lid)
    c_obj.USER_id = id.id
    # c_obj.USER_id=User.objects.get(LOGIN_id=request.session['lid']).LOGIN_id
    c_obj.save()
    return HttpResponse('''<script>alert("complaint succesfully sent");window.location='/tvshow_app/sent_complaint'</script>''')


def view_complaints(request):
    var=Complaint.objects.all()
    return render(request,'admin/view_complaint.html',{'var':var})

def view_complaints_search(request):
    f=request.POST["f"]
    t=request.POST["t"]
    var=Complaint.objects.filter(date__range=[f,t])
    return render(request,'admin/view_complaint.html',{'var':var})

def user_view_reply(request):
    var=Complaint.objects.filter(USER__LOGIN=request.session['lid'])
    return render(request,'user/user_view_reply.html',{'var':var})



def user_view_replysearch(request):
    f=request.POST['f']
    t=request.POST['t']
    var=Complaint.objects.filter(USER__LOGIN=request.session['lid'], date__range=[f,t])
    return render(request,'user/user_view_reply.html',{'var':var})



def viewgeneratedratings(request):
    sall=Tvshow.objects.all()

    m=[]

    for i in sall:
        rall= Review.objects.filter(TVSHOW=i)
        totalrating= rall.aggregate(Avg('score'))
        print(totalrating)

        try:
            s=float(str(totalrating['score__avg']))
            m.append({'show': i, 'rating': s })
        except:
            m.append({'show': i, 'rating': 0})


    for i in range(0,len(m)):
        for j in range(0,len(m)):

            if m[i]['rating']> m[j]['rating']:
                temp=m[i]
                m[i]=m[j]
                m[j]=temp




    return render(request,"user/view_tv_shows_ratings.html",{'data': m})



