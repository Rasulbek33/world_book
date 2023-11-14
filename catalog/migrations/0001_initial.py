# Generated by Django 3.2.12 on 2023-11-09 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Avtorning ismini kiriting!', max_length=100, verbose_name='Avtorning ismi')),
                ('last_name', models.CharField(help_text='Avtorning familyasini kiriting!', max_length=100, verbose_name='Avtorning familyasi')),
                ('date_of_birth', models.DateField(blank=True, help_text="Avtorning tug'ilgan kunini kiritng!", null=True, verbose_name="Avtorning tug'ilgan kuni")),
                ('about', models.TextField(help_text='Avtor haqida', verbose_name='Avtor haqida')),
                ('photo', models.ImageField(blank=True, help_text='Avtorning rasimini kiriting!', null=True, upload_to='author/%Y/%m/%d', verbose_name='Avtor rasmi')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Kitobning nomini tanlang', max_length=200, verbose_name='Kitobning nomi')),
                ('year', models.CharField(help_text='Kitobning chiqarilgan yilini kiriting!', max_length=4, verbose_name='Kitobning yili')),
                ('summary', models.TextField(help_text='Kitob haqida xulosangizni kiriting!', max_length=1000)),
                ('isbn', models.CharField(help_text="Uzunligi 13 ta belgidan iborat bo'lsin", max_length=13, verbose_name='Kitobning ISBN')),
                ('price', models.DecimalField(decimal_places=2, help_text='Kitobning narxini kiriting!', max_digits=7, verbose_name='Narx (sum)')),
                ('photo', models.ImageField(help_text='Kitobning rasmini kiriting!', upload_to='books/%Y/%m/%d', verbose_name='Kitobning rasmi')),
                ('author', models.ManyToManyField(help_text='Kitobning Avtor (Avtorlari) tanlang', to='catalog.Author', verbose_name='Kitobning Avtor(Avtorlari)')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Kitobning janrini kiriting!', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Kitobning tilini kiriting!', max_length=20, verbose_name='Kitobning tili')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nashriyotning nomini kiriting!', max_length=20, verbose_name='Nashriyot nomi')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Kitobning statusini kiriting!', max_length=20, verbose_name='Kitobning statusi')),
            ],
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inv_nom', models.CharField(help_text='Kitobning inventar nomerini kiriting!', max_length=20, null=True, verbose_name='Inverntar nomer')),
                ('due_back', models.DateField(blank=True, help_text='Kitobning status tugash vaqti', null=True)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.book')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.status')),
            ],
            options={
                'ordering': ['due_back'],
            },
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(help_text='Kitobning janrini tanlang', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.genre', verbose_name='Kitobning janri'),
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(help_text='Kitobning tilini tanlang', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.language', verbose_name='Kitobning tili'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(help_text='Nashriyotni tanlang', on_delete=django.db.models.deletion.CASCADE, to='catalog.publisher', verbose_name='Nashriyot'),
        ),
    ]