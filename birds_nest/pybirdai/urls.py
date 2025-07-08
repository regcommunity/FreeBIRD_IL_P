# coding=UTF-8
# Copyright (c) 2024 Bird Software Solutions Ltd
# This program and the accompanying materials
# are made available under the terms of the Eclipse Public License 2.0
# which accompanies this distribution, and is available at
# https://www.eclipse.org/legal/epl-2.0/
#
# SPDX-License-Identifier: EPL-2.0
#
# Contributors:
#    Neil Mackenzie - initial API and implementation
from django.urls import path

from . import views
from . import report_views

from django.views.generic import TemplateView


app_name = 'pybirdai'  # Add this line if using namespaces

urlpatterns = [
    path('', views.home_view, name='home'),  # This should handle the root URL of your app
    path('executable-transformations/', report_views.executable_transformations, name='executable_transformations'),
    path('execute-data-point/<str:data_point_id>/', views.execute_data_point, name='execute_data_point'),
    path('show-report/<str:report_id>/', views.show_report, name='show_report'),
    path('report-templates/', report_views.report_templates, name='report_templates'),
    path('lineage/', views.list_lineage_files, name='list_lineage_files'),
    path('lineage/<str:filename>/', views.view_csv_file, name='view_csv'),
    path('bird_diffs_and_corrections/', views.bird_diffs_and_corrections, name='bird_diffs_and_corrections'),
    path('test_report_view/', views.test_report_view, name='test_report_view'),
    path('export-database-to-csv/', views.export_database_to_csv, name='export_database_to_csv'),
]
