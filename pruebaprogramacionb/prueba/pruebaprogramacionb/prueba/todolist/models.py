from django.db import models
from django.conf import settings

class ToDo(models.Model):
    action_text = models.CharField(max_length = 120)
    post_date = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
