# Generated by Django 4.2.12 on 2024-10-24 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_tag_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]