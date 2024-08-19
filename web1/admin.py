from django.contrib import admin

# Register your models here.
from web1.models import FrontEnd,BackEnd,Contact,Skill,Resume

admin.site.register(FrontEnd)
admin.site.register(BackEnd)
admin.site.register(Contact)
admin.site.register(Skill)
admin.site.register(Resume)