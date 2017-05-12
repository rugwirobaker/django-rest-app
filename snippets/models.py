# -*- coding: utf-8 -*-
from django.db import models

#A lexer splits the source into tokens, 
# #fragments of the source that have a token type 
# #that determines what the text represents semantically 
# (e.g., keyword, string, or comment). 
# #There is a lexer for every language or markup format that Pygments supports.
from pygments.lexers import get_all_lexers


from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)
    


