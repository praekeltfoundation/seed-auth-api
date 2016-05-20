from django.conf.urls import include, url
from rest_framework_nested import routers

from authapi import views

router = routers.DefaultRouter()
router.register(r'organizations', views.OrganizationViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'users', views.UserViewSet)

orgusers_router = routers.NestedSimpleRouter(
    router, r'organizations', lookup='organization')
orgusers_router.register(
    r'users', views.OrganizationUsersViewSet,
    base_name='seedorganization-users')

permissions_router = routers.NestedSimpleRouter(
    router, r'teams', lookup='team')
permissions_router.register(
    r'permissions', views.TeamPermissionViewSet,
    base_name='seedteam-permissions')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(orgusers_router.urls)),
    url(r'^', include(permissions_router.urls)),
]
