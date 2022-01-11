# Generated by Django 3.2 on 2022-01-01 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0004_auto_20211228_2145'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('detail', models.TextField(blank=True, null=True)),
                ('complete', models.BooleanField(default=False)),
            ],
        ),
    ]
