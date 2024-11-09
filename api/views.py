import os

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
import io
import azure.cognitiveservices.speech as speechsdk
from django.conf import settings
from django.templatetags.static import static
import os
from pydub import AudioSegment
from pydub.playback import play

# Create your views here.
@csrf_exempt
def get_voice(request):
    return JsonResponse({"sdfsd":'dfgdfgdfg'})

def play_audio_from_bytes(audio_data,format='wave'):
    audio_Data_io = io.BytesIO(audio_data)
    audio_Segment = AudioSegment.from_file(audio_Data_io, format=format)
    play(audio_Segment)
@csrf_exempt
def my_api_view(request):
    if request.method == "GET":  # or 'GET'
        subscription_key = "1leCCsjzYrtC8b8xUcpyjTCUQszkq64JcUmJsUqes0ucLXRIh0L5JQQJ99AJACYeBjFXJ3w3AAAYACOGEWz6"
        region = "eastus"
        speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=region)
        speech_config.speech_synthesis_voice_name = "ka-GE-EkaNeural"

        # Set up the audio output configuration to use the in-memory stream
        audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
        # Synthesize speech
        synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
        result = synthesizer.speak_text_async('და')
        if result.get().reason == synthesizer.ResultReason.SynthesizingAudioCompleted:
            result.get()
            audio_data = result.get().audio_data
            play_audio_from_bytes(audio_data)
            with open("output.wave", "wb") as file:
                file.write(audio_data)

            audio_stream = io.BytesIO()

            # Check the result of speech synthesis (you can also handle errors here)

            # Rewind to the start of the stream
            audio_stream.seek(0)

            # Send the audio data as a response for download
            response = HttpResponse(audio_stream, content_type='audio/wave')
            response['Content-Disposition'] = 'attachment; filename="output.wave"'
            return response


