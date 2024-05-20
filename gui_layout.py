from PyQt5.QtWidgets import QVBoxLayout, QLabel, QPushButton, QComboBox, QTextEdit, QHBoxLayout, QFileDialog, QWidget
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QSize

def create_layout(main_window):
    layout = QVBoxLayout()

    # Modellauswahl
    model_layout = QVBoxLayout()
    main_window.model_label = QLabel("Wähle das passende Whisper-Modell:")
    main_window.model_label.setFont(QFont("Arial", 14))
    main_window.model_label.setAlignment(Qt.AlignCenter)
    model_layout.addWidget(main_window.model_label)

    main_window.model_combo = QComboBox()
    main_window.model_combo.addItems(["tiny", "base", "small", "medium", "large"])
    main_window.model_combo.setFont(QFont("Arial", 12))
    main_window.model_combo.setFixedWidth(200)
    main_window.model_combo.setCurrentIndex(2)  # Setze das "small" Modell als Standard
    main_window.model_combo.currentIndexChanged.connect(main_window.update_model)
    model_layout.addWidget(main_window.model_combo, alignment=Qt.AlignCenter)

    layout.addLayout(model_layout)

    # Sprachwahl-Buttons
    language_layout = QHBoxLayout()
    main_window.language_german_button = QPushButton("Deutsch")
    main_window.language_german_button.setFont(QFont("Arial", 14))
    main_window.language_german_button.clicked.connect(lambda: main_window.set_language("de"))
    main_window.language_german_button.setStyleSheet("background-color: lightblue;")
    language_layout.addWidget(main_window.language_german_button)

    main_window.language_auto_button = QPushButton("Sprache automatisch erkennen")
    main_window.language_auto_button.setFont(QFont("Arial", 14))
    main_window.language_auto_button.clicked.connect(lambda: main_window.set_language(None))
    language_layout.addWidget(main_window.language_auto_button, alignment=Qt.AlignCenter)

    main_window.language_english_button = QPushButton("Englisch")
    main_window.language_english_button.setFont(QFont("Arial", 14))
    main_window.language_english_button.clicked.connect(lambda: main_window.set_language("en"))
    language_layout.addWidget(main_window.language_english_button)

    layout.addLayout(language_layout)

    # Statusanzeige
    main_window.status_label = QLabel("Status: Bereit")
    main_window.status_label.setFont(QFont("Arial", 14))
    main_window.status_label.setAlignment(Qt.AlignCenter)
    layout.addWidget(main_window.status_label)

    # Aufnahme- und Dateihochladen-Button
    button_layout = QHBoxLayout()

    # Aufnahme-Button mit Symbol
    main_window.record_button = QPushButton()
    main_window.record_button.setIcon(QIcon("resources/microphone.png"))
    main_window.record_button.setIconSize(QSize(64, 64))
    main_window.record_button.clicked.connect(main_window.toggle_recording)
    button_layout.addWidget(main_window.record_button, alignment=Qt.AlignCenter)

    # Dateihochladen-Button
    main_window.upload_button = QPushButton()
    main_window.upload_button.setIcon(QIcon("resources/hochladen.png"))
    main_window.upload_button.setIconSize(QSize(64, 64))
    main_window.upload_button.clicked.connect(main_window.upload_file)
    button_layout.addWidget(main_window.upload_button, alignment=Qt.AlignCenter)

    layout.addLayout(button_layout)

    # Platz schaffen
    layout.addSpacing(20)

    # Letzte Eingabe
    main_window.transcription_label = QLabel("Letzte Eingabe:")
    main_window.transcription_label.setFont(QFont("Arial", 14))
    layout.addWidget(main_window.transcription_label)

    main_window.text_display = QTextEdit()
    main_window.text_display.setFont(QFont("Arial", 12))
    main_window.text_display.setReadOnly(True)
    layout.addWidget(main_window.text_display)

    # Button zum Anzeigen aller Transkriptionen
    main_window.show_all_button = QPushButton("Alle Chats anzeigen")
    main_window.show_all_button.setFont(QFont("Arial", 14))
    main_window.show_all_button.clicked.connect(main_window.toggle_all_transcriptions)
    layout.addWidget(main_window.show_all_button, alignment=Qt.AlignCenter)

    # Transkriptionsbereich (versteckt, standardmäßig nicht angezeigt)
    main_window.transcription_area = QTextEdit()
    main_window.transcription_area.setFont(QFont("Arial", 12))
    main_window.transcription_area.setVisible(False)
    layout.addWidget(main_window.transcription_area)

    # Hilfe-Button mit Symbol
    main_window.help_button = QPushButton()
    main_window.help_button.setIcon(QIcon("resources/help.png"))
    main_window.help_button.setIconSize(QSize(64, 64))  # Icon um 100% vergrößern
    main_window.help_button.clicked.connect(main_window.show_help)
    layout.addWidget(main_window.help_button, alignment=Qt.AlignCenter)

    widget = QWidget()
    widget.setLayout(layout)
    main_window.setCentralWidget(widget)

