# Generated by Django 5.1.3 on 2024-12-10 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_booking_delete_menu_delete_menucategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=100)),
                ('shift', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
    ]
