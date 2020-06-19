from django.db import models

POST_CHOICES = [
    ('head', 'Руководитель'),
    ('alternative_head', 'Заместитель руководителя'),
    ('senior', 'Ведущий эксперт'),
    ('middle', 'Эксперт'),
    ('junior', 'Младший эксперт'),
]


class Position(models.Model):
    """Должности сотрудников."""
    post = models.CharField(
        max_length=128,
        choices=POST_CHOICES,
        default='junior'
    )
