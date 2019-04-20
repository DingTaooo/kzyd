# Create your views here.

from django.shortcuts import HttpResponse
from apps.users import models
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# 导入models模块
def orm(request):
    # 创建数据
    # 第一种方式
    models.UserInfo.objects.create(username="root", password="123456")
    # 第二种方式
    # obj = models.UserInfo(username='dt', password="123")
    # obj.save()
    # result = models.UserInfo.objects.all()  # 查询所有，为QuerySet类型，可理解成列表

    # 删除数据
    #     models.UserInfo.objects.all().delete()  # 删除所有

    # 更新数据
    # models.UserInfo.objects.all().update(password=8888)
    # models.UserInfo.objects.filter(id=3).update(password=888888)

    return HttpResponse('orm')


@csrf_exempt
def test_api(request):
    return JsonResponse({"result": 0, "msg": "执行成功"})

def get_book(request):
    books_list = models.Books.objects.all()
    print(books_list)
    return books_list