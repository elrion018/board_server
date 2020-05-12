from django.db import models

class Article(models.Model):
    slug = models.AutoField(primary_key=True, help_text='PK AutoIncrement')
    title = models.CharField(max_length=300, blank=False, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(blank=False, null =True)
    recommended = models.IntegerField(blank=False, null=True)
    