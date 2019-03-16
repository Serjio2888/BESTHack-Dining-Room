from django.db import models

class Bucket(models.Model):
    meal = models.CharField(u'Блюдо', max_length=255)
    calories = models.SmallIntegerField(u'Количество калорий',default = 1)
    price = models.SmallIntegerField(u'Стоимость (в рублях)',default = 40)

    def __str__(self):
        return '{}|{}|{}'.format(self.meal, self.calories, self.price)

class Topic(models.Model):
    MAINCOURSE = 'MC'
    FIRSTCOURSE = 'FC'
    SALADS = 'SD'
    DRINKS = 'DR'
    FOOD_CHOICES = (
        (MAINCOURSE, 'Второе/горячее'),
        (FIRSTCOURSE, 'Первое'),
        (SALADS, 'Салаты'),
        (DRINKS, 'Напитки'),
    )
    food_type = models.CharField(u'Тип блюда',max_length=2,
                                      choices=FOOD_CHOICES,
                                      default=MAINCOURSE)
    weigth = models.SmallIntegerField(u'Масса блюда (в граммах)',default = 100)
    price = models.SmallIntegerField(u'Стоимость (в рублях)',default = 40)
    subject = models.CharField(u'Блюдо', max_length=255)
    text = models.TextField(u'Описание')
    calories = models.SmallIntegerField(u'Количество калорий',default = 1)
    hidden = models.SmallIntegerField(u'Скрытый?(0-нет, 1-да)',default = 0)
    creation_date = models.DateTimeField(u'Дата создания', auto_now_add=True)
    views = models.IntegerField(u'Количество просмотров темы',  default=0)
    made_time = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '{}|{}|{}'.format(self.price, self.calories, self.subject)

class Comment(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    author_nick   = models.CharField(u'Автор', max_length=255)
    text = models.TextField(u'Текст')
    reply_to = models.ForeignKey('forum.Comment', null=True, blank=True, on_delete=models.PROTECT)
    creation_date = models.DateTimeField(u'Дата создания', auto_now_add=True)

    def __str__(self):
        return "{} -> {}".format(self.author_nick, self.topic)    
