from django.db import models

# Create your models here.

class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)


class User(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    house_name = models.CharField(max_length=100)
    post_name = models.CharField(max_length=100)
    landmark=models.CharField(max_length=100)
    street_name=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.BigIntegerField()
    image = models.CharField(max_length=400)
    gender=models.CharField(max_length=10)

class Category(models.Model):
    category_name=models.CharField(max_length=100)


class Tvshow(models.Model):
    name=models.CharField(max_length=100)
    CATEGORY=models.ForeignKey(Category,on_delete=models.CASCADE)
    from_time=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    language=models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    demo_video=models.CharField(max_length=800)
    image=models.CharField(max_length=500)
    Date=models.DateField(max_length=100)
    channelname=models.CharField(max_length=100)
    actors_name=models.CharField(max_length=100)
    actress_name=models.CharField(max_length=100)
    producer_name=models.CharField(max_length=100)
    director_name=models.CharField(max_length=100)




class Review(models.Model):
    TVSHOW=models.ForeignKey(Tvshow,on_delete=models.CASCADE)
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField()
    review=models.CharField(max_length=100)
    score=models.FloatField(default=0.0)


class Complaint(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField()
    complaint=models.CharField(max_length=500)
    status=models.CharField(max_length=100,default='pending')
    reply=models.CharField(max_length=100,default='pending')