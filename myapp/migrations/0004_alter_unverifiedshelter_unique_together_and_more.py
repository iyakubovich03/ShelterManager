# Generated by Django 5.1.1 on 2024-09-28 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_unverifiedshelter'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='unverifiedshelter',
            unique_together={('address', 'latitude', 'longitude')},
        ),
        migrations.AlterField(
            model_name='unverifiedshelter',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='unverifiedshelter',
            name='available_food',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='unverifiedshelter',
            name='available_medical_supplies',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='unverifiedshelter',
            name='electricity',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='unverifiedshelter',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.RemoveField(
            model_name='unverifiedshelter',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='unverifiedshelter',
            name='updated_at',
        ),
    ]