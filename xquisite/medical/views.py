from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import MedicalRequest

class MedicalRequestCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    def test_func(self) -> bool | None:
        if not (self.request.user.is_superuser or self.request.user.is_staff):
            return True
        else:
            return False
        
    model = MedicalRequest
    fields = ['description', 'seat', 'phone']
    template_name_suffix = '_create'
    success_url = reverse_lazy('store:list')
    
    def form_valid(self, form, **kwargs):
        form.instance.User = self.request.user
        return super().form_valid(form)

class MedicalRequests(LoginRequiredMixin, UserPassesTestMixin, ListView):
    def test_func(self) -> bool | None:
        if self.request.user.is_superuser or self.request.user.is_staff:
            return True
        else:
            return False
    model = MedicalRequest

class MedicalRequestUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    def test_func(self) -> bool | None:
        if self.request.user.is_superuser or self.request.user.is_staff:
            return True
        else:
            return False
    model = MedicalRequest
    fields = '__all__'
    # fields = ['seat', 'requested_at', 'is_resolved']
    readonly_fields = ['User']
    template_name_suffix = '_update'
    success_url = reverse_lazy('medical:list')

class MyRequests(LoginRequiredMixin, UserPassesTestMixin, ListView):
    def test_func(self) -> bool | None:
        if not (self.request.user.is_superuser or self.request.user.is_staff):
            return True
        else:
            return False
    model = MedicalRequest
    template_name = 'medical/myrequests.html'
    
    def get_queryset(self):
        return get_list_or_404(MedicalRequest, User=self.request.user)