from django.contrib import admin

# Register your models here.
from .models import Coupons

@admin.register(Coupons)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['code','valid_from','valid_to','discounts','active']
    list_filter = ['active','valid_from','valid_to']
    search_fields = ['code']
    