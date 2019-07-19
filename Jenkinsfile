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
				sh "sudo docker-compose push"
			}
		}
		stage('---deploy---'){
			steps{
				sh "sudo docker stack deploy --compose-file docker-compose.yaml devops"
			}
		}
	}
}
