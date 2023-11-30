from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True, null=True)
    password = models.CharField()

    def __str__(self):
        return self.name
    
class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    date = models.DateField()
    photo_name = models.CharField(max_length=100, default='no names associated')
    preview_url = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='photos/')
    comment = models.TextField()
    

    def __str__(self):
        return self.photo_name
    
class People(models.Model):
    related_photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='related_photo')
    related_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='related_user', default=1)
    

    def __str__(self):
        return str(self.related_user.name)
    
