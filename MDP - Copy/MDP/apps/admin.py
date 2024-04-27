from django.contrib import admin
from apps.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phonenumber', 'feedback')


admin.site.register(Feedback, FeedbackAdmin)

# Register your models here.
