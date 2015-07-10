from django.contrib import admin
from helloworld.models import Blogs
from django import forms
from django import formfield



class BlogsAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(BlogsAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'content':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield
# Register your models here.
admin.site.register(Blogs, BlogsAdmin)
