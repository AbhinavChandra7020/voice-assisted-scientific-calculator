
import sounddevice as sd
import soundfile as sf

class AudioRecorder:
    
    def __init__(self, sample_rate=16000):

        self.sample_rate = sample_rate
        print(f"Audio Recorder Ready (Sample Rate: {sample_rate} Hz)")
     
    def record(self, duration=5, filename="temp_audio.wav"):
        print(f"Recording for {duration} seconds...")
        print("   Speak now!")
        
        # Record audio
        audio = sd.rec(
            int(duration * self.sample_rate),
            samplerate=self.sample_rate,
            channels=1, 
            dtype='float32'
        )
        
        sd.wait()
        
        print("✓ Recording complete!")
        
        sf.write(filename, audio, self.sample_rate)
        print(f"✓ Saved to: {filename}")
        
        return filename
