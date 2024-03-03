from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name ="core/home.html"
    #*def get_context_data(self, **kwargs):
    # context = super().get_context_data(**kwargs)
    #* context["Tittle"] = "Mi super web playgorund"
    #* return context
    def get(self, request, *args,**kwagars):
        return render(request, self.template_name, {"Tittle":"Mi super web playhround"})

class  samplepageView(TemplateView):
    template_name_sample ="core/sample.html"