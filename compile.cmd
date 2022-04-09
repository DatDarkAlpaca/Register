@echo off
.\venv\Scripts\pyside6-uic.exe res/ui/main_window.ui -o res/compiled/main_window.py
.\venv\Scripts\pyside6-uic.exe res/ui/list_users_window.ui -o res/compiled/list_users_window.py
.\venv\Scripts\pyside6-uic.exe res/ui/register_window.ui -o res/compiled/register_window.py