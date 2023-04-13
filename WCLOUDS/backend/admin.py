from django.contrib import admin
from .models import Community,Cloud,Blog,Topic,Message,SavedBlog,likeposts,likeclouds,ShareBlogs,ShareClouds
admin.site.register(Community)
admin.site.register(Cloud)
admin.site.register(Blog)
admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(SavedBlog)
admin.site.register(likeposts)
admin.site.register(likeclouds)
admin.site.register(ShareBlogs)
admin.site.register(ShareClouds)