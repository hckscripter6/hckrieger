# Generated by Django 3.0.2 on 2020-03-16 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0004_auto_20200312_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='organization',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
