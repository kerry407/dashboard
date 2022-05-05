
from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,blank=True, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(blank=True, null=True,max_length=20)
    last_name = models.CharField(blank=True, null=True, max_length=20)

    def __str__(self):
        return self.user.username

    @property
    def username(self):
        if self.user_id is not None:
            return self.user.first_name + '' + self.user.last_name + '[' + self.user.username + ']'
    
    @property
    def email(self):
        if self.user_id is not None:
            return (self.user.email)

    class Meta:
        db_table = 'userprofile'
        managed = True
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'