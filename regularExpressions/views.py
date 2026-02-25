from django.db.models.expressions import result
from django.http import HttpResponse
from django.shortcuts import render
import re

def index(request):
    return render(request,'regularExpressions/base.html')


def check_regex(request):
    # ВРЕМЕННО: просто показываем, что пришло
    if request.method == 'POST':
        regex = request.POST.get('regexInput')
        test_string = request.POST.get('testString')

        print(f"Regex: {regex}")
        print(f"String: {test_string}")

        result = re.findall(rf'{regex}', test_string)
        print(result)
        return HttpResponse(f"Найдено: {result}")
        print(result)

    # Если GET запрос
    return HttpResponse("Отправьте POST запрос через форму")