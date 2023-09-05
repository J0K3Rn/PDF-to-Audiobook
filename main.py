from google.cloud import texttospeech
from PyPDF2 import PdfReader
import tkinter
from tkinter import filedialog


def synthesize_text(text):
    """Synthesizes speech from the input string of text."""

    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.SynthesisInput(text=text)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Standard-C",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        request={"input": input_text, "voice": voice, "audio_config": audio_config}
    )

    # The response's audio_content is binary.
    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')


def main():
    tkinter.Tk().withdraw()  # prevents an empty tkinter window from appearing

    file = filedialog.askopenfilename()
    try:
        reader = PdfReader(file)
        number_of_pages = len(reader.pages)
        text = ''
        for index in range(number_of_pages):
            page = reader.pages[index]
            text += page.extract_text()
        synthesize_text(text)
    except FileNotFoundError:
        print(f"{file} not found!")


if __name__ == "__main__":
    main()
