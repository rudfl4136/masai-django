from django.db import models

class BlogKeyword(models.Model):
    thema = models.CharField(max_length=1000)
    category = models.CharField(max_length=1000)
    worked_date = models.DateTimeField('date published')

    def __str__(self):
        return self.thema + '/'+self.category + '/'+self.worked_date

class AiWorkedContent(models.Model):
    gubun = models.CharField(max_length=100)
    request_contents = models.CharField(max_length=2000)
    request_worked_date = models.DateTimeField('date published')
    response_contents = models.CharField(max_length=2000)

    def __str__(self):
        return self.gubun + '/'+self.request_contents + '/'+self.request_worked_date+ '/'+self.response_contents