from django import forms
from django.core import validators


from .models import Bb, Rubric

class BbForm(forms.ModelForm):
	title = forms.CharField(label='Name of product',
		validators=[validators.RegexValidator(regex='^.{4,}$')],
		error_messages={'invalid':'Invalid name of your product!'})
	content = forms.CharField(label='Describe it',
		widget=forms.widgets.Textarea(attrs={
			'rows':10,
			'cols':25,
			'style':'resize:none;'}))
	price = forms.DecimalField(label='Price',decimal_places=2)
	rubric = forms.ModelChoiceField(queryset=Rubric.objects.all(),
		label='Rubric', help_text='Do not forget to choice rubric!',
		widget=forms.widgets.Select(attrs={'size':8}))
	class Meta:
		model = Bb
		fields = ('title','content','price','rubric')

