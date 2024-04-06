from .models import ErrorCodeModel
from rest_framework import serializers

class ErrorCodeSerializer(serializers.ModelSerializer):
	class Meta:
		model = ErrorCodeModel
		fields ="__all__"

	def validate_code(self, value):
		if not value.isdigit():
			raise serializers.ValidationError("Error code must be an integer!!!")
		
		code = int(value)

		if code < 400 or code >= 600:
			raise serializers.ValidationError("Error code must be in the range of 400-600!!!")
		return value