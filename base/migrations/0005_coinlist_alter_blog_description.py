# Generated by Django 4.0.6 on 2022-07-21 04:02

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_blog_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coinlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
