from django.shortcuts import render
from django.views.generic import ListView, DetailView

from news.utils import MyMixin
from .models import Rubric

# Create your views here.


def test(request):
    return render(request, "testapp/test.html", {'rubrics': Rubric.objects.all()})

class GetRubric(DetailView):
    model = Rubric
    template_name = 'testapp/rubric.html'
    context_object_name = 'rubric'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context