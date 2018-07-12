
python3 manage.py makemigrations polls
python3 manage.py migrate
python3 manage.py shell
python3 manage.py createsuperuser
python3 manage.py runserver
Question.objects.all()
from polls.models import *

__gt 大于
__gte 大于等于
__lt 小于
__lte 小于等于