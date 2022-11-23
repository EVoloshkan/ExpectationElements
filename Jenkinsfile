pipeline {
  agent any
  stages {
     stage("Build image") {
        steps {
    	catchError {
      	   script {
        	      docker.build("page_object2", "-f Dockerfile .")
      	     }
          }
       }
    }
     stage('Run tests') {
        steps {
           catchError {
              script {
          	     docker.image('aerokube/selenoid:1.10.8').withRun('-p 4444:4444 -v /run/docker.sock:/var/run/docker.sock -v $PWD:/etc/selenoid/',
            	'-timeout 600s -limit 2') { c ->
              	docker.image('page_object2').inside("--link ${c.id}:selenoid") {
                    	sh "pytest -n 2 --reruns 1 ${CMD_PARAMS}"
                	    }
                   }
        	     }
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
      	   results: [[path: 'allure-results/']]
    	   ])
  	        }
         }
     }
}