"""
Standalone Voice Calculator
Run this file for voice-only mode: python voice_calculator.py
"""

from voice_mode.audio_recorder import AudioRecorder
from voice_mode.speech_to_text import SpeechToText
from voice_mode.llm_parser import VoiceParser
from calculator import calculate


class VoiceCalculator:
    
    def __init__(self, whisper_model='base', llm_model='gemma3:4b', sample_rate=16000):
        """Initialize the voice calculator pipeline"""
        
        print("\n" + "="*60)
        print("VOICE CALCULATOR")
        print("="*60)
        
        # Initialize components
        self.recorder = AudioRecorder(sample_rate=sample_rate)
        self.stt = SpeechToText(model_size=whisper_model)
        self.parser = VoiceParser(model=llm_model)
        
        print("\n✓ Voice Calculator Ready!")
        print("="*60 + "\n")
    
    def process_voice_input(self, duration=5, audio_file="temp_audio.wav"):
        """Complete pipeline: Record → Transcribe → Parse → Calculate"""
        
        print("\n" + "-"*60)
        print("VOICE CALCULATION")
        print("-"*60)
        
        # Step 1: Record audio
        print("\n[1/4] Recording audio...")
        self.recorder.record(duration=duration, filename=audio_file)
        
        # Step 2: Transcribe speech to text
        print("\n[2/4] Transcribing speech...")
        transcribed_text = self.stt.transcribe(audio_file)
        
        # Step 3: Parse natural language to calculator syntax
        print("\n[3/4] Parsing expression...")
        calc_expression = self.parser.parse(transcribed_text)
        print(f"Calculator Expression: {calc_expression}")
        
        # Step 4: Calculate result
        print("\n[4/4] Calculating...")
        result = calculate(calc_expression)
        
        print("\n" + "-"*60)
        print("RESULTS")
        print("-"*60)
        print(f"You said: \"{transcribed_text}\"")
        print(f"Expression: {calc_expression}")
        print(f"Result: {result}")
        print("-"*60 + "\n")
        
        return {
            'transcription': transcribed_text,
            'expression': calc_expression,
            'result': result
        }
    
    def interactive_mode(self, duration=5):
        """Run in interactive mode - continuous voice calculations"""
        
        print("\n" + "="*60)
        print("VOICE CALCULATOR - INTERACTIVE MODE")
        print("="*60)
        print("\nSpeak your math problem after pressing ENTER")
        print("Type 'quit' to exit\n")
        
        while True:
            user_input = input("Press ENTER to record (or 'quit' to exit): ").strip().lower()
            
            if user_input in ['quit', 'exit', 'q']:
                print("\n✓ Goodbye!")
                break
            
            try:
                self.process_voice_input(duration=duration)
            except KeyboardInterrupt:
                print("\n\n✓ Interrupted. Goodbye!")
                break
            except Exception as e:
                print(f"\n✗ Error: {e}")
                print("Try again...\n")


if __name__ == "__main__":
    
    # Initialize voice calculator
    voice_calc = VoiceCalculator(
        whisper_model='base',      # Options: 'tiny', 'base', 'small', 'medium', 'large'
        llm_model='gemma3:4b',     # Your Ollama model
        sample_rate=16000
    )
    
    # Run in interactive mode
    voice_calc.interactive_mode(duration=5)