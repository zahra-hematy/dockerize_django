# Generated by Django 4.1.7 on 2025-03-28 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upimg', '0004_alter_customuser_email_alter_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=models.ImageField(upload_to='images/%m-%Y/', verbose_name='تصویر'),
        ),
    ]
