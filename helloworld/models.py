from django.db import models

class Blogs(models.Model):
    pub_date =models.DateTimeField('date published')
    author=models.CharField(max_length=100)
    title=models.CharField(max_length=200)
    summary=models.CharField(max_length=500)
    content=models.CharField(max_length=100000)
    def __unicode__(self):
        return self.title
