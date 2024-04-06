from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ErrorCodeModel
from .ser import ErrorCodeSerializer

def home(request):
	return render(request, 'home.html')


class ErrorCodeList(generics.ListAPIView):
	queryset = ErrorCodeModel.objects.all()
	serializer_class = ErrorCodeSerializer


class ErrorCodeMeaning(generics.RetrieveAPIView):
	queryset = ErrorCodeModel.objects.all()
	serializer_class = ErrorCodeSerializer


@api_view(["GET"])
def error_code_meaning(request, code):
	code_str = str(code)
	
	if not code_str.isdigit():
		return JsonResponse({"error": "Error code should be an integer only!!!"}, status=status.HTTP_400_BAD_REQUEST)
	
	code = int(code_str)


	if code < 400 or code >= 600:
		return JsonResponse({"error": "Error code must be in the range of 400-599."}, status=status.HTTP_400_BAD_REQUEST)
	
	
	try:
		error_code = ErrorCodeModel.objects.get(code=code)
		ser = ErrorCodeSerializer(error_code)
		return Response(ser.data)
	except ErrorCodeModel.DoesNotExist:
		return Response({"error": "Error code not found."}, status=status.HTTP_404_NOT_FOUND)
	except ValueError:
		return Response({"error": "Invalid error code."}, status=status.HTTP_400_BAD_REQUEST)

def req_error_codes():
	error_codes = [
		{"code": 404, "meaning": "Page Not Found"},
		{"code": 500, "meaning": "Internal Server Error"},
		{"code": 403, "meaning": "Page Forbidden"},
		{"code": 401, "meaning": "Unauthorized"},
		{"code": 400, "meaning": "Bad Request"},
		{"code": 503, "meaning": "Service Unavailable"},
		{"code": 502, "meaning": "Bad Gateway"},
		{"code": 408, "meaning": "Request Timeout"},
		{"code": 429, "meaning": "Too Many Requests"},
		{"code": 405, "meaning": "Method Not Allowed"}
	]

	for data in error_codes:
		code = data["code"]
		meaning = data["meaning"]

# Check if ErrorCodeModel object already exists
		if ErrorCodeModel.objects.filter(code=code).exists():
			print("Error code " + str(code) + " already exists!!!")
			continue

# Create ErrorCodeModel object if it doesn't exist
		ErrorCodeModel.objects.create(code=code, meaning=meaning)

	print("Error codes setup completed.")
req_error_codes()