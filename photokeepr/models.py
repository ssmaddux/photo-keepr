from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100,  null=True)
    email = models.CharField(max_length=100,  null=True)
    phone = models.CharField(max_length=15,  null=True)
    password = models.CharField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users'  ,null=True)
    date = models.DateField(null=True)
    photo_name = models.CharField(max_length=100, default='no names associated',null=True)
    preview_url = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='photos/' ,null=True)
    comment = models.TextField(null=True)
    

    def __str__(self):
        return self.photo_name
    
class People(models.Model):
    related_photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='related_photo',null=True)
    related_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='related_user', default=1 ,null=True)
    
    

    def __str__(self):
        return str(self.related_user.name)
    

class Comment(models.Model):
    rel_photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='photo', null=True, blank=True)
    rel_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', null=True, blank=True)
    comment = models.TextField()

    def __str__(self):
        return self.comment
