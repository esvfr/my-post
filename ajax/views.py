# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
import json

from django.contrib import auth
from django.http import HttpResponse
from django.views import View


class BookmarkView(View):
    # в данную переменную будет устанавливаться модель закладок, которую необходимо обработать
    model = None

    def post(self, request, pk):
        # нам потребуется пользователь
        user = auth.get_user(request)
        # пытаемся получить закладку из таблицы, или создать новую
        bookmark, created = self.model.objects.get_or_create(user=user, obj_id=pk)
        # если не была создана новая закладка,
        # то считаем, что запрос был на удаление закладки
        if not created:
            bookmark.delete()

        return HttpResponse(
            json.dumps({
                "result": created,
                "count": self.model.objects.filter(obj_id=pk).count()
            }),
            content_type="application/json"
        )