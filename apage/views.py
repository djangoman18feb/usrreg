from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Quote, About_art

# Create your views here.

def index(request):
    all_quotes = Quote.objects.all()
    template = loader.get_template('apage/index.html')
    context = {
        'all_quotes': all_quotes,
    }



    # html = ''
    # for quote in all_quotes:
    #     url = '/apage/' + str(quote.id) +'/'
    #     html+= '<a href="' + url + '">' + quote.text + '</a><br>'
    return HttpResponse(template.render(context, request))

def detail(request, quote_id):
    return HttpResponse('<h4>history of Artist of quote id' + str(quote_id) +'</h4>')
