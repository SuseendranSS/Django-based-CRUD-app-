import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cruddemo.settings')

import django
django.setup()
from crudapp.models import *

from random import randint
from faker import Faker

faker = Faker()


def populate(n):
    for i in range(n):
        fsno = randint(4, 100)
        fsname = faker.name()
        fsclass = randint(1, 10)
        fsaddr = faker.city()
        stud_record, created = Student.objects.get_or_create(
            sno=fsno, sname=fsname, sclass=fsclass, saddr=fsaddr)


populate(20)
