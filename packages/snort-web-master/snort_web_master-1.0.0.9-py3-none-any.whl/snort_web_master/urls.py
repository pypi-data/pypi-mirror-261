"""snort_web_master URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from snort.views import get_rule, get_rule_keys, get,\
    build_rule_parse,build_rule_serialize, \
    build_rule_keyword_to_rule, build_rule_rule_to_keywords, \
    favico,get_current_user_name, check_pcap, convert2to3
from django.conf import settings
from django.conf.urls.static import static
import django.contrib.auth.admin
django.contrib.auth.admin.UserAdmin.readonly_fields= ("last_login", 'date_joined')
admin.site.site_header = 'snort web master'
app_name = "snort_web_master"
urlpatterns = [
    path("favicon.ico", favico),
    path("check_pcap/", check_pcap, name="check_pcap"),
    path("get_rule_update/<int:rule_id>/", get_rule, name="get_rule_update"),
    path("get_rule_update/<str:cloned>/", get_rule, name="get_rule_update"),
    path("get_rule_update//", get_rule, name="get_rule_update"),
    path("get_rule_keywords/<int:rule_id>/", get_rule_keys,name="get_rule_keywords"),
    path('advanced_filters/', include("advanced_filters.urls"), name="advance_filter"),
    path("build_rule/keyword_to_rule", build_rule_keyword_to_rule,name="build_rule"),
    path("build_rule/rule_to_keywords", build_rule_rule_to_keywords,name="build_keyword"),
    path("build_rule_parse/", build_rule_parse, name="build_rule_parse"),
    path("build_rule_serialize/", build_rule_serialize, name="build_rule_serialize"),
    path("build_rule_serialize/", build_rule_serialize, name="build_rule_serialize"),
    path("convert2to3/", convert2to3, name="convert2to3"),
    path("get/<str:stage>/", get, name="get"),
    path("get/", get, name="get"),
    path('admin/', admin.site.urls, name="admin_main"),
    path('',  admin.site.urls, name="admin_main"),
]+ static("static/", document_root=settings.STATIC_ROOT) + static("/", document_root=settings.BASE_DIR)
