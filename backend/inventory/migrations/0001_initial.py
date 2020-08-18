# Generated by Django 3.1 on 2020-08-18 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=10000)),
                ('price_per', models.IntegerField(default=0.0)),
                ('cost_per', models.IntegerField(default=0.0)),
                ('in_stock', models.IntegerField(default=0)),
                ('weight_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('weight_unit', models.CharField(choices=[('g', 'gram'), ('oz', 'ounce'), ('lb', 'pound'), ('na', 'not applicable')], max_length=2)),
                ('volume_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('volume_unit', models.CharField(choices=[('fl oz', 'fluid ounce'), ('pt', 'pint'), ('qt', 'quart'), ('gal', 'gallon'), ('na', 'not applicable')], max_length=5)),
                ('categories', models.ManyToManyField(related_name='categories', to='inventory.Category')),
            ],
        ),
    ]