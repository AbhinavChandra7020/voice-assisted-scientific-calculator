
import whisper

class SpeechToText:
    
    def __init__(self, model_size='base'):

        print(f"Loading Whisper model: {model_size}...")
        self.model = whisper.load_model(model_size)
        print(f"✓ Whisper {model_size} model loaded!")
    
    def transcribe(self, audio_file):

        print(f"Transcribing audio...")
        
        # Transcribe with Whisper
        result = self.model.transcribe(audio_file)
        
        # Extract text
        text = result["text"].strip()
        
        print(f"Transcription: \"{text}\"")
        
        return text
