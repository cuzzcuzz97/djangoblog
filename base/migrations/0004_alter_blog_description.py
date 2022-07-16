# Generated by Django 4.0.6 on 2022-07-14 12:21

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_blog_options_alter_blog_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=tinymce.models.HTMLField(blank=True, max_length=1000000, null=True),
        ),
    ]