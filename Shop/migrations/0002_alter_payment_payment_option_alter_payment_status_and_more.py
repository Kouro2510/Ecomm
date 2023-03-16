# Generated by Django 4.1.7 on 2023-03-15 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_option',
            field=models.CharField(choices=[('Wallet', 'Wallet'), ('Card', 'Card'), ('MoMo', 'MoMo')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Packed', 'Packed'), ('Cancel', 'Cancel'), ('On The Way', 'On The Way'), ('Accepted', 'Accepted'), ('Pending', 'Pending')], default='Pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='paymentoption',
            name='name',
            field=models.CharField(choices=[('Wallet', 'Wallet'), ('Card', 'Card'), ('MoMo', 'MoMo')], max_length=50),
        ),
    ]
