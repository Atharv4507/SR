# Generated by Django 4.2.5 on 2023-10-13 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_pcw_category_select'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pcw',
            old_name='category_select',
            new_name='input_category',
        ),
        migrations.RenameField(
            model_name='pcw',
            old_name='date',
            new_name='input_date',
        ),
    ]
