# Generated by Django 3.2.7 on 2021-10-04 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_accountoperation_operation_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountoperation',
            name='operation_id',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
