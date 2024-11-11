from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    sno = models.AutoField(primary_key=True)
    slug = models.SlugField(unique=True, max_length=200)
    title = models.CharField(max_length=100, null=False)
    blog_card_img = models.ImageField(upload_to="blog/images", blank=True, null=False)
    content = models.TextField(null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    
    # Auto timestamps
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    updated_at = models.DateTimeField(auto_now=True)  # Automatically updated on save
    
    image = models.ImageField(upload_to="blog/images", blank=True, null=False)
    heading_1 = models.CharField(max_length=50)
    para_1 = models.TextField()
    heading_2 = models.CharField(max_length=50)
    para_2 = models.TextField()
    heading_3 = models.CharField(max_length=50)
    para_3 = models.TextField()
    heading_4 = models.CharField(max_length=50)
    para_4 = models.TextField()
    heading_5 = models.CharField(max_length=50)
    para_5 = models.TextField()
    heading_6 = models.CharField(max_length=50)
    para_6 = models.TextField()

    # Fixed duplicate field name issue
    para_7 = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
