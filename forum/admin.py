
from django.contrib import admin
from forum import models

class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'topic', 'author_nick', 'reply_to', 'creation_date')

admin.site.register(models.Topic)
admin.site.register(models.Bucket)
admin.site.register(models.Comment, CommentAdmin)
