from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'win_django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^store/', include('store.urls'), name='store'),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
