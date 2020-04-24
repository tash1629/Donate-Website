from django.shortcuts import render
from django.http import HttpResponse

from .models import DonationLinks
# Create your views here.

def index(request):

    return render(request, 'donate/index.html') # arg is some text or html code

def detail(request):
    # try to go to a page and get donator name
    all_donation_links = DonationLinks.objects.all()
    context = {
        'all_donation_links': all_donation_links
    }
    return render(request, 'donate/detail.html', context)