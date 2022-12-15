# Generated by Django 4.1.3 on 2022-12-04 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todoapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="date",
            field=models.DateField(default="1996-04-07"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="task", name="priority", field=models.IntegerField(),
        ),
    ]