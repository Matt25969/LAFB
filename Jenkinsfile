pipeline{
	agent any
        stages{
		stage('---build---'){
                        steps{
                               sh "docker-compose up --build -d"
                        }
                }
		stage('---push---'){
			steps{
				sh "docker-compose push"
			}
		}
		stage('---deploy---'){
			steps{
				sh "docker stack deploy --compose-file docker-compose.yaml stackdemo"
			}
		}
	}
}
