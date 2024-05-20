import os
import subprocess
import sys

# Verzeichnis deines Projekts
project_dir = "C:\\Users\\matth\\Downloads\\AI_Transcriber"

def generate_requirements(directory):
    try:
        # Navigiere in das Projektverzeichnis
        os.chdir(directory)
        
        # Überprüfe, ob pipreqs installiert ist, wenn nicht, installiere es
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pipreqs'])
        
        # Generiere die requirements.txt Datei
        subprocess.check_call(['pipreqs', '.', '--force'])
        print("requirements.txt erfolgreich generiert.")
    except Exception as e:
        print(f"Fehler bei der Generierung der requirements.txt: {e}")

if __name__ == "__main__":
    generate_requirements(project_dir)
