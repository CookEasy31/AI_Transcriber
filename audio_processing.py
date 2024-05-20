import whisper
import pyperclip
import torch

def process_audio(self):
    try:
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model = whisper.load_model(self.model_combo.currentText(), device=device)
        result = self.model.transcribe(self.audio_file, language=self.language)
        transcribed_text = result['text']
        self.text_display.setText(transcribed_text)
        self.transcription_area.append(transcribed_text)
        pyperclip.copy(transcribed_text)
        self.status_label.setText("Status: Fertig")
    except Exception as e:
        self.show_error(str(e))
