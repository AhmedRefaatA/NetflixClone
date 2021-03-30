from django.contrib import admin
from .models import *
# Register your models here.

class MovieInline(admin.StackedInline):
    model = Movie
    extra = 4
    max_num = 10



class CoutnryAdmin(admin.ModelAdmin):
    inlines = [MovieInline]



class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "story", "publish_year")
    list_filter = ("rate",)

admin.site.register(Movie, MovieAdmin)
admin.site.register(Country, CoutnryAdmin)
admin.site.register(Rate)
admin.site.register(Category)
admin.site.register(Classification)
admin.site.register(Producer)