# Generated by Django 5.1.1 on 2024-10-05 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homestay_app', '0003_alter_todolist_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComplainList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complain_item', models.CharField(blank=True, max_length=200, null=True)),
                ('remark', models.CharField(blank=True, max_length=200, null=True)),
                ('unit', models.CharField(blank=True, max_length=30, null=True)),
                ('status', models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Done', 'Done')], max_length=30, null=True)),
                ('date', models.CharField(blank=True, max_length=200, null=True)),
                ('reported_by', models.CharField(blank=True, max_length=200, null=True)),
                ('urgency', models.CharField(blank=True, choices=[('5-Extreme', '5-Extreme'), ('4-Very', '4-Very'), ('3-Normal', '3-Normal'), ('2-Less', '2-Less'), ('1-Not', '1-Not')], max_length=30, null=True)),
                ('importance', models.CharField(blank=True, choices=[('5-Extreme', '5-Extreme'), ('4-Very', '4-Very'), ('3-Normal', '3-Normal'), ('2-Less', '2-Less'), ('1-Not', '1-Not')], max_length=30, null=True)),
                ('channel', models.CharField(blank=True, max_length=200, null=True)),
                ('outcome', models.CharField(blank=True, max_length=200, null=True)),
                ('date_added', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
