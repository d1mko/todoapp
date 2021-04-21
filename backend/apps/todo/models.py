from django.db import models
from django.contrib.auth import get_user_model

from django.db import models

User = get_user_model()


class Todo(models.Model):
    COLORS = (
        ('#6fa8dc', 'blue'),
        ('#6aa84f', 'green'),
        ('#f9cb9c', 'beige'),
        ('#ffffff', 'white'))

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='todos')
    content = models.TextField()
    color = models.CharField(max_length=100, choices=COLORS)
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               null=True,
                               default=None,
                               related_name='children')
