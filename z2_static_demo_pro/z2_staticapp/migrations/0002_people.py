# Generated by Django 4.1.3 on 2022-11-16 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("z2_staticapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="People",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("img", models.ImageField(upload_to="pics1")),
                ("name", models.CharField(max_length=250)),
                ("desc", models.TextField()),
            ],
        ),
    ]
