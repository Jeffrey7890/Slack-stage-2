from django.db import models
from django.urls import reverse

class Resume(models.Model):
    full_name = models.CharField(max_length = 100)
    email = models.EmailField()
    phone = models.CharField(max_length = 30)
    address = models.TextField()
    skills = models.CharField(max_length = 500)
    degree = models.CharField(max_length = 200)
    school = models.CharField(max_length = 200)
    accomplishments = models.CharField(max_length = 200, null = True, blank = True, help_text = 'Optional')

    def get_absolute_url(self):
        return reverse('resume:detials', kwargs = {'pk':self.pk})

    def skill_split(self):
        return self.skills.split(',')

    def __str__(self):
        return self.full_name


    