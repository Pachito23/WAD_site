# Generated by Django 4.1.2 on 2022-11-15 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0028_rename_card_data_order_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')], max_length=2),
        ),
    ]
