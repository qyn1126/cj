from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from polls.models import *
from django.utils import timezone
import random
import datetime
def index(request,question_id):
    if timezone.now()<Questionaire.objects.filter(id=question_id)[0].pub_date:
        return HttpResponse('还没开始')
    if timezone.now()>Questionaire.objects.filter(id=question_id)[0].end_time:
        return HttpResponse('已经结束')
    f=Questionaire.objects.filter(id=question_id)[0]
    latest_question_list = f.question_set.all().order_by('-pub_date')[:5]
    t1 = datetime.datetime.strftime(f.pub_date, '%Y年-%m月-%d日 %H:%M:%S')
    t2 = datetime.datetime.strftime(f.end_time, '%Y年-%m月-%d日 %H:%M:%S')
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
        'f':f,
        't1':t1,
        't2':t2,
    }
    return HttpResponse(template.render(context, request))

def vote(request):
    aire=request.POST.get('wjid',1)
    name1 = Questionaire.objects.filter(id=int(aire))[0].question_set.all().order_by('-pub_date')[:5]
    f = request.POST['phone_number']
    if Questionaire.objects.get(id=aire).answer_set.filter(answer_phonenumber=f):
        return HttpResponse('抱歉，您已经答过题了')
    s=''
    q=1
    num=0
    r = 0
    for i in name1:
        s=s+' '+str(q)+'.'
        q=q+1

        if i.sf==True:
            r=0
            for j in i.choice_set.all():
                if (request.POST.get(str(j.id),1)!=1) :
                    s = s + j.choice_text[0]
                    r=r+Choice.objects.filter(id=int(request.POST[str(j.id)]))[0].votes
                    if r<0:
                        r=0
        else:
            if (request.POST.get(str(i.id), 1) != 1):
                s=s+Choice.objects.get(id=int(request.POST[str(i.id)])).choice_text[0]
                num=num+Choice.objects.get(id=int(request.POST[str(i.id)])).votes
            else:
                template = loader.get_template('polls/dx.html')
                context = {
                    'aire': aire,
                }
                return HttpResponse(template.render(context, request))

    num=num+r
    if num>5:
        num=5
    q = answer(questionaire_id=aire, answer_name=request.POST['firstname'], answer_email=request.POST['email'], answer_number=num, answer_choice=s, answer_phonenumber=f )
    q.save()

    return HttpResponse(s)

def rank1(request):
    a=(int(request.POST['j1']),int(request.POST['j2']),int(request.POST['j3']))
    c=int(request.POST['j4'])
    b=request.POST['wjid']
    o=''
    ans=[]

    for i in b:
        j=Questionaire.objects.get(id=int(i))
        ranki=j.answer_set.all().filter(answer_number__gte=c)
        if len(ranki)<sum(a):
            return HttpResponse(j.questionaire_text+'抽奖人数不足')
        if j.drawnd==True:
            return HttpResponse(j.questionaire_text + '抽过奖了')
        if timezone.now() < j.pub_date:
            return HttpResponse('还没开始')
        if timezone.now() > j.end_time:
            return HttpResponse('已经结束')
        r=[i for i in range(len(ranki))]
        random.shuffle(r)
        z=0
        zz=0
        for k in range(len(a)):
            for l in range(a[z]):
                ranki[r[zz]].drawn=True
                ranki[r[zz]].answer_drawn=str(z+1)+'等奖'
                ranki[r[zz]].save()
                zz=zz+1
            z=z+1
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
