from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django import forms


#ADMIN = 0
#BUSINESS = 1
#STUDENT = 2
#TOURIST = 3

class UserProfile(models.Model):

######################## User Type ##########
    '''user_choices = [(0, 'Admin'),
            (1, 'Business'),
            (2, 'Student'),
            (3, 'Tourist'),
            ]
    # Link UserProfile to User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add attributes to the user model

    user_type = models.CharField(max_length = 50,
                                 choices = user_choices,
                               #  default = '2Business',
                                 blank = False,default='Admin')
'''

    # Link UserProfile to User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    EXP =((1,1),(2,2),(3,3),(4,4),(5,5))
    experience = models.CharField(max_length=1,choices=EXP,default='Fresher',blank=False)

    first_name = models.CharField(max_length=20,default='Name')
    last_name = models.CharField(max_length=20,default='Last name')

    Field=(("Engineer", "Engineer"),("Doctor","Doctor"),("Artist","Artist"),("Photographer","Photographer"))
    profession=models.CharField(choices=Field,default="Engineer",blank=False,max_length=10)

def __str__(self):
        return self.user.username

@receiver(post_save, sender = User)
def create_user_profile( sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user = instance)
    instance.userprofile.save()