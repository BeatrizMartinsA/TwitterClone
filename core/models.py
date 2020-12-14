from django.db import models
from django.contrib.auth.models import User
from commons.utils import gravatar_url


class ActivityLog(models.Model):
    type = models.CharField(max_length=64)
    logged_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    fromuser = models.ForeignKey(User, null=True, blank=True, related_name="activitylogs_withfromuser", on_delete=models.SET_NULL)
    jsondata = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return '%s / %s / %s' % (
            self.type,
            self.logged_user,
            self.created_at,
        )


class Seguindo(models.Model):
    de = models.ForeignKey(User, related_name='seguindo_de', null=True, on_delete=models.SET_NULL)
    para = models.ForeignKey(User, related_name='seguindo_para', null=True, on_delete=models.SET_NULL)

    class Meta:
        unique_together = ('de', 'para')


class Tweet(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    text = models.CharField(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)

    def to_dict_json(self):
        return {
            'avatar': gravatar_url(self.user.email),
            'author_name': self.user.first_name,
            'author_username': self.user.username,
            'created_at': self.created_at.isoformat(),
            'text': self.text,
        }
