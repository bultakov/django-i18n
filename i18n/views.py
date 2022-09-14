from django.shortcuts import render
from django.utils.translation import gettext as _

from .models import News

def home(request):
	text = _('Maktab')
	news = News.objects.all()
	return render(request=request, template_name='index.html', context={'text': text, "news": news})
