from django.db import models

# Create your models here.

class Source(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100, blank=True)
    # type = {book, magazine, url, image}  ### <--- add this !
    def __unicode__(self):
   	 return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField(max_length=200, blank=True)
    #
    source = models.ForeignKey(Source)
    srcPage = models.CharField(max_length=20, blank=True)
    srcURL = models.CharField(max_length=200, blank=True)
    #
    #ingredients = models.ManyToManyField(Ingredient, through = 'IngredientList')  # <-- need to try this
    #
    def __unicode__(self):
   	 return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
   	 return self.name

class IngredientList(models.Model):
    recipe = models.ForeignKey(Recipe)
    ingredient = models.ForeignKey(Ingredient)
    quantity = models.CharField(max_length=50)
    units = models.CharField(max_length=50, blank=True)	

