# Generated by Django 4.2.3 on 2023-08-05 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoStoreModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('todo', models.CharField(max_length=50)),
                ('todate', models.DateField(auto_now_add=True)),
            ],
        ),
    ]