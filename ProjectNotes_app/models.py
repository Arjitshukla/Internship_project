from django.db import models
from Course_app.models import Card_list
from django.contrib.auth.models import User

# Create your models here.
class Notes_Section(models.Model):
    sno =models.AutoField(primary_key=True)
    tech_title =models.ForeignKey(Card_list, on_delete=models.CASCADE,null=False ,verbose_name='Technology Name')
    tech_Notes_pdf = models.FileField(upload_to='Course_documents/Notes')
    tech_Cheatsheet_pdf = models.FileField(upload_to='Course_documents/Cheatsheet')
    Card_image = models.ImageField(upload_to="Course_documents/images",blank=True, null=False)

    class Meta:
        verbose_name = ' Course SourceCode'  # This is the human-readable singular name
        verbose_name_plural = 'Course SourceCodes'  # This is the plural name

    def __str__(self):
        return f"Scource code of {self.tech_title }"



class Project_Section(models.Model):
    sno =models.AutoField(primary_key=True)
    category = models.CharField(max_length=50,verbose_name='Category of Projects')
    slug = models.CharField(max_length=150,verbose_name='Url - Name')
    Publisher_name =models.ForeignKey(User,on_delete=models.CASCADE,null=False,verbose_name='Teacher Name')
    Project_name =models.CharField(max_length=80)
    created_at =  models.DateTimeField(blank=True,verbose_name='Project Created Date') 
    project_image = models.ImageField(upload_to="Project_documents/images",blank=True, null=False)
    headline_1 =models.CharField(max_length=80,null=True,default=None)
    Project_content_1 =models.TextField(null=True,default=None)
    Project_Code_1 =models.CharField(max_length=80,null=True,default=None)
    headline_2 =models.CharField(max_length=80,null=True,default=None)
    Project_content_2 =models.TextField(null=True,default=None)
    Project_Code_2 =models.CharField(max_length=80,null=True,default=None)
    headline_3 =models.CharField(max_length=80,null=True,default=None)
    Project_content_3 =models.TextField(null=True,default=None)
    Project_Code_3 =models.CharField(max_length=80,null=True,default=None)



    class Meta:
        verbose_name = 'All kind of Project'  # This is the human-readable singular name
        verbose_name_plural = 'All kind of Projects'  # This is the plural name

    def __str__(self):
        return  self.Project_name


