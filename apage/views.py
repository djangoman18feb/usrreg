from .models import Quote
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views import generic
from django.views.generic import CreateView, DeleteView, UpdateView
from .models import Quote


def index(request):
    all_quotes = Quote.objects.all()
    return render(request,'apage/index.html', {'all_quotes': all_quotes})


def detail(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id)
    return render(request, 'apage/detail.html', {'quote': quote})


class Index(generic.ListView):
    template_name = 'apage/index.html'
    context_object_name = 'all_quotes'

    def get_queryset(self):
        return Quote.objects.all()

class Detail(generic.DetailView):
    template_name = 'apage/detail.html'
    model = Quote


class QuoteCreate(CreateView):
    model = Quote
    fields = ['text', 'tag']

class QuoteUpdate(UpdateView):
    model = Quote
    fields = ['text', 'tag']

class QuoteDelete(DeleteView):
    model = Quote
    success_url = reverse_lazy('apage:index')
