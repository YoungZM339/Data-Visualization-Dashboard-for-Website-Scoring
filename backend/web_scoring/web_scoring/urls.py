"""
URL configuration for web_scoring project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/

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
from django.conf.urls.static import static
from algorithms.views import ProcessFilesAPIView, GetProcessedDataAPIView, TaskViewSet
from users.views import JWTTokenObtainPairView, UserViewSet
from rest_framework import routers

from web_scoring import settings

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', JWTTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('algorithms/process-files/', ProcessFilesAPIView.as_view(), name='process_files'),
    path('algorithms/get-processed-data/', GetProcessedDataAPIView.as_view(), name='get_processed_data'),
    path('', include(router.urls))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
