# Generated by Django 3.1.7 on 2021-03-27 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('netflix', '0003_category_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=233)),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=233)),
            ],
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='year',
            new_name='publish_year',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='overview',
            new_name='story',
        ),
        migrations.AddField(
            model_name='movie',
            name='duration',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=233),
        ),
        migrations.AddField(
            model_name='movie',
            name='classification',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='netflix.classification'),
        ),
        migrations.AddField(
            model_name='movie',
            name='producer',
            field=models.ManyToManyField(to='netflix.Producer'),
        ),
    ]