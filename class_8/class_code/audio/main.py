from openai import OpenAI
import pyaudio
import wave
import tempfile
import os
import time

# Initialize OpenAI client
client = OpenAI()

def record_audio(duration=5, sample_rate=44100):
    """Record audio from microphone for specified duration"""
    # Set up audio recording parameters
    chunk = 1024
    audio_format = pyaudio.paInt16
    channels = 1
    
    # Initialize PyAudio
    p = pyaudio.PyAudio()
    
    # Open audio stream
    stream = p.open(format=audio_format,
                   channels=channels,
                   rate=sample_rate,
                   input=True,
                   frames_per_buffer=chunk)
    
    print("Recording...")
    frames = []
    
    # Record audio in chunks
    for _ in range(0, int(sample_rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)
    
    print("Recording finished")
    
    # Clean up
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    return frames, sample_rate

def save_audio_to_temp_file(frames, sample_rate):
    """Save audio frames to a temporary WAV file"""
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
        wf = wave.open(temp_audio.name, 'wb')
        wf.setnchannels(1)  # Mono audio
        wf.setsampwidth(pyaudio.PyAudio().get_sample_size(pyaudio.paInt16))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))
        wf.close()
        return temp_audio.name

def transcribe_audio(audio_file_path):
    """Transcribe audio file using OpenAI Whisper"""
    with open(audio_file_path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
    return transcript.text

def main():
    try:
        while True:
            # 1. Record audio
            frames, sample_rate = record_audio(duration=5)
            
            # 2. Save to temporary file
            temp_audio_file = save_audio_to_temp_file(frames, sample_rate)
            
            # 3. Transcribe audio
            transcript = transcribe_audio(temp_audio_file)

            print(transcript)
            
            print("\nPress Ctrl+C to stop")
            
            # 6. Clean up temporary file
            os.remove(temp_audio_file)
            user_input = input("Do you want to record again? (yes/no - default yes): ").strip().lower()
            if user_input != 'yes' and user_input != '':
                break
    except KeyboardInterrupt:
        print("\nStopping...")

if __name__ == "__main__":
    main()