from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse
from backend import models
# 导入models模块
def orm(request):
# 创建数据
    # 第一种方式
    models.UserInfo.objects.create(username="root", password="123")
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