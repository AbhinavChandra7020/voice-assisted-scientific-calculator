from calculator import calculate
from calculator.utils.angle_modes import angle_mode

# Voice components - optional import
try:
    from voice_mode.audio_recorder import AudioRecorder
    from voice_mode.speech_to_text import SpeechToText
    from voice_mode.llm_parser import VoiceParser
    VOICE_AVAILABLE = True
except ImportError:
    VOICE_AVAILABLE = False


class CLI:
    
    def __init__(self, enable_voice=True):
        """Initialize calculator CLI with optional voice support"""
        
        self.running = True
        
        # Initialize voice components if available and requested
        self.voice_enabled = False
        if enable_voice and VOICE_AVAILABLE:
            try:
                print("Initializing voice support...")
                self.recorder = AudioRecorder(sample_rate=16000)
                self.stt = SpeechToText(model_size='base')
                self.parser = VoiceParser(model='gemma3:4b')
                self.voice_enabled = True
                print("✓ Voice support enabled!\n")
            except Exception as e:
                print(f"⚠ Voice support unavailable: {e}\n")
                self.voice_enabled = False
    
    def print_banner(self):
        """Display welcome banner"""
        print("Scientific Calculator")
        if self.voice_enabled:
            print("Voice Support: ENABLED ✓")
        print("Commands:")
        print("  'deg' or 'rad' - Switch angle mode")
        print("  'mode' - Show current angle mode")
        if self.voice_enabled:
            print("  'voice' - Use voice input")
        print("  'quit' or 'exit' - Close calculator")
        print("=" * 40)
        print(f"Current mode: {angle_mode.get_mode()}")
    
    def handle_voice_input(self, duration=5):
        """Handle voice calculation"""
        
        if not self.voice_enabled:
            print("⚠ Voice support is not available")
            return
        
        print("\n" + "-"*50)
        print("VOICE INPUT MODE")
        print("-"*50)
        
        try:
            # Step 1: Record audio
            print(f"\n[1/4] Recording for {duration} seconds...")
            print("   Speak now!")
            audio_file = self.recorder.record(duration=duration, filename="temp_audio.wav")
            
            # Step 2: Transcribe
            print("\n[2/4] Transcribing speech...")
            transcribed_text = self.stt.transcribe(audio_file)
            
            # Step 3: Parse to calculator expression
            print("\n[3/4] Parsing expression...")
            calc_expression = self.parser.parse(transcribed_text)
            print(f"Expression: {calc_expression}")
            
            # Step 4: Calculate
            print("\n[4/4] Calculating...")
            result = calculate(calc_expression)
            
            # Display result
            print("\n" + "-"*50)
            print(f"You said: \"{transcribed_text}\"")
            print(f"Expression: {calc_expression}")
            print(f"Result: {result}")
            print("-"*50)
            
        except Exception as e:
            print(f"\n✗ Voice calculation error: {e}")
    
    def run(self):
        """Main CLI loop"""
        
        self.print_banner()
        
        while self.running:
            try:
                expression = input("\n>>> ").strip()
                
                # Skip empty input
                if not expression:
                    continue
                
                # Exit commands
                if expression.lower() in ['quit', 'exit']:
                    print("Goodbye!")
                    break
                
                # Voice input
                if expression.lower() in ['voice', 'v']:
                    self.handle_voice_input(duration=5)
                    continue
                
                # Angle mode - degrees
                if expression.lower() == 'deg':
                    angle_mode.set_mode('DEG')
                    print(f"Mode set to: DEGREES")
                    continue
                
                # Angle mode - radians
                if expression.lower() == 'rad':
                    angle_mode.set_mode('RAD')
                    print(f"Mode set to: RADIANS")
                    continue
                
                # Show current mode
                if expression.lower() == 'mode':
                    print(f"Current mode: {angle_mode.get_mode()}")
                    continue
                
                # Calculate expression
                result = calculate(expression)
                print(f"= {result}")
            
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except EOFError:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")


def run_cli(enable_voice=True):
    """Entry point for CLI"""
    cli = CLI(enable_voice=enable_voice)
    cli.run()


if __name__ == "__main__":
    run_cli(enable_voice=True)