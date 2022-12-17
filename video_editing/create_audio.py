from gtts import gTTS
import re

# Use the gTTS library to convert the text to speech
def get_audio_file(heading,summary,file_name,folder='store_data'):
    text = f"{heading}.\n {summary}"
    pattern = re.compile(r"[^a-zA-Z0-9\s]|^\s|\s$")
    text = pattern.sub('', text)
    # text  = re.sub("[^0-9a-zA-Z]+"," ",text)
    print(f'Audio Created for: {text}')
    speech = gTTS(text=text, lang="en",tld='co.in',slow=False,lang_check=False)
    speech.voice = "en-uk-north"
    audio_file = f"{folder}/audio_files/audio_{file_name}.mp3"
    speech.save(audio_file)
    return audio_file

if __name__ == "__main__":
    heading = 'Automation'
    summary = "Hello, this is a test of creating video and audio from text using Python"
    file_name = 'file_name'
    get_audio_file(heading,summary,file_name)