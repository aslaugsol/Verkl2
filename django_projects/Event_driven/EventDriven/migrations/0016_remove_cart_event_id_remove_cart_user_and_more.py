# Generated by Django 4.0.4 on 2022-06-03 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EventDriven', '0015_alter_paymentinfo_cvc_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='event_id',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
        migrations.DeleteModel(
            name='Credentials',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tickets',
            name='event_id',
        ),
        migrations.RemoveField(
            model_name='tickets',
            name='name_on_ticket',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Tickets',
        ),
    ]
