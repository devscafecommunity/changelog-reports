@echo off
REM Ativa o ambiente virtual e executa o changelog-report
cd /d %~dp0
if exist .venv\Scripts\activate.bat (
    call .venv\Scripts\activate.bat
)
python .
pause
