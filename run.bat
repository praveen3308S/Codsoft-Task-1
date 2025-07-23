@echo off
echo Starting ChatBot Flask Application...
echo.

REM Activate virtual environment
call chatbot_env\Scripts\activate

REM Run the Flask application
python app.py