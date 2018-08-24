from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    name = models.CharField('分类', max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Category'


class Tag(models.Model):
    name = models.CharField('标签', max_length=20)

    def __str__(self):
        return self.name


class Music(models.Model):
    name = models.CharField('歌曲名称', max_length=50)
    author = models.CharField('创作者', max_length=50)
    pic = models.URLField('封面链接', null=True, blank=True)
    url = models.URLField('歌曲链接')

    def __str__(self):
        return '{} - {}'.format(self.name, self.author)


class Post(models.Model):
    # 标题
    title = models.CharField('标题', max_length=100)
    # 描述
    show_desc = models.BooleanField('在正文显示描述', default=True)
    desc = models.TextField('描述', blank=True, null=True)
    # URL显示的文本
    # show = models.CharField('url显示', max_length=10)
    # 发布 修改时间
    create_time = models.DateTimeField('创建时间', default=timezone.now)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    # 置顶 隐藏 草稿
    hide = models.BooleanField('隐藏', default=False)
    pin = models.BooleanField('置顶', default=False)
    draft = models.BooleanField('草稿', default=False)
    # 作者
    author = models.ForeignKey(User, auto_created=True,
                               on_delete=models.CASCADE)
    # 分类 标签
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, blank=True)
    # 音乐
    has_music = models.BooleanField('Has Music', default=True)
    music = models.ForeignKey(Music, null=True, blank=True,
                              on_delete=models.CASCADE)
    # 开放评论区 目录
    can_comment = models.BooleanField('开放评论区', default=True)
    toc = models.BooleanField('TOC', default=False)
    # 正文
    body = models.TextField('正文')
    view_count = models.IntegerField('浏览量', default=0)
    cc = models.BooleanField('使用CC授权', default=True)

    def __str__(self):
        return '[{cate}]{title}'.format(cate=self.category,
                                        title=self.title)

    class Meta:
        ordering = ['-pin', '-create_time']


class FriendLink(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return self.title
