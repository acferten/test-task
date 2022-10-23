from django.http import JsonResponse

#
# def error_404(request, exception):
#     message = "Not found"
#     response = JsonResponse(error={"code": 404, "message": message})
#     response.status_code = 404
#     return response
#
#
# def error_500(request):
#     message = "An error occured, its on us"
#     response = JsonResponse(error={"code": 500, "message": message})
#     response.status_code = 500
#     return response
