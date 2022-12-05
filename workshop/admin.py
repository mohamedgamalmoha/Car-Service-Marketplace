from django.contrib import admin

from .models import Service, WorkShop, Rate, Comment, ReportIssue


class RateInlineAdmin(admin.TabularInline):
    model = Rate
    extra = 0
    min_num = 0
    max_num = 0
    can_delete = False
    fields = ('customer', 'value', 'created', 'updated')
    readonly_fields = ('customer', 'value', 'created', 'updated')


class CommentInlineAdmin(admin.TabularInline):
    model = Comment
    extra = 0
    min_num = 0
    max_num = 0
    can_delete = False
    fields = ('customer', 'title', 'comment',  'created', 'updated')
    readonly_fields = ('customer', 'created', 'updated')


class WorkShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'avg_rate', 'count_rate', 'count_comment', 'count_reports', 'created', 'updated')
    inlines = (
        RateInlineAdmin,
        CommentInlineAdmin
    )


class ReportIssueAdmin(admin.ModelAdmin):
    list_display = ('customer', 'workshop', 'title', 'date_of_issue', 'created', 'updated')


admin.site.register(Service)
admin.site.register(WorkShop, WorkShopAdmin)
admin.site.register(ReportIssue, ReportIssueAdmin)
