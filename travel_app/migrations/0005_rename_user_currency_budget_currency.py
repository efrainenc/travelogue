# Generated by Django 4.1.6 on 2023-02-03 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0004_alter_budget_purpose_alter_budget_user_currency'),
    ]

    operations = [
        migrations.RenameField(
            model_name='budget',
            old_name='user_currency',
            new_name='currency',
        ),
    ]
