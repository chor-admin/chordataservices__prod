# Generated by Django 5.0.7 on 2024-11-09 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blogexitpost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogexitpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='staticfiles/graphics/start_a_business'),
        ),
    ]