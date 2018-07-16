from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from polls.models import *
from django.utils import timezone
import random
import datetime
import numpy as np

def index(request,question_id):
    z=question_id
    if timezone.now()<Questionaire.objects.filter(id=question_id)[0].pub_date:
        return HttpResponse('还没开始')
    if timezone.now()>Questionaire.objects.filter(id=question_id)[0].end_time:
        return HttpResponse('已经结束')
    f=Questionaire.objects.filter(id=question_id)[0]
    latest_question_list = f.question_set.all().order_by('pub_date')[:5]
    t1 = datetime.datetime.strftime(f.pub_date, '%Y年-%m月-%d日 %H:%M:%S')
    t2 = datetime.datetime.strftime(f.end_time, '%Y年-%m月-%d日 %H:%M:%S')
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
        'f':f,
        't1':t1,
        't2':t2,
        'z' :z,
    }
    return HttpResponse(template.render(context, request))

def vote(request):
    aire=request.POST.get('wjid',1)
    name1 = Questionaire.objects.filter(id=int(aire))[0].question_set.all().order_by('pub_date')[:5]
    f = request.POST['phone_number']
    if Questionaire.objects.get(id=aire).answer_set.filter(answer_phonenumber=f):
        return HttpResponse('抱歉，您已经答过题了')
    s=''
    q=1
    num=0
    for i in name1:
        s=s+' '+str(q)+'.'
        q=q+1

        if i.sf==True:
            r=0
            for j in i.choice_set.all():
                if (request.POST.get('r'+str(j.id),1)!=1) :
                    s = s + j.choice_text[0]
                    if Choice.objects.filter(id=int(request.POST['r'+str(j.id)]))[0].answer==True:
                        r=r+2
            if r < 0:
                r = 0
            if r < len(i.choice_set.all()):
                r = 1
            if r == len(i.choice_set.all()):
                r = 2
            num=num+r
        else:
            if (request.POST.get('r'+str(i.id), 1) != 1):
                s = s + Choice.objects.get(id=int(request.POST['r' + str(i.id)])).choice_text[0]
                if Choice.objects.get(id=int(request.POST['r' + str(i.id)])).answer==True:
                    num = num + 2

    q = answer(questionaire_id=aire, answer_name=request.POST['firstname'], answer_email=request.POST['email'], answer_number=num, answer_choice=s, answer_phonenumber=f )
    q.save()

    return HttpResponse('感谢您的参与')

def rank1(request):
    a=int(request.POST['j1'])
    b=request.POST['wjid']
    ans=[]
    FA=think.objects.get(votes=a)
    FA1=FA.gt_set.all()
    a = np.array([[0 for i in range(len(FA1))] for i in range(2)])
    i=0
    for j in FA1:
        a[0][i]=j.num
        a[1][i] = j.votes
        i=i+1
    c=a[1]
    a=a[0]
    for i in b:
        j=Questionaire.objects.get(id=int(i))
        ranki = j.answer_set.all().filter(answer_number__gte=len(FA1)).order_by('answer_number')
        if len(ranki)<sum(a):
            return HttpResponse(j.questionaire_text+'抽奖人数不足')
        if j.drawnd==True:
            return HttpResponse(j.questionaire_text + '抽过奖了')
        if timezone.now() < j.pub_date:
            return HttpResponse('还没开始')
        if timezone.now() > j.end_time:
            return HttpResponse('已经结束')
        R = np.array([i.answer_number for i in ranki])
        r=[i for i in range(len(ranki))]
        p=0
        for i in c:
            S=np.where(R >= i)[0]
            random.shuffle(S)
            S=S[:a[p]]
            for l in S:
                R[l]=0
                ranki[r[l]].drawn = True
                ranki[r[l]].answer_drawn = FA1[int(p)].name
                ranki[r[l]].save()
            p=p+1
        j.drawnd = True
        j.save()
    for i in b:
        q=Questionaire.objects.get(id=int(i)).answer_set.all().filter(drawn=True).order_by('answer_drawn')
        ans.append(q)
    template = loader.get_template('polls/answer.html')
    context = {
        'ans': ans,
    }
    return HttpResponse(template.render(context, request))
