from django.contrib import admin
from .models import Booking  # 必要なモデルのみをインポート

# 必要に応じてモデルを管理サイトに登録
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'first_name', 'last_name', 'cat_name', 'breed', 'color',
        'gender', 'date',  
    ]
    list_filter = ['breed', 'gender']
    search_fields = ['user__username', 'cat_name']
    date_hierarchy = 'date'