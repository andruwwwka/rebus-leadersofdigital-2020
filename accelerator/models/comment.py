from django.db import models


class Comment(models.Model):
    """Комментарий к предложению."""
    message = models.TextField(
        verbose_name='Текст комментария',
    )
    author = models.ForeignKey(
        'users.Profile',
        on_delete=models.CASCADE
    )
    tender = models.ForeignKey(
        'Tender',
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления комментария',
    )
