# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import HttpResponse
from django_splitio import get_factory


def hello_world(request):
    return HttpResponse('SplitIO Rules!')


def test_treatment(request):
    factory = get_factory()
    client = factory.client()

    split_name = request.GET.get('split')
    key = request.GET.get('key')

    if not key or key == '':
        return HttpResponse('No key provided')
    if not split_name or split_name == '':
        return HttpResponse('No split provided')

    treatment = client.get_treatment(key, split_name)
    return HttpResponse(treatment)
