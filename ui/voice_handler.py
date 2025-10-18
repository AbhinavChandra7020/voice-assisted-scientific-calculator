
class VoiceHandler:
    
    def __init__(self, parent):
        self.parent = parent
        self.is_recording = False
        
        self.voice_available = False
        try:
            from voice_mode import AudioRecorder, SpeechToText, VoiceParser
            self.recorder = AudioRecorder(sample_rate=16000)
            self.stt = SpeechToText(model_size='base')
            self.parser = VoiceParser(model='gemma3:4b')
            self.voice_available = True
        except Exception as e:
            print(f"Voice features unavailable: {e}")
    
    def toggle_voice_input(self):
        """Toggle voice recording"""
        if not self.voice_available:
            return
            
        self.is_recording = not self.is_recording
        
        if self.is_recording:
            self.parent.voice_btn.config(bg='#ff4444', text="⏺ RECORDING...")
            self.parent.voice_indicator.config(fg='#ff0000')
            self.parent.root.after(100, self.process_voice_input)
        else:
            self.parent.voice_btn.config(bg='#4a4a4a', text="🎤 VOICE INPUT")
            self.parent.voice_indicator.config(fg='#00ff00')
    
    def process_voice_input(self):
        """Process voice input in background"""
        if not self.is_recording:
            return
            
        try:
            # Record audio
            audio_file = self.recorder.record(duration=5, filename="temp_audio.wav")
            
            # Transcribe
            self.parent.voice_btn.config(text="🔄 Transcribing...")
            self.parent.root.update()
            transcribed = self.stt.transcribe(audio_file)
            
            # Parse
            self.parent.voice_btn.config(text="🧠 Parsing...")
            self.parent.root.update()
            parsed = self.parser.parse(transcribed)
            
            # Insert
            self.parent.display.expression_entry.delete(0, 'end')
            self.parent.display.expression_entry.insert(0, parsed)
            self.parent.on_entry_change()
            
            # Auto-calculate
            self.parent.root.after(500, self.parent.calculate_result)
            
        except Exception as e:
            self.parent.display.result_display.config(state='normal')
            self.parent.display.result_display.delete('1.0', 'end')
            self.parent.display.result_display.insert('1.0', f"Voice Error:\n{str(e)[:50]}")
            self.parent.display.result_display.config(state='disabled')
        finally:
            self.is_recording = False
            self.parent.voice_btn.config(bg='#4a4a4a', text="🎤 VOICE INPUT")
            self.parent.voice_indicator.config(fg='#00ff00')