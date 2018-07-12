from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from polls.models import *
from django.utils import timezone
import random
import datetime
def drawn(request,question_id):
    f = Questionaire.objects.filter(id=question_id)[0]
    if timezone.now()<f.end_time:
        return HttpResponse('还没开始抽奖')
    if f.drawnd == False:
        return HttpResponse( '还未完成抽奖')

    f=f.answer_set.all().filter(drawn=True).order_by('answer_drawn')
    template = loader.get_template('polls/drawn.html')
    r = [i for i in f]
    for k in range(len(r)):
        r[k].answer_phonenumber=r[k].answer_phonenumber%10000
    f=r
    context = {
        'f': f,
    }
    return HttpResponse(template.render(context, request))
def rank2(request):
    print('kk')
    b=request.GET['ids']
    if len(b)>0:
        b=b.replace(',', '')
    template = loader.get_template('polls/cj.html')
    context = {
        'b': b,
    }
    return HttpResponse(template.render(context, request))