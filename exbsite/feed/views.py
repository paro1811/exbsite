from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
import datetime
# Create your views here.
from .models import Post, Picture # User
from .forms import PostForm, ImagesForm

def index(request):
    messages.success(request, "Success: This is the sample success Flash message.")
    return HttpResponse("This is the feed") 

def echo(request, myid):
	return HttpResponse("You said %s" %myid)

def listFeed(request):
    posts_db = Post.objects.all().order_by('-post_id') 
    posts_display = []
    #output = ''
    for p in posts_db:
        #u = User.objects.get(user_id=p.user_id)
        pics = Picture.objects.filter(post = p.post_id)

        post_display = {'post_title':p.post_title, 'post_text': p.post_text, 'post_author':p.post_author, 'post_grade': p.post_grade, 'post_email': p.post_email, 'post_id':p.post_id, 'pics':pics}
        posts_display.append(post_display)

        #pics = Picture.objects.all()#filter(pic_post_id = p.post_id)
    #    print (p.post_id)
    #	output = output + post.post_title + '>' + user.user_name + "<br>"
    return render(request, 'list_feed.html',{'posts_display':posts_display})

def postForm(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            p = Post(post_title= form.cleaned_data['title'], post_text = form.cleaned_data['text'] , post_date = datetime.datetime.now(), post_author= form.cleaned_data['name']  , post_grade= form.cleaned_data['grade']  , post_email= form.cleaned_data['email'] )
            p.save()
            
            pic = Picture(post=p, pic=request.FILES['pic'])
            pic.save()
            pic.shrink_image()
            
            pic1 = Picture(post=p, pic=request.FILES.get('pic1', ''))
            pic1.save()
            pic1.shrink_image()
            
            pic2 = Picture(post=p, pic=request.FILES.get('pic2', ''))
            pic2.save()
            pic2.shrink_image()
            
            messages.success(request, 'Your post has been successfully posted!')
            return HttpResponseRedirect('/feed/listFeed/')
    else:
        form= PostForm()
    return render(request, 'create_post.html', {'form': form})

def thanks(request):
  output = "<p>thanks<br> <a href='/feed/listFeed/'>Return To</a></p>"
  return HttpResponse(output)

def pic(request):
    if request.method == 'POST':
        form = ImagesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/feed/success/')
    else:
        form = ImagesForm()
    return render(request, 'upload_image.html', {'form': form})

def success(request):

    output = "<p> success <br> <a href='/feed/display_image/'> See image </a></p>"
    return HttpResponse(output)

def display_image(request):
    if request.method == 'GET':
        images = Picture.objects.all()
    return render(request, 'display_image.html',{'Images': images} )






