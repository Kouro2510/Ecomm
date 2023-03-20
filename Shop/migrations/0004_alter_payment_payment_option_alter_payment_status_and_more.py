# Generated by Django 4.1.7 on 2023-03-20 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0003_alter_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_option',
            field=models.CharField(choices=[('Card', 'Card'), ('Wallet', 'Wallet'), ('MoMo', 'MoMo')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('On The Way', 'On The Way'), ('Packed', 'Packed'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel'), ('Accepted', 'Accepted'), ('Pending', 'Pending')], default='Pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='paymentoption',
            name='name',
            field=models.CharField(choices=[('Card', 'Card'), ('Wallet', 'Wallet'), ('MoMo', 'MoMo')], max_length=50),
        ),
    ]
