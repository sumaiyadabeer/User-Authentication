from django.contrib.auth.models import Permission, User
from django.db import models


class Images(models.Model):
    
    username = models.CharField(max_length=250)
    tagg = models.CharField(max_length=500)
    ans = models.CharField(max_length=50)
    pass_img = models.FileField()
    optical_img = models.FileField()
    other_img1 = models.FileField()
    other_img2 = models.FileField()
    other_img3 = models.FileField()
    other_img4 = models.FileField()
    other_img5 = models.FileField()
    other_img6 = models.FileField()
    other_img7 = models.FileField()
    other_img8 = models.FileField()
    
    def __str__(self):
        return self.username + ' - ' + self.tagg 
