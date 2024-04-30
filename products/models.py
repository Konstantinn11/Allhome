from django.db import models
from django.contrib.auth.models import User

class Customer(User):
    birth_date = models.DateField(null=False, blank=False, verbose_name='Дата рождения')
    phone_number = models.CharField(max_length=20, null=False, blank=False, verbose_name='Номер телефона')

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'


class Employer(User):
    image = models.ImageField(null=True, blank=True, upload_to='image/', verbose_name='Фотография сотрудника')
    employer_position = models.ForeignKey(to='EmployerPosition', on_delete=models.CASCADE, null=True, blank=True,
                                          verbose_name='Должность')
    category = models.ForeignKey(to='UslugaCategory', on_delete=models.CASCADE, blank=True, null=True,
                                 verbose_name="Категория услуги")
    phone_number = models.CharField(max_length=20, null=False, blank=False, verbose_name='Номер телефона')
    date_of_employment = models.DateField(null=False, blank=False, verbose_name='Дата приема на работу')
    date_of_dismissal = models.DateField(null=True, blank=True, verbose_name='Дата увольнения')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

class EmployerPosition(models.Model):
    title = models.CharField(max_length=40, null=False, blank=False, verbose_name='Должность')

    def __str__(self):
        return '%s' % self.title

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

class ZayavkaState(models.Model):
    title = models.CharField(max_length=20, null=False, blank=False, verbose_name='Статус заявки')

    def __str__(self):
        return '%s' % self.title

    class Meta:
        verbose_name = 'Статус заявки'
        verbose_name_plural = 'Статусы заявки'


class DogovorState(models.Model):
    title = models.CharField(max_length=20, null=False, blank=False, verbose_name='Статус договора')

    def __str__(self):
        return '%s' % self.title

    class Meta:
        verbose_name = 'Статус договора'
        verbose_name_plural = 'Статусы договора'

class Usluga(models.Model):
    title = models.CharField(max_length=60, null=False, blank=False, verbose_name='Наименование услуги')
    description = models.TextField(verbose_name='Описание услуги')
    image = models.ImageField(upload_to="images/", blank=True, verbose_name="Изображение")
    category = models.ForeignKey(to='UslugaCategory', on_delete=models.CASCADE, blank=True, null=True,
                                 verbose_name="Категория услуги")

    def __str__(self):
        return '%s' % self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

class Price(models.Model):
    number = models.CharField(max_length=20, null=False, blank=False, verbose_name='Номер прайс-листа')
    data = models.DateField(verbose_name="Дата утверждения прайс-листа", auto_now_add=True)
    employer = models.ForeignKey(to='Employer', on_delete=models.CASCADE, blank=True, null=True, verbose_name="Сотрудник")

    def __str__(self):
        return '%s ' % self.data

    class Meta:
        verbose_name = 'Прайс-лист',
        verbose_name_plural = 'Прайс-листы'

class Position_Price(models.Model):
    usluga = models.ForeignKey('Usluga', on_delete=models.CASCADE, blank=True, null=True,
                               verbose_name="Услуга")
    cost_product = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False,
                                       verbose_name="Стоимость услуги")
    price_list = models.ForeignKey('Price', on_delete=models.CASCADE, null=True, blank=True,verbose_name='Прайс-лист')

    def __str__(self):
        return '%s %s руб.' % (self.usluga,  self.cost_product)

    class Meta:
        verbose_name = 'Позиция прайс-листа',
        verbose_name_plural = 'Позиции прайс-листа'

class Zayavka(models.Model):
    number = models.CharField(max_length=10, null=False, blank=False, verbose_name='Номер заявки')
    date_document = models.DateField(null=False, blank=False, verbose_name='Дата документа')
    position = models.ForeignKey(to='Position_Price', on_delete=models.CASCADE, null=True, blank=True,
                                 verbose_name='Позиция прайс-листа')
    address = models.CharField(max_length=1000, null=False, blank=False, verbose_name='Адрес исполнения')
    description = models.TextField(null=True, blank=True, verbose_name='Комментарий к заявке')
    customer = models.ForeignKey(to='Customer', on_delete=models.CASCADE, null=True, blank=True,
                                 verbose_name='Заказчик')
    employer = models.ForeignKey(to='Employer', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Сотрудник')

    def __str__(self):
        return '%s %s %s' % (self.number, self.date_document, self.customer)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

class UslugaCategory(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False, verbose_name='Категория услуги')
    image = models.ImageField(upload_to="images/", blank=True, verbose_name="Изображение")

    def __str__(self):
        return '%s' % self.title

    class Meta:
        verbose_name = 'Категория услуги'
        verbose_name_plural = 'Категории услуги'

class Dogovor(models.Model):
    number = models.CharField(max_length=30, null=False, blank=False, verbose_name='Номер договора')
    date_oformlenie = models.DateField(verbose_name='Дата оформления договора', null=False, blank=False)
    date_ispolnenie = models.DateField(verbose_name='Дата расторжения', null=True, blank=True)
    summa = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, verbose_name='Сумма договора')
    zayavka = models.OneToOneField(Zayavka, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Номер заявки')

    def __str__(self):
        return '%s %s %s' % (self.number, self.date_oformlenie, self.summa)

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договоры'

class StateofDogovor(models.Model):
    dogovor = models.ForeignKey(to='Dogovor', on_delete=models.CASCADE, verbose_name='Договор', null=True, blank=True)
    status = models.ForeignKey(to='DogovorState', on_delete=models.CASCADE, verbose_name='Статус договора', null=True,
                               blank=True)
    date = models.DateField(verbose_name='Дата статуса', null=False, blank=False)
    employer = models.ForeignKey(to='Employer', on_delete=models.CASCADE, verbose_name='Сотрудник', null=True, blank=True)

    def __str__(self):
        return '%s %s %s' % (self.dogovor, self.status, self.date)

    class Meta:
        verbose_name = 'Статус в договоре'
        verbose_name_plural = 'Статусы в договоре'

class StateofZayavka(models.Model):
    zayavka = models.ForeignKey(to='Zayavka', on_delete=models.CASCADE, verbose_name='Заявка', null=True, blank=True)
    status = models.ForeignKey(to='ZayavkaState', on_delete=models.CASCADE, verbose_name='Статус заявки', null=True,
                               blank=True)
    date = models.DateField(verbose_name='Дата статуса', null=False, blank=False)
    employer = models.ForeignKey(to='Employer', on_delete=models.CASCADE, verbose_name='Сотрудник', null=True, blank=True)

    def __str__(self):
        return '%s %s %s' % (self.zayavka, self.status, self.date)

    class Meta:
        verbose_name = 'Статус в заявке'
        verbose_name_plural = 'Статусы в заявке'

class Otziv(models.Model):
    number = models.ForeignKey(to='Zayavka', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Номер заявки')
    text = models.TextField(max_length=200, blank=False, null=True, verbose_name='Отзыв')

    def __str__(self):
        return '%s' % self.number

    class Meta:
        verbose_name = 'Отзыв',
        verbose_name_plural = 'Отзывы'

class Contact(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Автор сообщения')
    message = models.TextField(max_length=200, blank=False, null=True, verbose_name='Сообщение')

    def __str__(self):
        return '%s' % self.username

    class Meta:
        verbose_name = 'Сообщение',
        verbose_name_plural = 'Сообщения'

class Act(models.Model):
    number = models.CharField(max_length=30, null=False, blank=False, verbose_name='Номер акта')
    date_document = models.DateField(null=False, blank=False, verbose_name='Дата документа')
    zayavka = models.OneToOneField(to='Zayavka', on_delete=models.CASCADE, blank=True, null=True,
                               verbose_name='Номер заявки')
    summa = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, verbose_name='Итого')

    def __str__(self):
        return '%s %s' % (self.number, self.date_document)

    class Meta:
        verbose_name = 'Акт выполненных работ',
        verbose_name_plural = 'Акты выполненных работ'

class Position_Act(models.Model):
    act = models.ForeignKey(to='Act', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Номер акта')
    position = models.ForeignKey(to='Position_Price', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Позиция прайс-листа')
    kolichestvo = models.CharField(max_length=30, null=False, blank=False, verbose_name='Количество услуг')
    itogo = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, verbose_name='Итого по позиции')

    def __str__(self):
        return '%s' % self.act

    class Meta:
        verbose_name = 'Позиция акта выполненных работ',
        verbose_name_plural = 'Позиции акта выполненных работ'