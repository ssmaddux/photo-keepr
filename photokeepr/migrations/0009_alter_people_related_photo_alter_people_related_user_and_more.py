# Generated by Django 4.2.7 on 2023-12-04 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photokeepr', '0008_alter_comment_rel_photo_alter_comment_rel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='related_photo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_photo', to='photokeepr.photo'),
        ),
        migrations.AlterField(
            model_name='people',
            name='related_user',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_user', to='photokeepr.user'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='comment',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(null=True, upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo_name',
            field=models.CharField(default='no names associated', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='photokeepr.user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
    ]