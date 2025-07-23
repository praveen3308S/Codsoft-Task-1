@echo off
echo Setting up ChatBot Flask Application...
echo.

REM Create virtual environment
echo Creating virtual environment...
python -m venv chatbot_env

REM Activate virtual environment
echo Activating virtual environment...
call chatbot_env\Scripts\activate

REM Install required packages
echo Installing required packages...
pip install -r requirements.txt

echo.
echo Setup complete! 
echo.
echo To run the application:
echo 1. Activate the virtual environment: chatbot_env\Scripts\activate
echo 2. Run the Flask app: python app.py
echo 3. Open your browser and go to: http://127.0.0.1:5000
echo.
pause