from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
author = {
    "Имя":"Всеволод",
    "Отчество":"Валерьевич",
    "Фамилия":"Севастьянов",
    "телефон":"8-968-642-72-53",
    "email":"Seva1983@list.ru",
}




def home(request):
    # text="""<h1>"Изучаем django"</h1>
    #             <strong>Автор<strong>: <i>Севастьянов В.В.</i>
    #      """
    # return HttpResponse(text)
    return render(request, "index.html")

def about(request):
    result = f"""
    Имя: <b>{author['Имя']}<b><br>
    Отчество: <b>{author['Отчество']}<b><br>
    Фамилия: <b>{author['Фамилия']}<b><br>
    телефон: <b>{author['телефон']}<b><br>
    email: <b>{author['email']}<b><br>
    """
    return HttpResponse(result)
