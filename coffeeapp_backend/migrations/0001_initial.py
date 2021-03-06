# Generated by Django 2.0.8 on 2018-09-30 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Badge",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=80)),
                ("checklist", models.TextField(blank=True)),
                ("internal_notes", models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="Cafe",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=80)),
                ("photo", models.ImageField(blank=True, upload_to="cafes")),
                ("description", models.TextField(blank=True)),
                ("lat", models.DecimalField(decimal_places=6, max_digits=9)),
                ("lon", models.DecimalField(decimal_places=6, max_digits=9)),
                ("address_string", models.CharField(max_length=240)),
                ("internal_notes", models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="CafeBadgeAssociation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("products", models.CharField(blank=True, max_length=80)),
                (
                    "badge",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="coffeeapp_backend.Badge",
                    ),
                ),
                (
                    "cafe",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="coffeeapp_backend.Cafe",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="cafe",
            name="badges",
            field=models.ManyToManyField(
                through="coffeeapp_backend.CafeBadgeAssociation",
                to="coffeeapp_backend.Badge",
            ),
        ),
    ]
