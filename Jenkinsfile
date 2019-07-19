pipeline{
	agent any
        stages{
		stage('---build---'){
                        steps{
                               sh "docker-compose build"
                        }
                }
		stage('---push---'){
			steps{
   				withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'dockerhub', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD']]) {
      				sh 'docker login -u "$USERNAME" -p "$PASSWORD"'
				sh 'docker-compose push'
			}
		}
		stage('---deploy---'){
			steps{
				sh "docker stack deploy --compose-file docker-compose.yaml devops"
			}
		}
	}
}

