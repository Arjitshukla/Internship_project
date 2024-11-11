from django.shortcuts import render
from ProjectNotes_app.models import Notes_Section,Project_Section
# Create your views here.

def project_list(request):
    allPosts = Project_Section.objects.all()
    context ={'allposts':allPosts}
    return render(request,"Projects/project.html",context)


def project_detail(request,slug):
    post = Project_Section.objects.filter(slug =slug)[0]
    context ={"post":post}
    return render(request,"Projects/project_detail.html",context)



# SOURCECODE OF TECHNOLOGIES
def notes_list(request):
    notes =Notes_Section.objects.all()
    context ={'notes':notes }
    return render(request,"Courses/Course_notes.html",context)