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

# def logout_view(request):
#     logout(request)
#     success_url = reverse_lazy('apage:index')
#     return redirect(success_url)
#


class UserFormView(View):
    form_class = User_Form
    template_name = 'apage/registration_form.html'

    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    #now user has all the info filled in and submitting it
    #so now process data

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            #cleaned (normalized data)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user.set_password(password)
            user.save()

            #returns user objects after authentication if credentials are correct
            user = authenticate(request, username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('apage:index')
        return render(request, self.template_name, {'form': form})



