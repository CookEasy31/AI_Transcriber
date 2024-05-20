import sys
import traceback
from PyQt5.QtWidgets import QApplication, QMessageBox
from main_window import MainWindow

class SpeechToTextApp(MainWindow):
    def __init__(self):
        super().__init__()

if __name__ == '__main__':
    def excepthook(exc_type, exc_value, exc_traceback):
        if issubclass(exc_type, KeyboardInterrupt):
            sys.__excepthook(exc_type, exc_value, exc_traceback)
            return
        print("Uncaught exception", exc_type, exc_value, exc_traceback)
        QMessageBox.critical(None, "Uncaught Exception",
                             ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback)))
        sys.exit(1)

    sys.excepthook = excepthook

    app = QApplication(sys.argv)
    window = SpeechToTextApp()
    window.show()
    sys.exit(app.exec_())
