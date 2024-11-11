# Generated by Django 5.0.7 on 2024-11-09 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_blogexitpost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogexitpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/exit_a_business/'),
        ),
        migrations.AlterField(
            model_name='blogrunpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/run_a_business/'),
        ),
        migrations.AlterField(
            model_name='blogstartpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/start_a_business/'),
        ),
    ]
