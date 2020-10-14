# Generated by Django 2.2.7 on 2020-02-25 20:11

from django.contrib.postgres.fields import JSONField as JSONBField
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0006_remove_formbuilder_preference_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrauserdetail',
            name='data',
            field=JSONBField(default=dict),
        ),
        migrations.AlterField(
            model_name='perusersetting',
            name='user_queries',
            field=JSONBField(help_text='A JSON representation of a *list* of Django queries, e.g. `[{"email__iendswith": "@kobotoolbox.org"}, {"email__iendswith": "@kbtdev.org"}]`. A matching user is one who would be returned by ANY of the queries in the list.'),
        ),
    ]
