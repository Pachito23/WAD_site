# Generated by Django 4.1.2 on 2022-11-17 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0040_remove_customer_firstname_remove_customer_lastname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='name',
            new_name='full_name',
        ),
    ]