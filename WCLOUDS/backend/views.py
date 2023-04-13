from django.shortcuts import render,redirect
from .models import Blog,Community,Cloud,SavedBlog,Message,likeposts,likeclouds,ShareBlogs,ShareClouds
from django.contrib.auth.models import User
from django.http import HttpResponse,JsonResponse
from django.contrib import messages
from itertools import chain

def home(request):
    blogs=Blog.objects.all()
    saved=SavedBlog.objects.filter(user=request.user)
    saved_blog = [post.blog for post in saved]
    liked = likeposts.objects.filter(user=request.user)
    liked_blogs = [likepost.post for likepost in liked]
    context = {
    'liked_blogs': liked_blogs
}
    mycom=Community.objects.filter(creater=request.user)
    community=Community.objects.all()
    clouds=Cloud.objects.all()
    return render(request,'index.html',{'blogs':blogs,'community':community,'mycom':mycom,'liked':liked_blogs,'saved':saved_blog,'clouds':clouds})
def blog(request,pk):
    blog=Blog.objects.get(id=int(pk))
    return render(request,'blog.html',{'blog':blog})
def community(request,pk):
    liked = likeclouds.objects.filter(user=request.user)
    liked_blogs = [likepost.post for likepost in liked]
    community=Community.objects.all()
    communit=Community.objects.get(id=int(pk))
    clouds=Cloud.objects.filter(community=communit)
    return render(request,'community.html',{'clouds':clouds,'communit':communit,'community':community,'liked':liked_blogs})
def gallery(request):
    liked = likeposts.objects.filter(user=request.user)
    liked_blogs = [likepost.post for likepost in liked]
    saved=SavedBlog.objects.filter(user=request.user)
    saved_blog = [post.blog for post in saved]
    mycom=Community.objects.filter(creater=request.user)
    community=Community.objects.all()
    clouds=SavedBlog.objects.filter(user=request.user)
    return render(request, 'gallery.html',{'clouds':saved_blog,'community':community,'mycom':mycom,'liked':liked_blogs})
def mycommunity(request):
    community=Community.objects.all()
    mycommunity=Community.objects.filter(creater=request.user)
    clouds=Cloud.objects.filter(creater=request.user)
    return render(request,'mycommunity.html',{'communit':mycommunity,'clouds':clouds,'community':community})
def cloud(request,pk):
    community=Community.objects.all()
    cloud=Cloud.objects.get(id=int(pk))
    blogs=Blog.objects.filter(cloud=cloud)
    return render(request,'cloud.html',{'clouds':blogs,'communit':cloud,'community':community})
def mail(request):
    users=User.objects.all()
    share=ShareBlogs.objects.filter(sender=request.user)
    
    got=ShareBlogs.objects.filter(reciever=request.user)
    shared_and_got = share | got
    shared_and_got_blogs = [post.blog for post in shared_and_got]
    sent_messages = request.user.sent_messages.all()
    received_messages = request.user.recieved_messages.all()
    
    sents=sent_messages.union(received_messages)
    
    community=Community.objects.all()
    return render(request,'mail.html',{'sents':sents,'recieves':received_messages,'community':community,'users':users,'shared':shared_and_got_blogs})
def likepost(request,pk):
    user=request.user
    blog=Blog.objects.get(id=int(pk))
    liked=likeposts.objects.filter(user=user,post=blog).first()
    if liked==None:
        blog.recomend=blog.recomend+1
        like=likeposts.objects.create(user=user,post=blog)
        blog.save()
        like.save()
        return redirect('/')
    else:
        liked.delete()
        blog.recomend=blog.recomend-1
        blog.save()
        return redirect('/')
def likecloud(request,pk):
    user=request.user
    blog=Cloud.objects.get(id=int(pk))
    liked=likeclouds.objects.filter(user=user,post=blog).first()
    if liked==None:
        blog.recomend=blog.recomend+1
        like=likeclouds.objects.create(user=user,post=blog)
        blog.save()
        like.save()
        return redirect('/')
    else:
        liked.delete()
        blog.recomend=blog.recomend-1
        blog.save()
        return redirect('/')

def save(request,pk):
    user=request.user
    blog=Blog.objects.get(id=int(pk))
    savedb=SavedBlog.objects.filter(user=user,blog=blog).first()
    if savedb==None:
        savednew=SavedBlog.objects.create(user=user,blog=blog)
        savednew.save()
        return redirect('/')
    else:
        savedb.delete()
        return redirect('/')
def share(request,pk):
    if request.method!="POST":
        users=User.objects.all()
        community=Community.objects.all()
        blog=Blog.objects.get(id=int(pk))
        return render(request,'share.html',{"post":blog,"community":community,'users':users})
    else:
        users=User.objects.all()
        
        blog=Blog.objects.get(id=int(pk))
        comname=request.POST['recieve']
        
        recipiant=User.objects.get(id=comname)
        newshare=ShareBlogs.objects.create(sender=request.user,reciever=recipiant,blog=blog)
        newshare.save()
        return redirect('/')
def shareclouds(request,pk):
    if request.method!="POST":
        users=User.objects.all()
        community=Community.objects.all()
        blog=Cloud.objects.get(id=int(pk))
        return render(request,'share.html',{"post":blog,"community":community,'users':users})
    else:
        users=User.objects.all()
        blog=Cloud.objects.get(id=int(pk))
        
        comname=request.POST['recieve']
        recipiant=User.objects.get(id=int(comname))
                
                
        newshare=ShareClouds.objects.create(sender=request.user,reciever=recipiant,blog=blog)
        newshare.save()
        return redirect('/')
def sent(request):
    if request.method=='POST':
        caption = request.POST['caption']
        body=request.POST['body']
        recipient=request.POST['recipient']
        image=request.FILES.get('image')
        
            
        
        video=request.FILES.get('video')
        
           
        
        audio=request.FILES.get('audio')
        
        
        iframe=request.FILES.get('document')
        recipient=User.objects.get(id=int(recipient))
        mes=Message.objects.create(subject=caption,body=body,image=image,video=video,audio=audio,iframe=iframe,sender=request.user,recipient=recipient)
        mes.save()
        return redirect('/')
def getMessages(request):
    message=Message.objects.filter(sender=request.user)

    return JsonResponse({'messages':message})
def mymessages(request,pk):
    message=Message.objects.get(id=int(pk))
    sender = message.sender
    return render(request,'mymessage.html',{'message':message, 'sender':sender})
def blog(request,pk):
    community=Community.objects.all()
    blog=Blog.objects.get(id=int(pk))
    liked = likeposts.objects.filter(user=request.user)
    liked_blogs = [likepost.post for likepost in liked]
    return render(request,'blog.html',{"blog":blog,'liked':liked_blogs,'community':community})




