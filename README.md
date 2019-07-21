# Little Anchorage Financial Bank: DevOps Project

In fulfilment of the group DevOps project assignment due Monday week 11 at QA consulting.

## Index
[Brief](#brief)
   
[Architecture](#architecture)
     
[Technologies Used](#tech)

[Deployment](#depl)
   * [Prerequisites and Installation Guide](#prereq)
   * [CI Pipeline](#CI)

[Authors](#auth)

[Acknowledgements](#ack)

<a name="brief"></a>
## The Brief

To create an OOP-based application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training. The application must manipulate two tables with full CRUD functionality.

<a name="architecture"></a>
## Architecture
#### Before

#### After

<a name="tech"></a>
### Technologies Used

* Mongo - Database
* Node - creating the account generator which includes generating the prize
* Python - creating the number and text generator which generates an account number
* Jenkins - CI Server
* [Git](https://github.com/ayshamarty/SoloProject.git) - VCS
* [Trello](https://trello.com/b/yf6TuPx0/devops-project) - Project Tracking
* Azure - Live Environment
* Docker-Compose - builds the images used to create our containers
* [DockerHub](https://cloud.docker.com/u/keepkarm/repository/list) - registry for storing and updating images used for deployment
* Docker Swarm

<a name="depl"></a>
## Deployment

<a name="prereq"></a>
### Prerequisites
* An Azure virtual machine with Jenkins, Docker and Docker-Compose installed
* At least one other Azure virtual machine with Docker installed
* Access to a Dockerhub registry

#### Installing Jenkins, Docker and Docker Compose, and setting up the swarm

##### Setting the project

1. Create a new resource group
<p align="center">
**az group create –name devops -l uksouth**
</p>

2. Create a new virtual machine
<p align="center">
**az vm create -g devops -n ManagerNode --image UbuntuLTS -l uksouth**
*repeat this command at least once to create your worker nodes, renaming the machines in the -n tag (eg -n Worker1)*
</p>

3. Clone down the project within your ManagerNode
<p align="center">
**git clone https://github.com/kryan1622/LAFB.git**
</p>

4. Install docker and jenkins with with the included scripts and follow the instructions
<p align="center">
**sh ~/LAFB/installation/docker.sh**
*remember to copy this script and run it on your worker nodes*

**sh ~/LAFB/installation/jenkins.sh**
</p>

##### Building the images

1. Build docker images
<p align="center">
**docker-compose build**
</p>

2. Push docker images to the desired dockerhub account by first logging onto dockerhub within the virtual machine
<p align="center">
**docker login**
*Enter username and password when requested*

**docker-compose push**
</p>

##### Setting up the swarm

1. Initialise your swarm in the manager node
<p align="center">
**docker swarm init**
*this will return a command with a unique token which you can run in any number of other virtual machines to set them up as your worker nodes*
</p>

2. Deploy containers with the built images in docker swarm
<p align="center">
**docker stack deploy --compose-file docker-compose.yaml devops**
</p>

##### Setting up Continuous Integration with Jenkins

q. As the Jenkins user, login to a dockerhub account that has access to the registry:
<p align="center">
**sudo su Jenkins**
**docker login**
*Enter username and password when requested*
</p>

2. Expose port 8080 to access Jenkins externally using the command:
<p align="center">
**az vm open-port -g devops -n devopsproject --port 8080 --priority 900**
</p>

3. Access Jenkins site using the public ip address of the virtual machine being used with the addition of :8080 at the end. For example:

4. Get password for initial screen in Jenkins using the command:
<p align="center">
**sudo cat /var/lib/jenkins/secrets/initialAdminPassword**
</p>

5. On the customize Jenkins page select the option to Install suggested plugins, and create your username and password.

6. Set up the pipeline
..1. Create Jenkins pipeline by selecting the new item option. Then name the job and select the pipeline option.

..2. Then in the general section select the GitHub project option and copy in the URL below.
https://github.com/kryan1622/LAFB.git

..3. Create webhook by selecting the trigger build remotely option in the Build Triggers section and type in:
DEVOPS

..4. In the pipeline section, select the "Pipeline Script from SCM" option in "Definition". elect Git in the dropdown menu of SCM and copy in the URL used above into Repository URL.  

To complete the webhook go into the settings option within the GitHub repository. Then select the webhook tab and select

http://51.144.95.241:8080/job/jobname/build 

Then in the payload URL http://username:password@PublicIP:8080/job/jobname/build?token=TOKEN


<a name="CI"></a>
### CI pipeline
![CI Pipeline](/documentation/CIpipeline.png)

#### Overview
The above diagram shows the flow of the continuous integration pipeline.
When a developer makes a change to the application in the source code and pushed to GitHub, the webhook is triggered and the Jenkins pipeline will automatically run.
The pipeline runs the following stages:
##### Build
   * Goes through the docker-compose.yaml and rebuilds any images that have been changed
##### Push
   * Pushes changed images to dockerhub
##### Deploy
   * Updates changed containers in the stack without redeploying the entire application or affecting the user experience

#### Switching Implementations
The client asked for three different unique implementations to be included, these were for the prize generator, number generator and account generator. We have provided these and they can be seemlessly switched out for each other.
The images used are as follows:
##### prize generator
keepkarm/account:v1
   * on creating an account, generates a prize of £50 or £0 with a 25% probability of winning
keepkarm/account:v2
   * on creating an account, generates a prize of £100 or £0 with a 25% probability of winning
##### text generator
keepkarm/text_gen:v1
   * generates a random string of three lowercase letters
keepkarm/text_gen:v2
   * generates a random string of two uppercase letters
##### number generator
keepkarm/num_gen:v1
   * generates a random six digit number
keepkarm/num_gen:v2
    * generates a random eight digit number
	
If the bank's developers want to switch out any of these implementations for the other, all they need to do is edit the docker-compose.yaml file and push it up to git hub. They can swap the implementations for any of the services by changing both version number in the image name, and the number in the build args option. It is crucial to note that that **both numbers must match**. 
When the new docker-compose.yaml is pushed to GitHub

### Improvements for the Future
Using a local registry would be helpful if deploying this application continuously. In cases of internet connection failures or dockerhub going down (which is not unlikely), images can still be easily accessed. 
We suggest using a registry container to improve redundancy.

<a name="auth"></a>
## Authors

Aysha Marty and Krystal Ryan

<a name="ack"></a>
## Acknowledgements

* QA consulting and our fantastic instructors
* The rest of our wonderful cohort on the programme
