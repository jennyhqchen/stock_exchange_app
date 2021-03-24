# Generated by Django 3.1.7 on 2021-03-23 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_exchange', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShareHolding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128)),
                ('code', models.CharField(max_length=128)),
                ('code_name', models.CharField(max_length=128)),
                ('volume', models.IntegerField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='sell_or_buy',
            field=models.IntegerField(default=0),
        ),
    ]