# Create your views here.
from django.http import Http404
from django.template import TemplateDoesNotExist
from django.views.generic.simple import direct_to_template

def index_page(request, page):
    try:
        return direct_to_template(request, template="index.html")
    except:
        raise Http404()

