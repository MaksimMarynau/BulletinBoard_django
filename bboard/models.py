from django.db import models

# Create your models here.

    
class Bb(models.Model):
	title = models.CharField(max_length=50, verbose_name='TITLE')
	content = models.TextField(null=True,blank=True, verbose_name='CONTENT')
	price = models.FloatField(null=True, blank=True, verbose_name='PRICE')
	published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='PUBLISHED')

	rubric = models.ForeignKey('Rubric', null=True,on_delete=models.PROTECT, verbose_name='Rubric')

	class Meta:
		verbose_name_plural = 'Advertisments'
		verbose_name = 'Advertisment'
		ordering = ['-published']


class Rubric(models.Model):
	name = models.CharField(max_length=20,db_index=True,verbose_name='NAME')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Rubrics'
		verbose_name='Rubric'
		ordering = ['name']
