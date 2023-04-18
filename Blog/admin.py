from django.contrib import admin
from Blog.models import Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "publish", "status"]
    list_editable = ["status"]
    list_filter = ["status", "publish", "created", "author"]
    ordering = ["title", "publish"]
    search_fields = ["title", "description"]
    raw_id_fields = ["author"]
    date_hierarchy = "publish"
    prepopulated_fields = {
        "slug": ["title"]
    }
