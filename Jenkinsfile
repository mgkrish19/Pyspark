pipeline {
    agent none
    stages { 
        stage('Test') {
            agent {
                docker {
                    image 'makotonagai/pyspark-pytest'
                }
            }
            steps {
                sh 'py.test --verbose --junit-xml test-reports/results.xml'
            }
            post {
                always {
                    junit 'test-reports/results.xml'  
                }
            }
        }
    }
}