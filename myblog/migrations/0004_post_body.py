# Generated by Django 4.1 on 2022-09-04 12:12

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0003_remove_post_body_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body',
            field=ckeditor.fields.RichTextField(default=''),
        ),
    ]
