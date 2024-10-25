from django import template
from ..models import Category, Post
from persiantools.jdatetime import JalaliDate

register=template.Library()

@register.simple_tag
def new_tag(name):
    return f" hi{name}this test"


@register.filter
def Upper(value):
    return value.upper()

@register.inclusion_tag('blog/includes/blog-recent.html')
def recent_news():
    posts=Post.objects.filter(active=1).order_by('-created_time')[:3]
    return {'posts': posts}

@register.filter
def jalali_date(value):
    return JalaliDate(value).strftime("%Y/%m/%d")



@register.inclusion_tag('blog/includes/blog-categories.html')
def category():
    categories =Category.objects.all()
    posts=Post.objects.filter(active=1)
    
    categories_count={}

    for cat in categories:
        categories_count[cat]=posts.filter(category__title=cat).count()
    return{'categories_count': categories_count}



@register.inclusion_tag('blog/includes/blog-tags.html')
def news_tags():
    posts=Post.objects.filter(active=1)
    return {'posts':posts}