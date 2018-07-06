f = request.POST['f']
w = f[:5]
s = 0
for i in w:
    s = s + i
q = answer(answer_name=f[6], answer_email=f[7], answer_number=s)
q.save()

question.id = 100;
action="{% url 'polls:vote'%}" method="post"