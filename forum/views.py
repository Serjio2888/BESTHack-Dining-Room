from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponse

from forum.models import Topic, Bucket
from forum.forms import CommentForm, TopicForm

import os
import time

from django.shortcuts import render_to_response
from django.template import RequestContext

def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response

def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response

t = time.localtime()

topics = Topic.objects.all()
context = {'topics': topics,
                'see_bucket':'see_bucket',
               'topic_add_url':'add_topic',
               'topic_sorted':'sorted',
		'hour':t.tm_hour+3,
		'minute':t.tm_min,
		'add_to_bucket':'bucket'}

def index(request):
    t = time.localtime()
    topics = Topic.objects.all()
    drinks = Topic.objects.filter(food_type="DR")
    mains = Topic.objects.filter(food_type="MC")
    salads = Topic.objects.filter(food_type="SD")
    firsts = Topic.objects.filter(food_type="FC")
    context = {	'drinks': drinks,
		'firsts':firsts,
		'salads':salads,
		'mains':mains,
                'see_bucket':'see_bucket',
               'topic_add_url':'add_topic',
               'topic_sorted':'sorted',
		'hour':t.tm_hour+3,
		'minute':t.tm_min,
		'add_to_bucket':'bucket'}
    return render(request, 'index.html', context)

def cleaning(request):
    meals = Bucket.objects.all().delete()
    
    return index(request)

def see(request):
    meals = Bucket.objects.all()
    allprice = int()
    allcall = int()
    for m in meals:
        my = str(m).split('|')
        allprice+=int(my[2])
        allcall+=int(my[1])

    context = {'meals': meals,
                'allprice':allprice,
                'allcall':allcall,
		'hour':t.tm_hour+3,
		'minute':t.tm_min}
    return render(request, 'see_bucket.html', context)

def bucket(request):

    for i in request.POST:
        arr = i.split('|')
        if len(arr)>2:
            b = Bucket(meal=str(arr[2]), price=int(arr[0]), calories=int(arr[1]))
            b.save()
    
    
    return index(request)



def sorted(request):

    topics = Topic.objects.all().order_by('-views')[:10]
    context = {'topics': topics,
               'topic_add_url':'add_topic',
               'topic_sorted':'sorted',
               'name':os.getlogin(),
		'hour':t.tm_hour+3,
		'minute':t.tm_min}
    return render(request, 'index.html', context)

class TopicView(DetailView):
    model = Topic
    template_name = 'topic.html'
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if True:
                q1 = Topic.objects.get(pk=context['topic'].id)
                q1.views += 1
                q1.save()
        context['comment_add_url'] = "/topic/{}/add_comment".format(context['topic'].id)
        return context

class CommentAdd(CreateView):
    template_name = 'comment_add.html'
    form_class = CommentForm

    def get_initial(self):
        return {
            "topic": self.kwargs['topic_pk']
        }

    def get_success_url(self):
        return "/topic/{}".format(self.kwargs['topic_pk'])


class TopicAdd(CreateView):
    template_name = 'topic_add.html'
    form_class = TopicForm

##    def get_initial(self):
##        return {
##            "topic": self.kwargs['topic_pk']
##        }

    def get_success_url(self):
        return "/"#.format(self.kwargs['topic_pk'])



