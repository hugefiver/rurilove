from django.db import models
from home.models import Post

# Create your models here.


class Comment(models.Model):
    name = models.CharField('称呼', max_length=20)
    url = models.URLField('URL', blank=True, null=True)
    email = models.EmailField('E-Mail', blank=True, null=True)
    create_time = models.DateTimeField('发布时间',
                                       auto_now_add=True)
    body = models.TextField('留言')
    hide = models.BooleanField('隐藏', default=False)
    post = models.ForeignKey(Post, verbose_name='文章', on_delete=models.CASCADE)

    def __str__(self):
        return '(post}-{name}:"{t}"'.format(post=post,
                                            name=name,
                                            t=body[:10])

    class Meta:
        ordering = ['-create_time']

