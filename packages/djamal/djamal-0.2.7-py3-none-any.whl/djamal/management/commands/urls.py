from django.urls import path
from .views import djamal_admin, call_function, edit_deploy_yaml


urlpatterns = [
    path("djamal/", djamal_admin, name="djamal_admin"),
    path("djamal/edit-deploy-yaml/", edit_deploy_yaml, name="edit_deploy_yaml"),
    path("djamal/<str:function_name>/", call_function, name="call_function"),
]
