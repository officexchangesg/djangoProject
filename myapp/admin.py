from django.contrib import admin
from .models import Post

#admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "body"]
    list_filter = ["status", "author"]
    search_fields = ["title","body"]
    prepopulated_fields = {"slug": ("title","author")}
    raw_id_fields = ["author"]
    date_hierarchy = "publish"
    ordering = ["status","publish"]
# Register your models here.
