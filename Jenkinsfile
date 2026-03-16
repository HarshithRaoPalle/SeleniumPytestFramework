pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\harsh\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:\\Users\\harsh\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" -m pytest -v'
            }
        }

    }
}
