# Generated by Django 5.1.6 on 2025-02-27 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='contact_no',
            field=models.CharField(default='+63', max_length=13),
        ),
        migrations.AddField(
            model_name='customuser',
            name='middle_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
