from django.db import models
from django.contrib.auth.models import User

class userinfo(models.Model):
    owner = models.OneToOneField(User)

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    male = models.BooleanField(default=False)

    workstatus = models.CharField(max_length=100)
    access = models.CharField(max_length=100)
    education = models.TextField(max_length=2000)

    medic = models.BooleanField(default=False)
    hacker = models.BooleanField(default=False)
    programmer = models.BooleanField(default=False)
    security = models.BooleanField(default=False)
    engeneer1 = models.BooleanField(default=False)
    engeneer2 = models.BooleanField(default=False)
    engeneer3 = models.BooleanField(default=False)
    engeneer4 = models.BooleanField(default=False)
    

    bloodtype = models.CharField(max_length=100)
    surveydate = models.DateTimeField(auto_now=False, auto_now_add=False)

    story = models.TextField(max_length=2000)
    
    def __unicode__(self):
        return self.name

class news(models.Model):
    name = models.CharField(max_length=100)
    discription = models.TextField(max_length=200)
    text = models.TextField(max_length=2000)
    creationdate = models.DateTimeField(auto_now=False, auto_now_add=True)
    creator = models.ForeignKey(userinfo)
    rating = models.IntegerField(default=0)
    show = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["-creationdate"]

class project(models.Model):
    name = models.CharField(max_length=100)
    discription = models.TextField(max_length=200)
    text = models.TextField(max_length=2000)
    show = models.BooleanField(default=False)
    creationdate = models.DateTimeField(auto_now=False, auto_now_add=True)
    rating = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["-creationdate"]

class comment(models.Model):
    text = models.TextField(max_length=2000)
    creator = models.ForeignKey(userinfo)
    creationdate = models.DateTimeField(auto_now=False, auto_now_add=True)
    news = models.ForeignKey(news)
    rating = models.IntegerField(default=0)
    show = models.BooleanField(default=False)

    def __unicode__(self):
        return self.text

    class Meta:
        ordering = ["-creationdate"]

class projectmember(models.Model):
    owner = models.ForeignKey(userinfo)
    project = models.ForeignKey(project)
    status = models.CharField(max_length=100)
    importance = models.IntegerField(default=0)

    def __unicode__(self):
        return self.project.name

class baseinfo(models.Model):
    importance = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=20)
    show = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["-importance"]

class voice(models.Model):
    owner = models.OneToOneField(userinfo)
    target = models.IntegerField(default=0)
    value = models.IntegerField(default=0)
    project = models.OneToOneField(project)
    comment = models.OneToOneField(comment)
    news = models.OneToOneField(news)

    def __unicode__(self):
        return self.owner.surname

