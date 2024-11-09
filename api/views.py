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
        subscription_key = "1leCCsjzYrtC8b8xUcpyjTCUQszkq64JcUmJsUqes0ucLXRIh0L5JQQJ99AJACYeBjFXJ3w3AAAYACOGEWz6"
        region = "eastus"
        speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=region)
        speech_config.speech_synthesis_voice_name = "ka-GE-EkaNeural"

        synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
       # result = synthesizer.speak_text_async('და').get()
        #audio_data_stream = speechsdk.AudioDataStream(result)
        audio_stream = io.BytesIO()
        static_file_path = os.path.join(settings.BASE_DIR, 'staticfiles', 'temp.wav')
        #audio_data_stream.save_to_wav_file(static_file_path)  # Save it temporarily as a file

        # Now we can read the contents of the temporary file into the BytesIO object
        with open(static_file_path, "rb") as temp_file:
            audio_stream.write(temp_file.read())

        # Rewind the stream to the beginning
        audio_stream.seek(0)

        # Send the audio data as a response
        response = HttpResponse(audio_stream, content_type='audio/wav')
        response['Content-Disposition'] = 'attachment; filename="output.wav"'
        return response