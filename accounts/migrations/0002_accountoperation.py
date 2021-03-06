# Generated by Django 3.2.7 on 2021-10-03 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountOperation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation_dt', models.DateField(auto_created=True)),
                ('operation_id', models.CharField(max_length=32)),
                ('cost', models.IntegerField(default=0)),
                ('account_from', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='account_from', to='accounts.account')),
                ('account_to', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='account_to', to='accounts.account')),
            ],
        ),
    ]
