from django.db import models
from django.contrib.auth.models import User
CONTENT_CHOICES=[
            ('None','None'),
            ('Like','Like'),
            ('View','View'),
            ('Click','Click'),
            ('Favourite','Favourite')
]

class MygUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    profile_pic = models.ImageField(upload_to='profile',blank=True, default='/media/profile/e2.png')
    mom = models.ForeignKey('self',on_delete=models.CASCADE, related_name="MOM", blank=True, null=True)
    dad = models.ForeignKey('self',on_delete=models.CASCADE, related_name="DAD", blank=True, null=True)
    sex=models.BooleanField(default=True)
    def __str__(self):
        return self.user.username

    def get_profile_picture(self):
        if self.profile_pic:
            return profile_pic_url
        else:
            return 'your_default_img_url_path'

class Sibling(models.Model):
    sibling1=models.ForeignKey(MygUser,on_delete=False,related_name="User")
    sibling2=models.ForeignKey(MygUser,on_delete=False,related_name="Sibling")
