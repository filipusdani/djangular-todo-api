# Generated by Django 4.2 on 2023-04-19 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.CharField(blank=True, max_length=255, null=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('created_by', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField()),
            ],
        ),
    ]