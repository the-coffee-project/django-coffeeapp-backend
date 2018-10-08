from django.db import models
from django.template.defaultfilters import truncatechars


class Badge(models.Model):
    name = models.CharField(max_length=80)
    checklist = models.TextField(blank=True)
    # TODO: color?

    internal_notes = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def admin_checklist(self):
        return truncatechars(", ".join(self.checklist.split("\n")), 100)

    admin_checklist.short_description = "Checklist"


class Cafe(models.Model):
    name = models.CharField(max_length=80)
    photo = models.ImageField(upload_to="cafes", blank=True)
    description = models.TextField(blank=True)

    # TODO consider using GeoDjango for locations
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    address_string = models.CharField(max_length=240)
    address_string.short_description = "Address"

    badges = models.ManyToManyField(Badge, through="CafeBadgeAssociation")

    internal_notes = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def admin_badge_list(self):
        return ", ".join([str(badge) for badge in self.badges.all()])

    admin_badge_list.short_description = "Badges"


class CafeBadgeAssociation(models.Model):
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    products = models.CharField(max_length=80, blank=True)

    def __str__(self):
        result = self.cafe.name + " - " + self.badge.name
        if self.products:
            result += " (" + self.products + ")"
        return result
