from django.shortcuts import render
from django.utils.translation import gettext as _

def home(request):
	text = _('Maktab')
	return render(request=request, template_name='index.html', context={'text': text})
