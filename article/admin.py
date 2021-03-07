from django.contrib import admin
from .models import Article


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["__str__", "date", "is_verified", "is_active"]
    list_editable = ["is_verified", "is_active"]

    class Meta:
        model = Article


admin.site.register(Article, ArticleAdmin)
