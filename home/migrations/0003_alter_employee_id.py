# Generated by Django 5.0.3 on 2024-11-13 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_employee"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="id",
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
