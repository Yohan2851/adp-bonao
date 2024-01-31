from django.contrib import admin
from blog.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published', 'created_at', 'updated_at')
    list_filter = ('published', 'created_at', 'updated_at')
    search_fields = ('title', 'content', 'author__username')
    fields = (
          'title', 'content', 'image','published'
    )

    def save_model(self, request, obj, form, change):
        # Establece el autor del Post como el usuario autenticado
        obj.author = request.user
        super().save_model(request, obj, form, change)


