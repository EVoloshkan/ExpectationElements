pipeline {
  agent any
  stages {
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
    stage('Reports') {
        steps {
           allure([
      	   includeProperties: false,
      	   jdk: '',
      	   properties: [],
      	   reportBuildPolicy: 'ALWAYS',
      	   results: [[path: 'allure-results']]
    	   ])
  	        }
         }
  }
}