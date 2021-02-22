"""flow urls"""
from django.urls import path
from django.views.decorators.csrf import ensure_csrf_cookie

from authentik.flows.models import FlowDesignation
from authentik.flows.views import (
    CancelView,
    ConfigureFlowInitView,
    FlowExecutorShellView,
    ToDefaultFlow,
)

urlpatterns = [
    path(
        "-/default/authentication/",
        ToDefaultFlow.as_view(designation=FlowDesignation.AUTHENTICATION),
        name="default-authentication",
    ),
    path(
        "-/default/invalidation/",
        ToDefaultFlow.as_view(designation=FlowDesignation.INVALIDATION),
        name="default-invalidation",
    ),
    path(
        "-/default/recovery/",
        ToDefaultFlow.as_view(designation=FlowDesignation.RECOVERY),
        name="default-recovery",
    ),
    path(
        "-/default/enrollment/",
        ToDefaultFlow.as_view(designation=FlowDesignation.ENROLLMENT),
        name="default-enrollment",
    ),
    path(
        "-/default/unenrollment/",
        ToDefaultFlow.as_view(designation=FlowDesignation.UNRENOLLMENT),
        name="default-unenrollment",
    ),
    path("-/cancel/", CancelView.as_view(), name="cancel"),
    path(
        "-/configure/<uuid:stage_uuid>/",
        ConfigureFlowInitView.as_view(),
        name="configure",
    ),
    path(
        "<slug:flow_slug>/",
        ensure_csrf_cookie(FlowExecutorShellView.as_view()),
        name="flow-executor-shell",
    ),
]
