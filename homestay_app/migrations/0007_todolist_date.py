# Generated by Django 5.1.1 on 2024-10-05 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homestay_app', '0006_repairlist_date_repairlist_date_added_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='date',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]