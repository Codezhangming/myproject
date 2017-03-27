# -*- coding:utf-8 -*-

# myproject/urls.py
from django.conf.urls import patterns, url, include
import views
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',

    url(r'test',views.test),

)
