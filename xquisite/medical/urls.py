from django.urls import path
from .views import (
    MedicalRequestCreate,
    MedicalRequests,
    MedicalRequestUpdate,
)

app_name = 'medical'

urlpatterns = [
    path('', MedicalRequestCreate.as_view(), name='create'),
    path('requests/', MedicalRequests.as_view(), name='list'),
    path('requests/<int:pk>/update', MedicalRequestUpdate.as_view(), name='update'),
]