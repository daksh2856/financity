from django.contrib import admin

# Register your models here.
from myapp.models import contactus
admin.site.register(contactus)

from myapp.models import user
admin.site.register(user)


from myapp.models import blog
admin.site.register(blog)

from myapp.models import comment
admin.site.register(comment)

from myapp.models import review
admin.site.register(review)

from myapp.models import budget
admin.site.register(budget)

from myapp.models import annualreports
admin.site.register(annualreports)

from myapp.models import services
admin.site.register(services)

from myapp.models import dataandstatistics
admin.site.register(dataandstatistics)

from myapp.models import actandrules
admin.site.register(actandrules)

from myapp.models import guidelines
admin.site.register(guidelines)

