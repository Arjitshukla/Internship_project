from django.shortcuts import render
from .models import ContactMessage,About_Section
from django.contrib import messages

# Create your views here.

def Home(request):
    return render (request,"Mainfile/index.html")

def About(request):
    alltext = About_Section.objects.all()
    context ={ "alltext":alltext }
    return render (request,"Mainfile/about.html",context)

def Contact(request):
   if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']

        # Validation logic

        if len(name) < 3 or len(email) < 3 or len(phone) < 10 or not phone.isdigit() or len(content) < 5:
            messages.error(request, "Kindly complete the form with accurate information.")
        else:
            # Match field names from the model (Email and Content are capitalized)
            contact_instance =  ContactMessage(Name=name, Email=email, Phone=phone, Content=content)
            contact_instance.save()
            messages.success(request, "Your message has been received. Thank you for contacting us!")
            

   return render (request,"Mainfile/contact.html")