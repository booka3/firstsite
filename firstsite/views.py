from django.http import HttpResponse
import datetime

def hello(request):
	now = datetime.datetime.now()
	html = "<html><body>Now<br> %s</body></html>" %now
	return HttpResponse(html)

def hello2(request):
	now = datetime.datetime.now()
	html = "<html><body>Now2<br> %s</body></html>" %now
	return HttpResponse(html)
