from django.urls import path
from . import views

urlpatterns = [
    path('device/<int:pk>/backups/', views.device_backup_view, name='device_backup'),
]
