from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.response import TemplateResponse
import requests
import json
from django.http import JsonResponse
from django.core import serializers
# import JSON
# Create your views here.


def all_list(request, *args, **kwargs):
    r = requests.get('https://o136z8hk40.execute-api.us-east-1.amazonaws.com/dev/get-list-of-conferences')
    res = r.text
    # json_str = json.dumps(res)
    json_data = json.loads(res)
    # data = eval(json_data)
    # json_pretty = json.dumps(json_data,sort_keys=True,indent=4)
    # context = {
        # "free_lists": json_data["free"],
        # "paid_lists": json_data["paid"]
    # }
    # for x in json_data["free"]:
    #     for key,val in x.items():
    #         print(key)
    #     break
    # print(type(json_data))
    # return HttpResponse("nothing")
    return render(request, "list.html", context={"lists": json_data["paid"], "vals": json_data["free"]})
    # return TemplateResponse(request, 'list.html', {'lists': json_data["free"]})
#