from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Quote, About_art
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    all_quotes = Quote.objects.all()
    context = {
        'all_quotes': all_quotes,
    }
    return render(request,'apage/index.html', context)

def detail(request, quote_id):
    try:
        aritst_history = Quote.objects.get(pk=quote_id)
    except(Http404):
        return HttpResponse("Page Doesn't exist")
    else:
        return HttpResponse('<h4>history of Artist of quote id' + str(quote_id) +'</h4>')
