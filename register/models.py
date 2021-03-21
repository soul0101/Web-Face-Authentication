from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
def my_default():
    return {'foo': 'bar'}

class UserProfile(models.Model):
    user = models.OneToOneField(User,related_name = "user_profile", on_delete=models.CASCADE, primary_key=True, null = False)
    face_data = models.JSONField(default = my_default)
    


    @property
    def username(self):
        return self.user.username
 
    # Methods
 
    # Meta and String
    class Meta:
        verbose_name = ("Profile")
        verbose_name_plural = ("Profiles")
        ordering = ("user",)
 
    def __str__(self):
        return self.user.username



#  class SignUp(models.Model):
#     name = models.CharField(max_length=122, default="Some name")
#     email = models.CharField(max_length=122)
#     password = models.CharField(max_length=12)

#     def __str__(self):
#         return self.name

# class Face(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     input_face = models.CharField(max_length = 70)
    
    
