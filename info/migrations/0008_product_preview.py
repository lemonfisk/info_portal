# Generated by Django 4.2.3 on 2023-10-18 00:01

from django.db import migrations, models
import info.models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0007_auto_20231017_2341'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to=info.models.product_preview_directory_path),
        ),
    ]
