# Generated by Django 3.2.2 on 2021-05-20 10:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_blog_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]