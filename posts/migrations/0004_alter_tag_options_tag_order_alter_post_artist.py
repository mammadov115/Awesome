# Generated by Django 4.2.7 on 2024-02-28 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_tag_post_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='tag',
            name='order',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='artist',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
