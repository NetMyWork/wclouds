from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
class Community(models.Model):
    comname=models.CharField(max_length=200)
    users=models.IntegerField(default=0)
    clouds=models.IntegerField(default=0)
    creater=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comimage=models.ImageField(upload_to='com_image',default='none.jpg')
    bio=models.TextField(null=True)
    def __str__(self):
        return self.comname
class Topic(models.Model):
    name=models.CharField(max_length=300)
    def __str__(self):
        return self.name
class Cloud(models.Model):
    cname=models.CharField(max_length=200)
    bio=models.TextField()
    readers=models.IntegerField(default=0)
    cimage=models.ImageField(upload_to="cloud_image",default='none.jpg')
    community=models.ForeignKey(Community,on_delete=models.SET_NULL, null=True)
    creater=models.ForeignKey(User,on_delete=models.SET_NULL ,null=True)
    recomend=models.IntegerField(default=0)
    location=models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.cname
class Blog(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)
    caption=models.CharField(max_length=300)
    image=models.ImageField(upload_to='blog_image',blank=True)
    video=models.FileField(upload_to='blog_videos',blank=True)
    creater=models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    cloud=models.ForeignKey(Cloud,on_delete=models.SET_NULL,null=True)
    body=RichTextUploadingField(blank=True, null=True)
    recomend=models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True,editable=False)
    location=models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.caption
class SavedBlog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
class Message(models.Model): 
    sender = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='sent_messages') 
    recipient = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,related_name='recieved_messages') 
    subject = models.CharField(max_length=255) 
    body=RichTextUploadingField(blank=True, null=True)
    image=models.ImageField(upload_to='blog_elements_images',blank=True)
    video=models.FileField(upload_to='blog_elements_videos',blank=True)
    audio=models.FileField(upload_to='blog_elements_audios', blank=True)
    iframe=models.FileField(upload_to='blog_elements_files', blank=True)
    created_at = models.DateTimeField(auto_now_add=True) 
class likeposts(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    post=models.ForeignKey(Blog,on_delete=models.SET_NULL,null=True)
class likeclouds(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    post=models.ForeignKey(Cloud,on_delete=models.SET_NULL,null=True)
class ShareBlogs(models.Model):
    sender=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='sender')
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE,null=True,blank=True)
    reciever=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='recieve')
    comment=models.CharField(max_length=500,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.sender.username
class ShareClouds(models.Model):
    sender=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='sendercloud')
    reciever=models.ForeignKey(User, on_delete=models.SET_NULL, null=True,related_name='recievercloud')
    blog=models.ForeignKey(Cloud,on_delete=models.CASCADE)
    comment=models.CharField(max_length=500,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.sender.username
