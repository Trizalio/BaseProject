from django.core.management.base import BaseCommand
from django.db import models
from django.contrib.auth.models import User
from mainapp.models import news, comment, userinfo, baseinfo, project, projectmember
import random
import datetime

class Command(BaseCommand):
    args = '<ask_id ask_id ...>'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        if args[0] == 'create':
            self.create(args[1], args[2])
        else:
            print "Command not found!"

    def create(self, model, count):
        if model == "User":
            self.createUser(count)
        elif model == "news":
            self.createQuestion(count)
        else:
            print "Not found model!"

    def createUser(self, count):
        for i in range(int(count)):
            name = random.choice(["Bender1","Bender2","Bender3","Bender4","Bender5"]) + str(i + 120) + str(i + 120)
            email = random.choice(["gmail"]) + random.choice(["yandex"]) + '@' + 'mail.ru'
            password = random.choice(["qwerty"]) + random.choice(["qwerty"]) + random.choice(["qwerty"]) + random.choice(["qwerty"])
            now = datetime.datetime.now()
            user = User.objects.create_user(username = name, email = email, password = password)
            user.save()
            print ("User created!")

    def createNews(self, count):
        for i in range(int(count)):
            now = datetime.datetime.now()
            header1 = random.choice("wvwvdwwferfdzfs") + random.choice("qdkgorjcscddfsfsdfl") + random.choice("dqjfiqjfksvjwm") + str(i)
            id = 1
            question1 = news(name = header1, discription = "discription", text = "text",  creationdate = now, creator_id = id, show = True)
            question1.save()
            print ("Question created!")

