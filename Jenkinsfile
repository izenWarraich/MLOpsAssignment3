pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("flask-app:${env.BUILD_NUMBER}")
                }
            }
        }
        
        stage('Test') {
            steps {
                sh 'echo "Running tests..."'
                // Add your test commands here
            }
        }
        
        stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh 'kubectl apply -f kubernetes/deployment.yaml'
                    sh 'kubectl apply -f kubernetes/service.yaml'
                }
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
}

