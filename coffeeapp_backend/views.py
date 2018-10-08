from django.http import JsonResponse

from .models import Cafe, Badge, CafeBadgeAssociation

from django.db import connection, reset_queries


def coffee_api(request):
    reset_queries()
    cafes = []
    cafes_by_id = {}
    for cafe in Cafe.objects.all():
        cafe_dict = {"name": cafe.name, "badge_associations": []}
        cafes.append(cafe_dict)
        cafes_by_id[cafe.id] = cafe_dict
        if cafe.description:
            cafe_dict["description"] = cafe.description
        if cafe.photo:
            cafe_dict["photo"] = cafe.photo.url
        if cafe.lat:
            cafe_dict["location"] = {"lat": float(cafe.lat), "lng": float(cafe.lon)}
            if cafe.address_string:
                cafe_dict["location"]["address"] = cafe.address_string
    for association in CafeBadgeAssociation.objects.all():
        cafes_by_id[association.cafe_id]["badge_associations"].append(
            [association.products, association.badge_id]
        )
    badges = {}
    for badge in Badge.objects.all():
        badges[badge.id] = {}
        badges[badge.id]["name"] = badge.name
        badges[badge.id]["checklist"] = badge.checklist.split("\n")
    print(connection.queries)
    return JsonResponse({"cafes": cafes, "badges": badges})
