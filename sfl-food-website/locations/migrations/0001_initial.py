# Generated by Django 3.0.5 on 2020-09-29 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrgLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=2000)),
                ('cost', models.CharField(max_length=100)),
                ('website', models.URLField()),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('phone_number', models.CharField(max_length=10)),
                ('last_updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
