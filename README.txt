# AI Transcriber

This project is an AI-based transcription tool that utilizes OpenAI's Whisper model to convert speech to text. It is built using Python and various libraries such as PyQt5, PyAudio, Torch, and more.

## Features
- Transcribes speech to text in real-time
- Easy-to-use graphical user interface
- Supports multiple audio input sources

## Requirements
- Python 3.12 or higher
- Virtual environment (venv)
- Internet connection (for initial setup and dependencies)

## Installation

1. **Clone the repository:**
    ```
    git clone https://github.com/DeinBenutzername/AI_Transcriber.git
    cd AI_Transcriber
    ```

2. **Create a virtual environment and activate it:**
    ```
    python -m venv venv
    .\\venv\\Scripts\\activate
    ```

3. **Install the required dependencies:**
    ```
    pip install -r requirements.txt
    ```

## Usage

1. **Activate the virtual environment:**
    ```
    .\\venv\\Scripts\\activate
    ```

2. **Run the application:**
    ```
    python main.py
    ```

## Files and Directories

- `main.py`: The main script to run the application.
- `requirements.txt`: Lists all the dependencies required to run the project.
- `resources/`: Contains icon and image files used in the application.
- `venv/`: The virtual environment directory.
- `whisper/`: Directory containing Whisper model assets.

## Troubleshooting

If you encounter issues related to missing DLL files or other dependencies, ensure that the required libraries are correctly installed and that your PATH environment variable includes necessary directories.

## Contributing

Feel free to fork this repository and contribute by submitting pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgements

- OpenAI for the Whisper model
- Contributors to PyQt5, PyAudio, Torch, and other libraries used in this project
"""