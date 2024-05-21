# Generated by Django 4.2.7 on 2024-05-21 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_alter_usluga_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/', verbose_name='Фотография сотрудника (jpeg, png)'),
        ),
        migrations.AlterField(
            model_name='uslugacategory',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='Изображение (jpeg, png)'),
        ),
    ]
