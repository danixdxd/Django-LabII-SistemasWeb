"""mongo_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from student import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/get', views.get_student, name='get_student'),
    path('student/delete', views.delete_student, name='delete_student'),
    path('student/put', views.put_student, name='put_student'),
    path('student/post', views.post_student, name='post_student'),
]
