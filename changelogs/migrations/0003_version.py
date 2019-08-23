# Generated by Django 2.2.4 on 2019-08-23 09:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("changelogs", "0002_project_subscribers")]

    operations = [
        migrations.CreateModel(
            name="Version",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=20)),
                ("date_time", models.DateTimeField()),
                ("body", models.TextField()),
            ],
            options={"db_table": "versions"},
        )
    ]
