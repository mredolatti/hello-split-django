# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import HttpResponse
from django_splitio import get_factory


def hello_world(request):
    factory = get_factory()
    client = factory.client()
    key = request.GET.get('key')
    split = request.GET.get('split')
    return HttpResponse(client.get_treatment(key, split))
