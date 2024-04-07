
from .models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .forms import PageForm


# Create your views here.
class PagesLestview(ListView):
    model = Page

class PageDetailView(DetailView):
    model = Page

class PageCreateView(CreateView):
    model = Page
    form_class = PageForm
    #fields = ['title','content','order']
    success_url = reverse_lazy('pages:pages')
    #def get_success_url(self) -> str:
        #return reverse('pages:pages')

class PageUpdateView(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = "_update_form"
    success_url = reverse_lazy('pages:pages')
    def get_success_url(self):
        return reverse_lazy('pages:update', args={self.object.id}) + '?ok'

class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')