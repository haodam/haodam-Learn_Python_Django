from django.conf.urls import url, include
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib import admin
from .import views
from .import base_class_views
from .import user_views

urlpatterns = [
    # Ham Views
    url(r"^$", views.index, name="index"),
    url(r"^list-reporter$", views.list_reporter, name="list_reporters"),
    url(r"^add-article", views.add_article, name ="add_article"),
    url(r"^validate-emails", views.validate_email, name ="validate_email"),
    url(r"^reporter/(?P<reporter_id>[0-9]+)$", views.view_detail_reporter, name="view_detail_reporter"),
    url(r"^update-reporter/(?P<reporter_id>[0-9]+)$", views.update_reporter, name="update_reporter"),
    url(r"^delete-reporter/(?P<reporter_id>[0-9]+)$", views.delete_reporter, name="delete_reporter"),
    #url(r"^register$", views.register_user, name ="register_user"),
    url(r"^add-reporter$", views.add_reporter, name="add_reporter"),
    
    # class_base_Views
    url(r"^all-reporter$", base_class_views.ReporterListView.as_view(), name = "all_reporters"),
    url(r"^view-reporter/(?P<pk>[0-9]+)$", base_class_views.ReporterDetailView.as_view(),name="view_reporter"),
    url(r"^insert-reporter$",base_class_views.ReporterCreateView.as_view(),name ="insert_reporter"),
    url(r"^edit-reporter/(?P<pk>[0-9]+)$", base_class_views.ReporterUpdateView.as_view(),name="edit_reporter"),
    url(r"^remove-reporter/(?P<pk>[0-9]+)$", base_class_views.reporterDeleteView.as_view(),name="remove_reporter"),

    # User authentication/authorization
    url(r"^register$", user_views.register_user, name ="register_user"),
    url(r"^login$", user_views.login_user, name ="login_user"),
    url(r"^logout$", auth_views.LogoutView.as_view(next_page="/"), name="logout_user"),


    
]