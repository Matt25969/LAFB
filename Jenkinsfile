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
				sh "docker push keepkarm/server:latest"
			}
		}
		stage('---deploy---'){
			steps{
				sh "docker stack deploy --compose-file docker-compose.yaml devops"
			}
		}
	}
}
