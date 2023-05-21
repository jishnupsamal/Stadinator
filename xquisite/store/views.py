from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Product, Order

class ProductCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    def test_func(self) -> bool | None:
        if self.request.user.is_superuser or self.request.user.is_staff:
            return True
    
    model = Product
    fields = '__all__'
    template_name_suffix = '_create'
    
    def get_success_url(self) -> str:
        return reverse_lazy('store:detail', kwargs={'slug': self.object.slug})

class ProductList(LoginRequiredMixin, ListView):
    model = Product
    paginate_by = 25
    
class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    
class ProductUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    def test_func(self) -> bool | None:
        if self.request.user.is_superuser or self.request.user.is_staff:
            return True
    
    model = Product
    fields = '__all__'
    template_name_suffix = '_update'
    
    def get_success_url(self) -> str:
        return reverse_lazy('store:detail', kwargs={'slug': self.object.slug})
    
class ProductDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    def test_func(self) -> bool | None:
        if self.request.user.is_superuser or self.request.user.is_staff:
            return True
    
    model = Product
    success_url = reverse_lazy('store:list')
    template_name_suffix = '_delete'

class OrderCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    def test_func(self) -> bool | None:
        if not (self.request.user.is_superuser or not self.request.user.is_staff):
            return True
        else:
            return False
        
    model = Order
    fields = ['seat', 'phone']
    template_name_suffix = '_create'
    success_url = reverse_lazy('store:list')
    
    def form_valid(self, form, **kwargs):
        obj = get_object_or_404(Product, slug=self.kwargs['slug'])
        form.instance.User = self.request.user
        form.instance.Product = obj
        return super().form_valid(form)

# Orders

class Orders(LoginRequiredMixin, UserPassesTestMixin, ListView):
    def test_func(self) -> bool | None:
        if self.request.user.is_superuser or self.request.user.is_staff:
            return True
        else:
            return False
    model = Order

class OrdersUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    def test_func(self) -> bool | None:
        if self.request.user.is_superuser or self.request.user.is_staff:
            return True
        else:
            return False
    model = Order
    fields = '__all__'
    template_name_suffix = '_update'
    success_url = reverse_lazy('store:list_orders')
    
class MyOrders(LoginRequiredMixin, UserPassesTestMixin, ListView):
    def test_func(self) -> bool | None:
        if not (self.request.user.is_superuser or self.request.user.is_staff):
            return True
        else:
            return False
    model = Order
    template_name = 'store/order_list.html'
    
    def get_queryset(self):
        return get_list_or_404(Order, User=self.request.user)
    
    