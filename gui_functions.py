import threading
from PyQt5.QtWidgets import QMessageBox, QFileDialog
import whisper
import torch
from audio_recording import record_audio
from audio_processing import process_audio

def update_model(main_window):
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    main_window.model = whisper.load_model(main_window.model_combo.currentText(), device=device)

def set_language(main_window, language):
    main_window.language = language
    # Farben der Buttons zurücksetzen
    main_window.language_german_button.setStyleSheet("")
    main_window.language_auto_button.setStyleSheet("")
    main_window.language_english_button.setStyleSheet("")

    if language == "de":
        main_window.language_german_button.setStyleSheet("background-color: lightblue;")
    elif language == "en":
        main_window.language_english_button.setStyleSheet("background-color: lightblue;")
    else:
        main_window.language_auto_button.setStyleSheet("background-color: lightblue;")

def toggle_recording(main_window):
    if not main_window.recording:
        start_recording(main_window)
    else:
        stop_recording(main_window)

def start_recording(main_window):
    main_window.recording = True
    main_window.status_label.setText("Status: Aufnahme läuft...")
    main_window.record_thread = threading.Thread(target=record_audio, args=(main_window,))
    main_window.record_thread.start()

def stop_recording(main_window):
    main_window.recording = False
    main_window.status_label.setText("Status: Aufnahme beendet, verarbeite...")
    main_window.record_thread.join()
    process_audio(main_window)
    main_window.status_label.setText("Status: Bereit")

def upload_file(main_window):
    file_dialog = QFileDialog(main_window)
    file_dialog.setFileMode(QFileDialog.ExistingFile)
    file_dialog.setNameFilter("Audio Files (*.wav *.mp3 *.flac *.ogg *.m4a)")
    if file_dialog.exec_():
        file_path = file_dialog.selectedFiles()[0]
        main_window.status_label.setText(f"Status: Datei {file_path} hochgeladen, verarbeite...")
        process_uploaded_file(main_window, file_path)
        main_window.status_label.setText("Status: Bereit")

def process_uploaded_file(main_window, file_path):
    if main_window.model is None:
        main_window.show_error("Das Modell wurde nicht korrekt geladen.")
        return

    try:
        # Führe die Transkription durch und übergebe den Dateipfad
        result = main_window.model.transcribe(file_path)

        # Setze den transkribierten Text in das Textfeld
        main_window.text_display.setPlainText(result["text"])

    except Exception as e:
        main_window.show_error(str(e))

def show_help(main_window):
    help_text = """
    <h1 style="font-size: 18pt;">Hilfe</h1>

    <h2 style="font-size: 16pt;">Modellauswahl</h2>
    <p style="font-size: 14pt;">Wähle das Whisper-Modell aus der Dropdown-Liste.</p>
    <p style="font-size: 14pt;"><strong>Modelle und Ressourcenbedarf:</strong></p>
    <ul style="font-size: 14pt;">
        <li><strong>tiny:</strong> Benötigt wenig Ressourcen, läuft auf den meisten Computern.</li>
        <li><strong>base:</strong> Moderater Ressourcenbedarf.</li>
        <li><strong>small:</strong> Erfordert mehr Leistung, ideal mit einer GPU.</li>
        <li><strong>medium:</strong> Hoher Ressourcenbedarf, GPU empfohlen.</li>
        <li><strong>large:</strong> Sehr hoher Ressourcenbedarf, GPU erforderlich.</li>
    </ul>

    <h2 style="font-size: 16pt;">Sprachwahl</h2>
    <p style="font-size: 14pt;">Wähle die gewünschte Sprache für die Transkription (Deutsch, Englisch) oder lass die Sprache automatisch erkennen.</p>

    <h2 style="font-size: 16pt;">Aufnahme-Button</h2>
    <p style="font-size: 14pt;">Klicke auf das Mikrofonsymbol, um die Aufnahme zu starten. Der Button wechselt die Farbe, wenn die Aufnahme läuft.</p>

    <h2 style="font-size: 16pt;">Datei-Upload-Button</h2>
    <p style="font-size: 14pt;">Klicke auf das Hochladen-Symbol, um eine Audiodatei auszuwählen und hochzuladen. Die Datei wird automatisch transkribiert, und der Text wird angezeigt.</p>

    <h2 style="font-size: 16pt;">Letzte Eingabe</h2>
    <p style="font-size: 14pt;">Zeigt den zuletzt transkribierten Text an.</p>

    <h2 style="font-size: 16pt;">Alle Chats anzeigen</h2>
    <p style="font-size: 14pt;">Zeigt alle vergangenen Transkriptionen an.</p>

    <h2 style="font-size: 16pt;">Hilfe-Button</h2>
    <p style="font-size: 14pt;">Zeigt diese Hilfsinformationen an.</p>
    """
    # Create a custom message box with increased width
    msg_box = QMessageBox(main_window)
    msg_box.setWindowTitle("Hilfe")
    msg_box.setText(help_text)
    msg_box.setStyleSheet("QLabel{min-width: 600px;}")  # Increase the width by 50%
    msg_box.exec_()


def toggle_all_transcriptions(main_window):
    main_window.transcription_area.setVisible(not main_window.transcription_area.isVisible())

def show_error(main_window, message):
    error_dialog = QMessageBox()
    error_dialog.setIcon(QMessageBox.Critical)
    error_dialog.setText("Ein Fehler ist aufgetreten")
    error_dialog.setInformativeText(message)
    error_dialog.setWindowTitle("Fehler")
    error_dialog.exec_()
