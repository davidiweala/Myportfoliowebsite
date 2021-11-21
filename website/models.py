from django.db import models

class AboutMe(models.Model):
    image = models.ImageField(upload_to='images/', editable=True, blank=True)
    name = models.CharField(max_length=250, default='David Iweala', verbose_name='name')
    date_of_birth = models.DateField(blank=True)
    address = models.CharField(max_length=250, default='Lagos, Nigeria', verbose_name='address')
    email = models.EmailField(default='iwealadavid@gmail.com')
    phone = models.TextField(default='(+234) 9061341499')
    no_of_projects = models.IntegerField(blank=True)
    resume = models.FileField(upload_to='media', blank=True)
    bg_photo = models.ImageField(upload_to='images/', blank=True)
    project_bg = models.ImageField(upload_to='images/', blank=True)
    customers = models.IntegerField(default='1', blank=True)

    def __str__(self):
        return self.name

class Skill(models.Model):
    title = models.CharField(max_length=250, verbose_name='skillset', blank=True)
    percentage = models.IntegerField(default='10')

    def __str__(self):
        return self.title

class Projects(models.Model):
    title = models.CharField(max_length=250, verbose_name='title', blank=True)
    link = models.URLField(blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    work_done = models.TextField(blank=True)

    def __str__(self):
        return self.title


class ProjectsPage(models.Model):
    title = models.CharField(max_length=250, verbose_name='title', blank=True)
    link = models.URLField(blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    work_done = models.TextField(blank=True)

    def __str__(self):
        return self.title
