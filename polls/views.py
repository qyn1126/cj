from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.template import loader
from polls.models import *

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
def vote(request):
    name1 = Question.objects.order_by('-pub_date')[:5]

    s = 0
    for i in name1:
        s = s + int(request.POST[i.question_text])
    q = answer(answer_name=request.POST['firstname'], answer_email=request.POST['lastname'], answer_number=s)
    q.save()


    return HttpResponse(s)