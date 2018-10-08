from django.contrib import admin

from .models import Cafe, Badge, CafeBadgeAssociation


class CafeBadgeAssociationInline(admin.TabularInline):
    model = CafeBadgeAssociation
    verbose_name = "Badge"
    verbose_name_plural = "Badges"
    extra = 0


class CafeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["name", "photo", "description"]}),
        ("Location information", {"fields": ["lat", "lon", "address_string"]}),
        ("Internal information (not published)", {"fields": ["internal_notes"]}),
    ]
    inlines = [CafeBadgeAssociationInline]
    list_display = ("name", "address_string", "admin_badge_list")
    list_filter = ("badges",)


class BadgeAdmin(admin.ModelAdmin):
    list_display = ("name", "admin_checklist")


admin.site.register(Cafe, CafeAdmin)
admin.site.register(Badge, BadgeAdmin)
