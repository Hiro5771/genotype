// Jenkinsfile

pipeline {
    agent any
    stages {
        stage('Pythonのインストール') {
            steps {
                // ChocolateyでPythonをインストール（既にインストール済みならスキップ）
                bat 'choco install python -y'
            }
        }
        stage('pipのアップグレード') {
            steps {
                // pipを最新版にアップグレード
                bat 'python -m pip install --upgrade pip'
            }
        }
        stage('uvのインストール') {
            steps {
                // uvをインストール
                bat 'pip install uv'
            }
        }
        stage('バージョン確認') {
            steps {
                // Python、pip、uvのバージョンを表示
                bat 'python --version'
                bat 'pip --version'
                bat 'uv --version'
            }
        }
    }
}
