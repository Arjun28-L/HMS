from django.db import models
# from django.contrib.auth.models import User
from Accounts.models import User

# Create your models here.

class ChatBot(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True
    )
    text_input = models.CharField(max_length=500)
    gemini_output = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return self.text_input