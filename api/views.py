from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
import io
import azure.cognitiveservices.speech as speechsdk

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
        audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
        synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
        result = synthesizer.speak_text_async("გია").get()

        # Check if the synthesis succeeded
        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            # If successful, retrieve the audio data stream
            audio_data = result.audio_data

            # Create the response with the audio data
            response = HttpResponse(audio_data, content_type="audio/wav")
            response['Content-Disposition'] = 'attachment; filename="speech.wav"'
            return response
        else:
            # If there was an error during synthesis
            return HttpResponse("Speech synthesis failed.", status=500)