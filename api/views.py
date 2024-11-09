import os

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
import io
import azure.cognitiveservices.speech as speechsdk
from django.conf import settings
from django.templatetags.static import static
import os
# Create your views here.
@csrf_exempt
def get_voice(request):
    return JsonResponse({"sdfsd":'dfgdfgdfg'})
@csrf_exempt
def my_api_view(request):
    if request.method == "GET":  # or 'GET'

        audio_stream = io.BytesIO()
        static_file_path = os.path.join(settings.BASE_DIR, 'staticfiles', 'temp.wav')


        # Now we can read the contents of the temporary file into the BytesIO object
        with open(static_file_path, "rb") as temp_file:
            audio_stream.write(temp_file.read())

        # Rewind the stream to the beginning
        audio_stream.seek(0)

        # Send the audio data as a response
        response = HttpResponse(audio_stream, content_type='audio/wav')
        response['Content-Disposition'] = 'attachment; filename="output.wav"'
        return response