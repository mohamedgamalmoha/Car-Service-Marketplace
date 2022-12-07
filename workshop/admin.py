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


class ReportIssueInlineAdmin(admin.TabularInline):
    model = ReportIssue
    extra = 0
    min_num = 0
    max_num = 0
    can_delete = False
    fields = ('customer', 'title', 'description',  'suggestion', 'date_of_issue', 'attachment')
    readonly_fields = ('customer', 'title', 'description',  'suggestion', 'date_of_issue', 'attachment')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'service_type', 'created', 'updated')
    list_filter = ('service_type', )
    search_fields = ('name', )


class WorkShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'avg_rate', 'count_rate', 'count_comment', 'count_reports', 'created', 'updated')
    inlines = (
        RateInlineAdmin,
        CommentInlineAdmin,
        ReportIssueInlineAdmin
    )
    readonly_fields = ('show_image', 'avg_rate', 'count_rate', 'count_comment', 'count_reports')
    fieldsets = (
        ('Main Info', {"fields": ('name', 'description', ('phone_number', 'whatsapp'), 'brands', 'services', 'map_link')}),
        ('Image', {"fields": ("image", "show_image")}),
        ('Statistics', {"fields": ('avg_rate', 'count_rate', 'count_comment', 'count_reports')}),
    )
    list_filter = ('brands', 'services')
    search_fields = ('name', 'description')


class ReportIssueAdmin(admin.ModelAdmin):
    list_display = ('customer', 'workshop', 'title', 'date_of_issue', 'created', 'updated')
    search_fields = ('title', 'customer__first_name', 'customer__last_name')


admin.site.register(Service, ServiceAdmin)
admin.site.register(WorkShop, WorkShopAdmin)
admin.site.register(ReportIssue, ReportIssueAdmin)
