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
from django.shortcuts import render
from django.conf import settings
import csv
import os


def executable_transformations(request):
    return render(request, 'pybirdai/executable_transformations.html')

def report_templates(request):
    return render(request, 'pybirdai/report_templates.html')

