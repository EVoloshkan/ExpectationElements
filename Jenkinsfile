pipeline {
  agent {
      docker {
          image 'python:3' }
       }
  stages {
         stage('Get Code') {
            steps {
                 git 'https://github.com/agridyaev/otus-allure/'
            }
         }
    stage('build') {
      steps {
        sh 'pip install --user -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'python3 -m pytest --junitxml=./test-reports/report.xml ./tests'
      }
      post {
        always {
          junit 'test-reports/*.xml'
        }
      }
    }
  }
}