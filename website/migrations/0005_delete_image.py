# Generated by Django 5.1.3 on 2025-01-02 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_image_remove_headerimage_created_at_gallery_title_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
    ]
