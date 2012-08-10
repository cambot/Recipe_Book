from RecipeBook.models import Source,Recipe,Ingredient,IngredientList
from django.contrib import admin

class SourceAdmin(admin.ModelAdmin):
	# list_display determines display order on app admin screen
	list_display = ('name', 'url')


#By default, provide enough fields for 3 choices.
class IngredientInline(admin.TabularInline):
	model = IngredientList
	extra = 3


# field sets - grouping fields together
class RecipeAdmin(admin.ModelAdmin):
	# list_display determines display order on app admin screen
	list_display = ('name', 'notes', 'source', 'srcPage', 'srcURL')
	#
	# list of tuplest to determine order on editing screen: (Name, {set of fields and config} )
	fieldsets = [
    	('Recipe',	{'fields': ['name', 'notes']}),
    	('Source', 	{'fields': ['source', 'srcPage', 'srcURL'] }),
	]
	inlines = [IngredientInline]  	# related objects are edited on the parent obj admin page.
	search_fields = ['name']  # specify which fields to search  (uses LIKE)


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(Ingredient)
