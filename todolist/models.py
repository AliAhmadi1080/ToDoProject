from django.db import models
from django.conf import settings


class Tag(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField('نام تگ', max_length=63)
    created = models.DateField("زمان ایجاد شدن", auto_created=True, auto_now_add=True)
    slug = models.SlugField(unique=True, allow_unicode=True, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'تگ'    
        verbose_name_plural = 'تگ ها'    

class Status(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=63, verbose_name="نام")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'وضعیت'
        verbose_name_plural = 'وضعیت ها'

class ToDoList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField('نام', max_length=63)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'لیست وظیفه'
        verbose_name_plural = 'لیست وظیفه ها'

class ToDo(models.Model):
    title        = models.CharField('عنوان', max_length=63)
    subtitle     = models.CharField('زیر عنوان', max_length=63, null=True, blank=True)
    user         = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='کاربر', related_name='user')
    status       = models.ForeignKey("Status", on_delete=models.CASCADE, verbose_name="وضعیت", related_name='status')
    description  = models.TextField('توضیحات', null=True)
    created_at   = models.DateTimeField(auto_now_add=True, verbose_name='زمان شروع', editable=False)
    tags         = models.ManyToManyField('Tag', verbose_name='تگ ها', related_name='todos', blank=True)
    todo_list    = models.ForeignKey(ToDoList, on_delete=models.CASCADE, related_name='todo_list', verbose_name='لیست وظیفه ها')


    # TODO:add subtasks to class

    def __str__(self) -> str:
        return f"{self.title} -> {self.status}"

    class Meta:
        verbose_name = 'وظیفه'
        verbose_name_plural = 'وظیفه ها'



