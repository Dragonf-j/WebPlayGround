
from .models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .forms import PageForm
from django.shortcuts import redirect


class stafRequeredMixin(object):
    """
    Este mixin sirve para que el usuario sea miembro del staff y pueda editar, crear o borrar paginas siempre y cuando este logueado y sea miebro
    """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect(reverse_lazy('admin:login'))
        return super(stafRequeredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class PagesLestview(ListView):
    model = Page

class PageDetailView(DetailView):
    model = Page

class PageCreateView(stafRequeredMixin, CreateView):
    model = Page
    form_class = PageForm
    #fields = ['title','content','order']
    success_url = reverse_lazy('pages:pages')
    #def get_success_url(self) -> str:
        #return reverse('pages:pages')
    

class PageUpdateView(stafRequeredMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = "_update_form"
    success_url = reverse_lazy('pages:pages')
    def get_success_url(self):
        return reverse_lazy('pages:update', args={self.object.id}) + '?ok'

class PageDelete(stafRequeredMixin, DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')