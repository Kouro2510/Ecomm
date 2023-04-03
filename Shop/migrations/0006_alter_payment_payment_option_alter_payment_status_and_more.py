# Generated by Django 4.1.7 on 2023-03-29 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0005_alter_payment_payment_option_alter_payment_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_option',
            field=models.CharField(choices=[('MoMo', 'MoMo'), ('Visa', 'Visa'), ('ZaloPay', 'ZaloPay'), ('Wallet', 'Wallet'), ('ATM', 'ATM'), ('Mastercard', 'Mastercard')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Pending', 'Pending'), ('Cancel', 'Cancel'), ('Packed', 'Packed'), ('Accepted', 'Accepted'), ('On The Way', 'On The Way')], default='Pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='paymentoption',
            name='name',
            field=models.CharField(choices=[('MoMo', 'MoMo'), ('Visa', 'Visa'), ('ZaloPay', 'ZaloPay'), ('Wallet', 'Wallet'), ('ATM', 'ATM'), ('Mastercard', 'Mastercard')], default='Wallet', max_length=50),
        ),
    ]
