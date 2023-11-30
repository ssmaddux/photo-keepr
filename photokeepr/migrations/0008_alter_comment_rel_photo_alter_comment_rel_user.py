# Generated by Django 4.2.7 on 2023-11-30 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photokeepr', '0007_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rel_photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photo', to='photokeepr.photo'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='rel_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='photokeepr.user'),
        ),
    ]