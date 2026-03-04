from django.shortcuts import render
import re

def index(request):
    regex = ""
    test_string = ""
    matches = []


    if request.method == "POST":
        regex = request.POST.get("regexInput", "")

        # Проверяем, был ли загружен файл
        if request.FILES.get("fileInput"):
            uploaded_file = request.FILES["fileInput"]
            # Читаем содержимое файла
            test_string = uploaded_file.read().decode('utf-8')
        else:
            test_string = request.POST.get("testString", "")
        try:
            matches = re.findall(regex, test_string)
        except re.error:
            matches = ["Ошибка в регулярном выражении!"]

    context = {
        "regex": regex,
        "test_string": test_string,
        "matches": matches,
    }
    return render(request, "regularExpressions/base.html", context)




