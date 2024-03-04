
from .models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy

# Create your views here.
class PagesLestview(ListView):
    model = Page

class PageDetailView(DetailView):
    model = Page

class PageCreateView(CreateView):
    model = Page
    fields = ['title','content','order']
    success_url = reverse_lazy('pages:pages')
    #def get_success_url(self) -> str:
        #return reverse('pages:pages')