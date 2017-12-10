from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Quote, About_art
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login
from .forms import User_Form
from django.contrib.auth import logout
from django.contrib.auth.models import User


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

class QuoteCreate(CreateView):
    model = Quote
    fields = ['text', 'tag', 'artist']

class QuoteUpdate(UpdateView):
    model = Quote
    fields = ['text', 'tag', 'artist']

class QuoteDelete(DeleteView):
    model = Quote
    success_url = reverse_lazy('apage:index')














#this one didnt work so far as below
# def logout_view(request):
#     logout(request)
#     success_url = reverse_lazy('apage:index')
#     return redirect(success_url)
#

