# Generated by Django 3.1.7 on 2021-03-23 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='K_Day',
            fields=[
                ('code', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('code_name', models.CharField(max_length=128)),
                ('date', models.CharField(max_length=128)),
                ('open', models.CharField(max_length=128)),
                ('high', models.CharField(max_length=128)),
                ('low', models.CharField(max_length=128)),
                ('close', models.CharField(max_length=128)),
                ('preclose', models.CharField(max_length=128)),
                ('volume', models.CharField(max_length=128)),
                ('amount', models.CharField(max_length=128)),
                ('adjustflag', models.CharField(max_length=128)),
                ('turn', models.CharField(max_length=128)),
                ('tradestatus', models.CharField(max_length=128)),
                ('pctChg', models.CharField(max_length=128)),
                ('isST', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128)),
                ('code', models.CharField(max_length=128)),
                ('code_name', models.CharField(max_length=128)),
                ('volume', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('code', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('code_name', models.CharField(max_length=128)),
            ],
        ),
    ]
