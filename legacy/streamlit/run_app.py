import subprocess
import sys
import os

def install_requirements():
    print("Installing requirements...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    except subprocess.CalledProcessError as e:
        print(f"Error installing requirements: {e}")
        sys.exit(1)

def run_app():
    print("Starting app...")
    app_path = os.path.join("app", "app.py")
    if not os.path.exists(app_path):
        print(f"Error: {app_path} not found!")
        sys.exit(1)
        
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", app_path])
    except KeyboardInterrupt:
        print("\nStopping app...")

if __name__ == "__main__":
    if os.path.exists("requirements.txt"):
        install_requirements()
    else:
        print("Warning: requirements.txt not found. Skipping installation.")
    
    run_app()
