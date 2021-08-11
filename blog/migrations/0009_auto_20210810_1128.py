# Generated by Django 3.2.6 on 2021-08-10 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_description'),
        ('blog', '0008_comment_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='category',
            name='color',
            field=models.CharField(blank=True, choices=[('pink', 'pink'), ('red', 'red'), ('aqua', 'aqua'), ('green', 'green'), ('grey', 'grey'), ('yellow', 'yellow'), ('custom-blue', 'custom-blue'), ('orange', 'orange')], max_length=12, null=True),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField()),
                ('rated', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_ratings', to='blog.post')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_ratings', to='users.profile')),
            ],
        ),
    ]