// Jenkinsfile

pipeline {
    agent any
    stages {
        stage('install Python') {
            steps {
                // ChocolateyでPythonをインストール（既にインストール済みならスキップ）
                bat 'choco install python -y'
            }
        }
        stage('upgrade pip') {
            steps {
                // pipを最新版にアップグレード
                bat 'python -m pip install --upgrade pip'
            }
        }
        stage('install uv') {
            steps {
                // uvをインストール
                bat 'pip install uv'
            }
        }
        stage('check versions') {
            steps {
                // Python、pip、uvのバージョンを表示
                bat 'python --version'
                bat 'pip --version'
                bat 'uv --version'
            }
        }
        stage('run uv pyinstaller') {
            steps {
                // create main.exe using uv
                bat 'uv run pyinstaller --onefile --noconsole main.py'
                echo 'successfully created main.exe'
            }
        }
    }
}
