# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse
from blog.models import BlogPost

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
# from django.http import HttpResponse
from django.utils import simplejson as json
from django.views.decorators.csrf import csrf_exempt

from celery.result import AsyncResult

from blog import tasks
import sys
# import logging
# logger = logging.getLogger(__name__)
def archive(request):
    posts = BlogPost.objects.all()
    t = loader.get_template("archive.html")
    c = Context({ 'posts':posts })
    return HttpResponse(t.render(c))
#    return HttpResponse("1")

#from django.http import HttpResponse
#import datetime

#def hello(request):
#	now = datetime.datetime.now()
#	html = "<html><body>Now<br> %s</body></html>" %now
#	return HttpResponse(html)



def home(request):
	if 'task_id' in request.session.keys() and request.session['task_id']:
		task_id = request.session['task_id']
	# logger.error('Something went wrong!')
	# logging.error('Something went wrong!')
	print >>sys.stderr, 'Goodbye, cruel world!'
	return render_to_response('home.html', locals(),\
								context_instance=RequestContext(request))


@csrf_exempt
def do_task(request):
	print >>sys.stderr, 'do task'
	data = 'Fail'
	print >>sys.stderr, '_______ data fail'
	if request.is_ajax():
		print >>sys.stderr, '_______ if request.is_ajax'
		job = tasks.create_models.delay()
		print >>sys.stderr, '_______ job'
		request.session['task_id'] = job.id
		print >>sys.stderr, '_______ job.id'
		data = job.id
		print >>sys.stderr, '_______ data_job'
	else:
		data = 'This is not an ajax request!'
		
	json_data = json.dumps(data)

	return HttpResponse(json_data, mimetype='application/json')


@csrf_exempt
def poll_state(request):
	""" A view to report the progress to the user """
	data = 'Fail'
	if request.is_ajax():
		if 'task_id' in request.POST.keys() and request.POST['task_id']:
			task_id = request.POST['task_id']
			task = AsyncResult(task_id)
			data = task.result or task.state
		else:
			data = 'No task_id in the request'
	else:
		data = 'This is not an ajax request'

	json_data = json.dumps(data)

	return HttpResponse(json_data, mimetype='application/json')
