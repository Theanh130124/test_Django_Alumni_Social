# Generated by Django 4.2.7 on 2023-12-05 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_media', '0011_alter_account_group_account_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='surveyquestion',
            name='question_content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='surveyquestionoption',
            name='question_option_value',
            field=models.TextField(),
        ),
    ]