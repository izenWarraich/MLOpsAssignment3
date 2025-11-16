pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'flask-k8s-app'
        DOCKER_TAG = 'latest'
    }
    
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    echo 'Building Docker image...'
                    sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
                    echo "Docker image ${DOCKER_IMAGE}:${DOCKER_TAG} built successfully"
                }
            }
        }
        
        stage('Deploy to Kubernetes') {
            steps {
                script {
                    echo 'Deploying to Kubernetes...'
                    sh 'kubectl apply -f kubernetes/'
                    echo 'Kubernetes manifests applied successfully'
                }
            }
        }
        
        stage('Verify Deployment') {
            steps {
                script {
                    echo 'Verifying deployment...'
                    sh 'kubectl rollout status deployment/flask-app'
                    echo '--- Pod Status ---'
                    sh 'kubectl get pods'
                    echo '--- Service Status ---'
                    sh 'kubectl get svc'
                    echo 'Deployment verification completed'
                }
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline execution completed'
        }
        success {
            echo 'Pipeline succeeded! Application deployed successfully.'
        }
        failure {
            echo 'Pipeline failed! Please check the logs for details.'
        }
    }
}

