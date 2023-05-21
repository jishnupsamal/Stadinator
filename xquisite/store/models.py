from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError

def validate_phone(value):
    if len(str(value)) != 12:
        raise ValidationError(
            ("%(value)s is not a valid phone number number"),
            params={"value": value},
        )

class Product(models.Model):
    image = models.ImageField('Product Thumbnail', upload_to='uploads/store', blank=True)
    item_code = models.CharField("Item Code", unique=True, max_length=50)
    name = models.CharField('Product Name', unique=True, max_length=100)
    slug = models.SlugField("Product Slug", unique=True, blank=True)
    description = models.TextField('Description')
    price = models.FloatField("Price")
    in_stock = models.BooleanField("Available in Stock", default=True)
    date_added = models.DateTimeField('Date Added', auto_now_add=True)
    date_updated = models.DateTimeField('Last Updated', auto_now=True)
    
    def __str__(self):
       return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.item_code = self.item_code.upper()
        super(Product, self).save(*args, **kwargs)

class Order(models.Model):
    User = models.ForeignKey("accounts.User", on_delete=models.CASCADE, limit_choices_to={"is_staff": False},)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE, to_field='name', limit_choices_to={"in_stock": True})
    seat = models.CharField("Seat Number", max_length=10)
    phone = models.IntegerField('Phone Number', help_text='Phone Number alongwith Country Code', validators=[validate_phone])
    ordered_at = models.DateTimeField('Ordered at', auto_now_add=True)
    delivered = models.BooleanField('Delivered', default=False)
    
    
