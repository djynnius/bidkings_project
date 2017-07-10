from django.shortcuts import render,get_object_or_404

from django.views import generic
from django.utils import timezone

from .models import Bidders,Bids

# Create your views here.


class IndexViewBids(generic.ListView):
    template_name = 'user/index.html'

    def get_queryset(self):
        pass


class IndexView(generic.ListView):
    template_name = 'app/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions(not including
        those set to be published in the future)."""
        return Bidders.objects.all()

class BaseView(generic.ListView):
    template_name = 'user/base.html'
    model = Bidders
