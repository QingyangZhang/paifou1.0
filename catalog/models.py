from django.db import models

from django.urls import reverse #Used to generate URLs by reversing the URL patterns

import uuid # Required for unique student instances

from django.contrib.auth.models import User

# Create your models here.
class Genre(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="")
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Customer(models.Model):
    """
    Model representing a Student
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_user')
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='photo', default="default/default.jpg",height_field=None, width_field=None, max_length=100)
    prefer1=models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True, related_name='customer_prefer1')
    prefer2=models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True, related_name='customer_prefer2')
    prefer3=models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True, related_name='customer_prefer3')
    contact=models.TextField(max_length=500, help_text="Enter a resume of student")
    credit=models.FloatField(help_text="Enter recruit Number")
    grade=models.IntegerField(help_text="Enter recruit Number")
    resume = models.TextField(max_length=1000, help_text="Enter a resume of student")
    
    def get_absolute_url(self):
        """
        Returns the url
        """
        return reverse('customer-detail', args=[str(self.id)])
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s' % (self.name)  
        
class Saler(models.Model):
    """
    Model representing a Student
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='saler_user')
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='photo', default="default/default.jpg",height_field=None, width_field=None, max_length=100)
    major1=models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True, related_name='saler_major1')
    major2=models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True, related_name='saler_major2')
    major3=models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True, related_name='saler_major3')
    contact=models.TextField(max_length=500, help_text="Enter a resume of student")
    credit=models.FloatField(help_text="Enter recruit Number")
    grade=models.IntegerField(help_text="Enter recruit Number")
    resume = models.TextField(max_length=1000, help_text="Enter a resume of student")
    
    def get_absolute_url(self):
        """
        Returns the url
        """
        return reverse('saler-detail', args=[str(self.id)])
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s' % (self.name)  
        
 
class Good(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="")
    saler=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    value=models.FloatField(help_text="")
    genre=models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True)
    photo=models.ImageField(upload_to='photo', default="default/default.jpg",height_field=None, width_field=None, max_length=100)
    timeRequire=models.IntegerField(help_text="")
    detail=models.TextField(max_length=500, help_text="Enter a resume of student")
    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s' % (self.name)  
    def get_absolute_url(self):
        """
        Returns the url
        """
        return reverse('good-detail', args=[str(self.id)])
    def get_genre_url(self):
        """
        Returns the url
        """
        return reverse('good-detail', args=[str(self.genre)])
    
 
class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="")
    customer=models.CharField(max_length=100)
    saler=models.CharField(max_length=100)
    good=models.CharField(default=None,max_length=100)
    sendTime=models.DateTimeField(null=True,blank=True)
    acceptTime=models.DateTimeField(null=True,blank=True)
    recvTime=models.DateTimeField(null=True,blank=True)
    cancelTime=models.DateTimeField(null=True,blank=True)
    def get_absolute_url(self):
        """
        Returns the url
        """
        return reverse('transaction-detail', args=[str(self.id)])
   
    