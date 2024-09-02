from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    display_name = models.CharField(max_length=200, db_index=True, unique=True, default='Unassigned', help_text='Required. Unique name that will be publicly associated with your comments')
    # add additional fields in here
    
    class Meta:
        app_label = "user_profile"
        db_table = u'"django_data\".\"user_profile__user_profile"'
        ordering = ['username']


    def __str__(self):
        return self.display_name
