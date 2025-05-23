@echo off
REM Run this script inside Redactify_lux folder

REM Create backend folders
mkdir backend\app

REM Create backend files
echo. > backend\app\main.py
echo. > backend\app\models.py
echo. > backend\app\classify.py
echo. > backend\app\redact.py
echo. > backend\app\utils.py
echo. > backend\requirements.txt
echo. > backend\Dockerfile

REM Create frontend folders
mkdir frontend\public
mkdir frontend\src\components
mkdir frontend\src\styles

REM Create frontend files
echo. > frontend\src\App.jsx
echo. > frontend\tailwind.config.js
echo. > frontend\vite.config.js
echo. > frontend\package.json

REM Create models folder and file
mkdir models
echo. > models\classifier.pkl

REM Create sample_docs folder and file
mkdir sample_docs
echo. > sample_docs\sample_invoice.pdf

REM Create scripts folder and file
mkdir scripts
echo. > scripts\train_classifier.ipynb



echo Folder and file structure created!
pause
