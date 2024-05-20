from PyQt5.QtWidgets import QMainWindow, QMessageBox
import gui_layout
import gui_functions

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Speech to Text Application")
        self.setGeometry(100, 100, 1200, 600)

        # Initialisierung von Aufnahme- und Transkriptionszustand
        self.recording = False
        self.audio_file = "audio.wav"
        self.model = None
        self.language = "de"  # Standardmäßig Deutsch

        # Layout erstellen
        gui_layout.create_layout(self)
        self.update_model()

    def update_model(self):
        gui_functions.update_model(self)

    def set_language(self, language):
        gui_functions.set_language(self, language)

    def toggle_recording(self):
        gui_functions.toggle_recording(self)

    def start_recording(self):
        gui_functions.start_recording(self)

    def stop_recording(self):
        gui_functions.stop_recording(self)

    def upload_file(self):
        gui_functions.upload_file(self)

    def process_uploaded_file(self, file_path):
        if self.model is not None:
            gui_functions.process_uploaded_file(self, file_path)
        else:
            self.show_error("Model konnte nicht geladen werden. Bitte versuche es erneut.")

    def show_help(self):
        gui_functions.show_help(self)

    def toggle_all_transcriptions(self):
        gui_functions.toggle_all_transcriptions(self)

    def show_error(self, message):
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setText("Ein Fehler ist aufgetreten")
        error_dialog.setInformativeText(message)
        error_dialog.setWindowTitle("Fehler")
        error_dialog.exec_()
