from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Quote, About_art
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DeleteView, UpdateView
from django.views import generic

# Create your views here.

def index(request):
    all_quotes = Quote.objects.all()
    return render(request,'apage/index.html', {'all_quotes': all_quotes})

class Index(generic.ListView):
    template_name = 'apage/index.html'
    context_object_name = 'all_quotes'

    def get_queryset(self):
        return Quote.objects.all()

def detail(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id)
    return render(request, 'apage/detail.html', {'quote': quote})

class Detail(generic.DetailView):
    template_name = 'apage/detail.html'
    model = Quote

