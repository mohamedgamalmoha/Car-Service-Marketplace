from django.contrib import admin

from .models import Post, PostComment


class PostCommentInlineAdmin(admin.TabularInline):
    model = PostComment
    extra = 0
    min_num = 0
    max_num = 0
    fields = ('customer', 'title', 'comment', 'created', 'updated')
    readonly_fields = ('customer', 'title', 'comment', 'created', 'updated')


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created', 'updated')
    search_fields = ('title', 'body')
    list_filter = ('is_active', 'created', 'updated')
    inlines = [PostCommentInlineAdmin]
    readonly_fields = ('show_image', )
    fieldsets = (
        (None, {"fields": ('title', 'body', 'image', 'show_image', 'is_active')}),
    )

    class Media:
        css = {
             'all': ('css/admin.css',)
        }


admin.site.register(Post, PostAdmin)
