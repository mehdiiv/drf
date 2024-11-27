from django.db import models


class User(models.Model):
    email = models.CharField(max_length=128, blank=False, null=False)
    json_web_token = models.CharField(max_length=1024, blank=False, null=False)

    class Meta:
        db_table = "users"


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=512)
    body = models.TextField(max_length=2048)

    class Meta:
        db_table = 'messages'