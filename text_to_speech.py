from google.cloud import texttospeech

def synthesize_text(text, output_file_path="output.mp3", language_code="en-US"):
    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code=language_code,
        name="en-US-Wavenet-D",
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL,
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16
    )

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    with open(output_file_path, "wb") as out_file:
        out_file.write(response.audio_content)

# Example usage
#response_text = "Hello, this is a sample response from the language model."
#synthesize_text(response_text, "output.mp3")
