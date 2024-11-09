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
        result = synthesizer.speak_text_async('რატომ')
        audio_data_stream = speechsdk.AudioDataStream(result.get())
        audio_stream = io.BytesIO()

        audio_data_stream.save_to_wav_file("/temp.wav")  # Save it temporarily as a file

        # Now we can read the contents of the temporary file into the BytesIO object
        with open("temp.wav", "rb") as temp_file:
            audio_stream.write(temp_file.read())

        # Rewind the stream to the beginning
        audio_stream.seek(0)

        # Send the audio data as a response
        response = HttpResponse(audio_stream, content_type='audio/wav')
        response['Content-Disposition'] = 'attachment; filename="output.wav"'
        return response