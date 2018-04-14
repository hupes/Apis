from django.http import HttpResponse, JsonResponse
from django.shortcuts import render_to_response

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from cores import excSql


# region 接口首页
def index(request):
    data = "欢迎使用api接口管理平台"
    # data = serializers.serialize("json", data, ensure_ascii=False)

    return HttpResponse(data, content_type='application/json; charset=utf-8')


# endregion

# region 原生的sql 查询
def test_excSql(request):
    data = excSql.my_custom_sql('select * from django_migrations', None)

    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


# endregion

# region 当找不到页面的时候返回
@csrf_exempt
def page_not_found(request):
    return render_to_response('404.html')


# endregion

# region 当服务器发生错误的时候返回的页面
@csrf_exempt
def page_error(request):
    return render_to_response('500.html')

# endregion
