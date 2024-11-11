"""
URL configuration for Teqpeers_Technology project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

# for Media 👇
from django.conf import settings
from django.conf.urls.static import static



admin.site.site_header ="👉 TEQPEERS LEARNING TECHNOLOGY ❤️"
admin.site.site_title ="TEQPEERS LEARNING TECHNOLOGY LEARNING Admin Panel"
admin.site.index_title ="Welcome to `TEQPEERS LEARNING TECHNOLOGY ' 🙏"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', include('Home_app.urls')) ,  #home_app_page
    path('course/', include('Course_app.urls')),   #Course_app_page
    path('blogs/', include('Blog_app.urls')),   #blog_app_page
    path('course-items/', include('ProjectNotes_app.urls')),   #blog_app_page
    path('user/', include('Authenticate.urls')),   #Authenticate_page
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
