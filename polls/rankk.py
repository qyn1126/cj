from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from polls.models import *
from django.utils import timezone
def rank1(request):
    a=request.POST.get('ids')
    return HttpResponse(a)