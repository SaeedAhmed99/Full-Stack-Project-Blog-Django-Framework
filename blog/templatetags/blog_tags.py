from django import template
from ..models import post, comment

register = template.Library()
@register.inclusion_tag('blog/latest_posts.html')
def latest_posts():
    context = {
        'l_posts': post.objects.all()[0:5],
    }
    return context


@register.inclusion_tag('blog/latest_comments.html')
def latest_comments():
    context = {
        'l_comments': comment.objects.filter(active=True)[:5],
    }
    return context