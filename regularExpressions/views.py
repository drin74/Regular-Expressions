from django.shortcuts import render
import re

def index(request):
    regex = ""
    test_string = ""
    matches = []

    if request.method == "POST":
        regex = request.POST.get("regexInput", "")

        if request.FILES.get("fileInput"):
            uploaded_file = request.FILES["fileInput"]

            # Новая проверка!!!
            if not uploaded_file.name.endswith('.txt'):
                matches = ["Ошибка: Можно загружать только файлы .txt!"]
                test_string = request.POST.get("testString", "")
            else:
                test_string = uploaded_file.read().decode('utf-8')
        else:
            test_string = request.POST.get("testString", "")

        try:
            if not matches:  # Ищем только если нет ошибки
                matches = re.findall(regex, test_string)
        except re.error:
            matches = ["Ошибка в регулярном выражении!"]

    context = {
        "regex": regex,
        "test_string": test_string,
        "matches": matches,
    }
    return render(request, "regularExpressions/base.html", context)




