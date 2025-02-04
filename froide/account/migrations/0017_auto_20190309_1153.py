# Generated by Django 2.1.7 on 2019-03-09 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0016_auto_20190212_1101"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserTag",
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
                (
                    "name",
                    models.CharField(max_length=100, unique=True, verbose_name="Name"),
                ),
                (
                    "slug",
                    models.SlugField(max_length=100, unique=True, verbose_name="Slug"),
                ),
                ("public", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "user tag",
                "verbose_name_plural": "user tags",
            },
        ),
        migrations.AlterModelOptions(
            name="taggeduser",
            options={
                "verbose_name": "tagged user",
                "verbose_name_plural": "tagged users",
            },
        ),
    ]
