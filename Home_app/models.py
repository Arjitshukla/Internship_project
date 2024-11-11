from django.db import models

# Create your models here.
class ContactMessage(models.Model):
    sno =models.AutoField(primary_key=True)
    Name =models.CharField(max_length=50)
    Phone =models.CharField(max_length=13)
    Email =models.CharField(max_length=100)
    Content =models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True,blank=True)
    
    def __str__(self):
        return "Message from " + self.Name 

# About Section

class About_Section(models.Model):
    sno =models.AutoField(primary_key=True)
    about_title =models.CharField(max_length=50)
    Short_content =models.TextField()
    heading_line = models.CharField(max_length=50)
    content1 =models.TextField()
    content2 =models.TextField()
    class Meta:
        verbose_name = 'About TEQPEERS TECHNOLOGY'  # This is the human-readable singular name
        verbose_name_plural = 'About TEQPEERS TECHNOLOGIES'  # This is the plural name
    def __str__(self):
        return   self. about_title

