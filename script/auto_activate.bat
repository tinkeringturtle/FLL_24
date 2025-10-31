@echo off
REM Auto-activate Python virtual environment
if exist "%~dp0..\.venv\Scripts\activate.bat" (
    call "%~dp0..\.venv\Scripts\activate.bat"
    echo [OK] Python environment activated
) else (
    echo [WARNING] Python environment not found. Run the Bootstrap task first.
)
