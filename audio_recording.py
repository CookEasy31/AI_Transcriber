import pyaudio
import wave

def record_audio(self):
    try:
        audio = pyaudio.PyAudio()
        stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
        frames = []
        while self.recording:
            data = stream.read(1024)
            frames.append(data)
        stream.stop_stream()
        stream.close()
        audio.terminate()
        with wave.open(self.audio_file, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
            wf.setframerate(44100)
            wf.writeframes(b''.join(frames))
        self.status_label.setText("Status: Aufnahme abgeschlossen")
    except Exception as e:
        self.show_error(str(e))
