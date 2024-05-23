# Generated by Django 4.2.11 on 2024-05-22 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("repairs", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="repair", name="title",),
        migrations.AddField(
            model_name="repair",
            name="category",
            field=models.CharField(
                choices=[
                    ("廁所", "廁所"),
                    ("馬桶", "馬桶"),
                    ("電器", "電器"),
                    ("教室", "教室"),
                    ("宿舍", "宿舍"),
                    ("其他", "其他"),
                ],
                default=" ",
                max_length=100,
            ),
        ),
    ]