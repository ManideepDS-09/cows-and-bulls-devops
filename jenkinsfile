pipeline{                                                                                                       // Starts a declarative pipeline
    agent any                                                                                                   // it says that the pipeline can run on any available agent
    stages{                                                                                                     // Starts defining all steps and the stages block
        stage('checkout'){                                                                                      // Starts a stage called checkout - which is pulling the code                                 
            steps{
                git branch: 'main', url:'https://github.com/ManideepDS-09/cows-and-bulls-devops.git'            // This step clones the git repo
            }
        }
        stage('Docker Build'){
            steps{
                sh 'docker build -t cows-and-bulls-devops .'                                                  // This step builds the docker image
            }
        }
    }
}