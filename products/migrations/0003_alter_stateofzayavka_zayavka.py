# Generated by Django 5.0.4 on 2024-05-08 22:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_employer_date_of_employment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stateofzayavka',
            name='zayavka',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stateozayvkas', to='products.zayavka', verbose_name='Заявка'),
        ),
    ]