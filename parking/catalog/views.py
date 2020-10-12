from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView
from django.db.models import Q
from functools import reduce
from .models import Car
import operator


class CarListView(View):
    def get(self, request):
        manufacturers_selected_item = ""
        modes_selected_item = ""
        transmissions_selected_item = ""
        issuances_selected_item = ""
        colors_selected_item = ""

        # Заполняем пункты выпадающего меню фильтров
        # так как в задании четко обозначен тип полей
        # пришлось изобразить это и второй зарос к БД 
        car_list = Car.objects.all()
        transmissions_list = set()
        manufacturers_list = set()
        models_list = set()
        issuances_list = set()
        colors_list = set()
        for item in car_list:
            transmissions_list.add(item.transmission)
            manufacturers_list.add(item.manufacturer)
            models_list.add(item.model)
            issuances_list.add(item.issuance)
            colors_list.add(item.color)

        # Формируем список Q-функций для запроса и запрашиваем БД
        if request.GET:
            # Для возврата состояния выбранного пункта фильтра
            manufacturers_selected_item = request.GET["manufacturer"]
            modes_selected_item = request.GET["model"]
            transmissions_selected_item = request.GET["transmission"]
            issuances_selected_item = request.GET["issuance"]
            colors_selected_item = request.GET["color"]

            q_list = []
            for item, value in request.GET.items():
                if value:
                    q_list.append(Q(**{item:value}))    
            car_list = Car.objects.filter(*q_list)

        return render(request, "index.html", {
            "car_list":car_list, 
            "manufacturers_list":manufacturers_list, 
            "manufacturers_selected_item":manufacturers_selected_item, 
            "models_list":models_list, 
            "modes_selected_item":modes_selected_item, 
            "transmissions_list": transmissions_list, 
            "transmissions_selected_item":transmissions_selected_item, 
            "issuances_list":issuances_list, 
            "issuances_selected_item":issuances_selected_item, 
            "colors_list":colors_list, 
            "colors_selected_item":colors_selected_item
            })