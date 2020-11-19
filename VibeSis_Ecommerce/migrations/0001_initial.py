# Generated by Django 3.1.2 on 2020-11-19 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('categories', models.CharField(choices=[('SL', 'Sale'), ('SH', 'Short'), ('CA', 'Calça'), ('VE', 'Vestido'), ('SA', 'Saia'), ('MA', 'Macação/Macaquinho'), ('CR', 'Cropped'), ('CM', 'Camisa'), ('BO', 'Body'), ('JA', 'Jaqueta/Casaco'), ('CN', 'Conjunto'), ('AC', 'Acessórios')], default='SL', max_length=2)),
                ('color', models.CharField(max_length=20)),
                ('quantity', models.IntegerField()),
                ('size', models.CharField(max_length=2)),
                ('description', models.TextField()),
            ],
        ),
    ]
