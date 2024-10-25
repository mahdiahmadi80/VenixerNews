from django.contrib import admin
from .models import Post ,Category,Comment

class CommentsAdminInline(admin.TabularInline):
      model=Comment
      fields=['name','email','subject','message','active']
      extra=0

@admin.register(Post)
class Postadmin(admin.ModelAdmin):
    date_hierarchy='created_time'

    list_display=['id','title','active','updated_time'] 
    search_fields=('title','description')
    list_filter=['active']
    list_display_links =['id','title'] 
    inlines=[CommentsAdminInline]
    # exclude = ['active']

    def get_tags(self,obj):
          return ', '.join([o for o in obj.tags.names( )])

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
        list_display=['id','title']
# admin.site.register(Post,Postadmin)







# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display=['id','post','name','active']