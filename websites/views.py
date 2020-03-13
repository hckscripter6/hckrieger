from django.shortcuts import render
from .models import Website

# Create your views here.
def websites(request):
    website = Website.objects.order_by('-id').all()
    return render(request, 'websites/websites.html', {'website': website})