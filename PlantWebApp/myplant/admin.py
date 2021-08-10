from django.contrib import admin
from .models import Question,Choice,AddPlant,Comment,Posts,Profile

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Posts)
admin.site.register(AddPlant)
admin.site.register(Comment)
admin.site.register(Profile)

# Register your models here.
