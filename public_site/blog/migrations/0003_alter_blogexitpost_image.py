# Generated by Django 5.0.7 on 2024-11-09 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogexittag_blogruntag_blogexitpost_blogrunpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogexitpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/start_a_business/'),
        ),
    ]
