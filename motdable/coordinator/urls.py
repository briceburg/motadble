from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('coordinator.views',
    url(r'^execute/', 'execute'),
    url(r'^', 'index', name="catchall")
)
