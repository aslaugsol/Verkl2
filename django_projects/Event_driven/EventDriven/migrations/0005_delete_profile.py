# Generated by Django 4.0.4 on 2022-05-29 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EventDriven', '0004_profile_alter_paymentinfo_user_id_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
