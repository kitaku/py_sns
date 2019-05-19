from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_owner')
    content = models.TextField(max_length=280)
    image = models.ImageField(upload_to = 'documents/', default='defo', null=True, blank=True)
    share_id = models.IntegerField(default= -1)
    good_count = models.IntegerField(default=0)
    share_count = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.content) + ' (' + str(self.owner) + ')'
    def get_share(self):
        return Message.objects.get(id=self.share_id)
    class Meta:
        ordering = ('-pub_date',)


class Friend(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name='friend_owner')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class Good(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='good_owner')
    message = models.ForeignKey(Message, on_delete=models.CASCADE)

    def __str__(self):
        return 'good for " ' + str(self.message) + ' " (by ' + str(self.owner) + ')'
