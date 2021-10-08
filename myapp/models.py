from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField

class Prefecture(models.Model):
    name = models.CharField('都道府県名', max_length=10)

    class Meta:
        verbose_name = '都道府県'
        verbose_name_plural = '都道府県'
    
    def __str__(self):
        return self.name



class City(models.Model):
    prefecture = models.ForeignKey(Prefecture, on_delete=PROTECT)
    name = models.CharField(max_length=24)

    class Meta:
        verbose_name = '市区町村'
        verbose_name_plural = '市区町村'

    def __str__(self):
        return self.name

class Occupation(models.Model):
    name = models.CharField('職種', max_length=20)

    class Meta:
        verbose_name = '職種'
        verbose_name_plural = '職種'

    def __str__(self):
        return self.name


class Industry(models.Model):
    name = models.CharField('産業', max_length=20)

    class Meta:
        verbose_name = '業種'
        verbose_name_plural = '業種'

    def __str__(self):
        return self.name



class Salary(models.Model):
    name = CharField('給与', max_length=10)

    class Meta:
        verbose_name = '年収'
        verbose_name_plural = '年収'

    def __str__(self):
        return self.name



class Tag(models.Model):
    name = models.CharField('タグ', max_length=20)

    class Meta:
        verbose_name = 'タグ'
        verbose_name_plural = 'タグ'

    def __str__(self):
        return self.name


class Time(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()



class Post(models.Model):
    WORK_STYLE = {
        ('part-time', 'アルバイト'),
        ('permanent', '正社員'),
        ('temporary', '派遣社員'),
        ('other', 'その他'),
    }

    title = models.CharField('タイトル', max_length=34)
    content = models.TextField('説明文')
    Industry = models.ManyToManyField(Industry, verbose_name='業種')
    occupation = models.ManyToManyField(Occupation, verbose_name='職種')
    job_description = models.CharField('業務内容', max_length=25)
    qualifications = models.TextField('応募資格')
    time = models.TextField('勤務時間', max_length=30)
    thumbnail = models.ImageField('サムネイル', upload_to='thumbnails/', blank=False)
    img = models.FileField(upload_to='images/', blank=False, verbose_name='動画')
    work_style = models.CharField('雇用形態', max_length=20, choices=WORK_STYLE)
    salary = models.ForeignKey(Salary, verbose_name='年収', on_delete=PROTECT)
    tag = models.ManyToManyField(Tag, verbose_name='タグ', blank=True)
    vacation = models.CharField('休日休暇',max_length=30)
    benefit = models.TextField('福利厚生')
    prefecture = models.ForeignKey(Prefecture, verbose_name='都道府県', on_delete=PROTECT)
    city = models.ForeignKey(City, on_delete=PROTECT, verbose_name='市区町村')