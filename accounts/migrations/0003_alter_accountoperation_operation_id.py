# Generated by Django 3.2.7 on 2021-10-03 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_accountoperation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountoperation',
            name='operation_id',
            field=models.CharField(blank=True, max_length=32),
        ),
    ]
