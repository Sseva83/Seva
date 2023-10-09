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

items = [
    {id:1, "name": "Кроссовки abibas" ,"quantity":5},
    {id:2, "name": "Куртка кожанная" ,"quantity":2},
    {id:5, "name": "Coca cola 1литр" ,"quantity":12},
    {id:7, "name": "Картофель фри" ,"quantity":0},
    {id:8, "name": "Кепка" ,"quantity":124},
]



def home(request):
    # text="""<h1>"Изучаем django"</h1>
    #             <strong>Автор<strong>: <i>Севастьянов В.В.</i>
    #      """
    # return HttpResponse(text)
    context = {
        "name": "Севастьянов Всеволод Валерьевич",
        "email": "Seva1983@list.ru"
    }
    return render(request, "index.html", context)

def about(request):
    result = f"""
    Имя: <b>{author['Имя']}<b><br>
    Отчество: <b>{author['Отчество']}<b><br>
    Фамилия: <b>{author['Фамилия']}<b><br>
    телефон: <b>{author['телефон']}<b><br>
    email: <b>{author['email']}<b><br>
    """
    return HttpResponse(result)

# def get_item(request,item_id):
#     # """По указанному id возвращает имя и количество"""
#     # for item in items:
#     #     if item["id"]==id:
#     #         result= f"""
#     #         <h2>Имя:{item["name"]}</h2>
#     #         <p>Количество:{item["quantity"]}</p>
#     # """
#     #     return HttpResponse(result)
#     # return HttpResponseNotFound(f'Item with id={id} not found')

#     context={
#         "items":items
#     }
#     return render(request,"item-list.html", context)

def items_list(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, "items-list.html", context)