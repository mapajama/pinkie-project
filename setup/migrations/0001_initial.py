# Generated by Django 3.2.16 on 2023-02-06 07:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('nature_of_business', models.CharField(max_length=40)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('tax_number', models.IntegerField()),
                ('bank_name', models.CharField(max_length=30)),
                ('account_number', models.IntegerField()),
                ('contact_name', models.CharField(max_length=30)),
                ('contact_position', models.CharField(max_length=30)),
                ('contact_email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator])),
                ('contact_phone', models.CharField(max_length=15)),
                ('ceo_name', models.CharField(max_length=30)),
                ('ceo_phone', models.CharField(max_length=15)),
                ('ceo_email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator])),
            ],
        ),
        migrations.CreateModel(
            name='Cobroker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_company', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('registered_office_address', models.CharField(max_length=100)),
                ('operating_office_address', models.CharField(max_length=100)),
                ('rc_number', models.IntegerField()),
                ('date_of_incorporated', models.DateField()),
                ('tax_number', models.IntegerField()),
                ('principal_activity_of_company', models.CharField(max_length=30)),
                ('last_year_turnover', models.IntegerField()),
                ('is_company_rated', models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], max_length=3)),
                ('ceo_name', models.CharField(max_length=30)),
                ('ceo_phone', models.CharField(max_length=15)),
                ('ceo_email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator])),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Underwriter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_company', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('registered_office_address', models.CharField(max_length=100)),
                ('operating_office_address', models.CharField(max_length=100)),
                ('rc_number', models.IntegerField()),
                ('date_of_incorporated', models.DateField()),
                ('tax_number', models.IntegerField()),
                ('principal_activity_of_company', models.CharField(max_length=30)),
                ('last_year_turnover', models.IntegerField()),
                ('is_company_rated', models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], max_length=3)),
                ('ceo_name', models.CharField(max_length=30)),
                ('ceo_phone', models.CharField(max_length=15)),
                ('ceo_email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator])),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
