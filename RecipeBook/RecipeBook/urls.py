from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from RecipeBook.models import Source,Recipe,Ingredient

from django.views.generic.simple import direct_to_template
from RecipeBook.views import index_page

urlpatterns = patterns('',
	('^index/$', direct_to_template, {'template': 'index.html'}),

	url(r'^listing$',   ### need index page ---> {Source/Recipe listings}
    	ListView.as_view(
        	queryset=Recipe.objects.order_by('name'),
        	context_object_name='recipe_list',
        	template_name='RecipeBook/recipeList.html')),

	url(r'^sources$',
    	ListView.as_view(
        	queryset=Source.objects.order_by('name'),
        	context_object_name='source_list',
        	template_name='RecipeBook/sourceList.html')),

	url(r'^Recipes$',
    	ListView.as_view(
        	queryset=Recipe.objects.order_by('name'),
        	context_object_name='recipe_list',
        	template_name='RecipeBook/recipeList.html')),
	url(r'^(?P<pk>\d+)/$',
    	DetailView.as_view(
        	model=Recipe,
        	template_name='RecipeBook/detail.html')),
)


