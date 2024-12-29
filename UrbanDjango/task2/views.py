from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def index(request):
    return render(request, 'ind_func.html')


class Index2(TemplateView):
    template_name = 'ind_class.html'
