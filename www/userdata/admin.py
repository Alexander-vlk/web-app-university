from django.contrib import admin


from .models import UserDataModel, UserProgrammingLanguages


admin.site.register(UserDataModel)
admin.site.register(UserProgrammingLanguages)