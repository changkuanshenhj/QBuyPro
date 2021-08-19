# Generated by Django 2.0.1 on 2021-08-19 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveGoodsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.FloatField(default=0.88, verbose_name='折扣率')),
            ],
            options={
                'verbose_name': '活动详情',
                'verbose_name_plural': '活动详情',
                'db_table': 'app_active_goods',
            },
        ),
        migrations.CreateModel(
            name='ActiveModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='名称')),
                ('img1', models.ImageField(upload_to='actives', verbose_name='图片1')),
                ('start_time', models.CharField(max_length=30, verbose_name='开始时间')),
                ('end_time', models.CharField(max_length=30, verbose_name='结束时间')),
            ],
            options={
                'verbose_name': '活动信息',
                'verbose_name_plural': '活动信息',
                'db_table': 'app_actives',
            },
        ),
        migrations.AddField(
            model_name='activegoodsmodel',
            name='active',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='actives', to='actives.ActiveModel', verbose_name='活动名'),
        ),
        migrations.AddField(
            model_name='activegoodsmodel',
            name='goods',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='actives', to='goods.GoodsModel', verbose_name='商品名'),
        ),
    ]
