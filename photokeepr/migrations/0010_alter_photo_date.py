# Generated by Django 4.2.7 on 2023-12-04 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photokeepr', '0009_alter_people_related_photo_alter_people_related_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='date',
            field=models.DateField(null=True),
        ),
    ]