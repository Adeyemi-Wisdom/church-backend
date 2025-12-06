"""
URL configuration for church project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

def home(request):
    return HttpResponse("API is Live 🚀")

# def temp_create_admin(request):
#     if not User.objects.filter(username="admin").exists():
#         User.objects.create_superuser(
#             username="admin",
#             email="admin@test.com",
#             password="Admin12345"
#         )
#         return HttpResponse("Admin created again ✅")
#     else:
#         return HttpResponse("Admin already exists ✅")

urlpatterns = [
    # path("create-admin/", temp_create_admin),
    path("", home),
    path("admin/", admin.site.urls),
    path("users/", include("user_app.api.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += static(
#     settings.MEDIA_URL,
#     document_root=settings.MEDIA_ROOT
# )

# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('users/', include('user_app.api.urls'))
# ]
