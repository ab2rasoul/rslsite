from django.http import HttpResponse, JsonResponse

def http_test(request):
    return HttpResponse('<h1>this is a test.</h1>')


def json_test(request):
    return JsonResponse({'name':'Ali'})

def leader1(request):
    return HttpResponse("The manager is up to changes.")

def player1(request):
    return JsonResponse({"1st player":"Yahya Ghane"})