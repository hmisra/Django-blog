from django.contrib import admin
from helloworld.models import Blogs



class BlogsAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(CabAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'content':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield
# Register your models here.
admin.site.register(Blogs, BlogsAdmin)
