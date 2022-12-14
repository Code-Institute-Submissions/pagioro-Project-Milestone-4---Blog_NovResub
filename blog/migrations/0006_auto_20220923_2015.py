# Generated by Django 3.2.15 on 2022-09-23 20:15

from django.db import migrations
import django_summernote.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20220920_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=django_summernote.fields.SummernoteTextField(),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=django_summernote.fields.SummernoteTextField(),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='method',
            field=django_summernote.fields.SummernoteTextField(),
        ),
    ]
