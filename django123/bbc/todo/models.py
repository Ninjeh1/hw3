from django.db import models
from datetime import datetime

class Article(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=999)
    views = models.IntegerField(db_default=0)
    is_published = models.BooleanField(default=True)
    create_date = models.DateField(default=datetime.today)