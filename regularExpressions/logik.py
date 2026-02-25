def my_view(request):
    if request.method == 'POST':
        # Сохраняем в переменные
        regex = request.POST.get('regexInput')  # строка 1
        test_string = request.POST.get('testString')  # строка 2

        # Теперь данные в переменных
        print(regex)  # то что ввели в regexInput
        print(test_string)