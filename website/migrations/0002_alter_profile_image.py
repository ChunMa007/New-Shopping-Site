# Generated by Django 5.1.7 on 2025-04-06 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='media/item_images/item_default.webp', upload_to='media/item_images'),
        ),
    ]
