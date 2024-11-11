from django.db import models
from django.contrib.auth.models import User
from tinymce.widgets import TinyMCE
from django.contrib import admin
# Create your models here.

class Card_list(models.Model):
    cad_id =models.AutoField(primary_key=True)
    User =models.ForeignKey(User, on_delete=models.CASCADE,null=False) 
    title = models.CharField(max_length=200)  # Title of the card
    image = models.ImageField(upload_to='card_images/', blank=True, null=True)  # Optional image for card
    
    def __str__(self):
        return self.title


class Topic(models.Model):
    top_id =models.AutoField(primary_key=True)
    Chapter_title= models.CharField(max_length=200)  
    card_list = models.ForeignKey(Card_list, related_name='topics', on_delete=models.CASCADE)  # Foreignkey to Card


    
    def __str__(self):
        return self.Chapter_title


class TopicDetail(models.Model):
    top_detail_id =models.AutoField(primary_key=True)
    topic = models.OneToOneField(Topic, related_name='detail', on_delete=models.CASCADE)  # One-to-One relationship with Topic
    content = models.TextField(blank=True, null=True) 
    url = models.URLField(default="",max_length=250,blank=True, null=True)
    image = models.ImageField(upload_to='card_images/', blank=True, null=True) 
    t1 =models.CharField(max_length=50,blank=True, null=True)
    content_t1 = models.TextField(blank=True, null=True)
    code_t1 = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return f"Detail of {self.topic}"
 

class MCQ(models.Model):
    question = models.CharField(max_length=300)
    option_1 = models.CharField(max_length=100)
    option_2 = models.CharField(max_length=100)
    option_3 = models.CharField(max_length=100)
    option_4 = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=100)  # Store the correct answer
    topic_detail = models.ForeignKey(TopicDetail, related_name='mcqs', on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class FillInTheBlank(models.Model):
    question = models.CharField(max_length=300)  # Question with a blank
    answer = models.CharField(max_length=100)  # Correct answer
    topic_detail = models.ForeignKey(TopicDetail, related_name='fill_blanks', on_delete=models.CASCADE)

    def __str__(self):
        return self.question