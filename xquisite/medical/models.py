from django.db import models
from django.contrib.auth import get_user_model
from store.models import validate_phone

class MedicalRequest(models.Model):
    User = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, limit_choices_to={'is_staff': False})
    description = models.TextField('Medical Emergency Despription')
    phone = models.IntegerField("Phone Number", help_text='Phone Number alongwith Country Code', validators=[validate_phone])
    seat = models.CharField('Seat Number', max_length=50)
    is_resolved = models.BooleanField("Resolved", default=False)
    requested_at = models.DateTimeField("Requested at", auto_now_add=True)
