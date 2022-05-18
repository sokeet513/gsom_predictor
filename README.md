# gsom_predictor
A training project for E2E (FINALIZED)
# GSOM Predictor Guide
Hello! It is a readme-ish file, created in order to help you to get easier understanding of the project and how to use it.

## Data source
To use a model we, first of all, need to have some data to train it on. In this case, the data is about prices on the real estate in Saint Petersburg from Yandex Real estate from 1st of Jan 2017 till 1st of August 2018. The dataset is using the following columns:
![base tab](https://drive.google.com/file/d/1QYzEpscQnKG2Oym0ZMFC5lTjjvALadbg/view?usp=sharing)
Every column is cleaned of outliers and NULLs. 
The data is split into training data and test data are selected in a way that training data covers all the columns dated before 1st of April 2018 and test data is using the remaining 4 months till August. 
## The model
To begin with, it is important to explain the data used. The data selected was chosen due to the best correlation with the **price** (which is predicted), as shown in a picture below:
![correlogram](https://drive.google.com/file/d/1TVaa2hPeGmg1CdXm51lbOrZh--wgB182/view?usp=sharing)
It was required to have two models in this project, so I used two models -- CatBoostRegressor and Random Forest Regressor. I have selected CatBoost as a primary model because it is an ML model, that can use gradient boosting and reduce the amount of errors. The second model in use is Random Forest because of its universal utility and ability to work with large datasets. 

Since there are two models used in this project, both of them use almost the same data:
**Catboost** uses data on:
 - Room count
 - Area
 - Ratio of living space to total area
 
**Random Forest** uses data on:
 - Room count -- integer
 - Area -- float
 - Kitchen area -- floar
 - Ratio of living space to total area -- float

> It was required by task to be so, so I had to add additional factor

Both of the models demonstrate MAE (0.19 and 0.18 vs 0.35), MSE(0.34 and 0.29 vs 0.41) and RMSE(0.59 and 0.54 vs 0.66) lower than the strongest training project one, making them less susceptible to error and more reliable.

## How to run on VM
To run on a virtual machine user needs to do several steps:

 1. Have an Ubuntu virtual machine
 2. Install	the Python 3 interpreter
 3. Install the needed Python 3 libraries (*pip install -r requirements.txt*): 
  - Flask
  - NumPy
  - Skitlearn
  - catboost
 4. Create a git-supported folder in the virtual machine
 5. Use a git pull command and download all folders from the github
 6. Use command ***python app.py*** 
 7. The model is active
 8. To stop it, write ***sudo pkill -9 -f app.py***

## How to open the port in your remote VM 
To run it online you need to run the app again and use the port 5444, as it is set as a default one for the app.py; then, to actually use the predictor, you need to make a specific request, that covers **all**  data, that is used by **Random Forest**. Otherwise, the app will return you an error.
You also need to  add additional factor for you to select from 2 models -- catboost?(1/0), where 1 is yes and 0 is no. It is a binary value.
In the end, the address of the running app will look like this:

> http://X.X.X.X:5444/predict_price?catboosted?(1/0)=1&rooms=2&area=60&kitchen_area=14&ratio=0.7

Where X.X.X.X is the IP address of your VM, after each = you should put the value that you need to predict. Make sure that ratio is in the range [0;1].

## Information about Dockerfile and it’s content 
There is a Dockerfile in the github, that allows you to make an alternative run of the app and also to save the image of the application to use on different devices.
Dockerfile that will be downloaded, contains the commands needed to build the container and make a working copy of the application. To use docker, you first need to install and tune it, as said in the instructions below:
[install docker on ubuntu](https://docs.docker.com/engine/install/ubuntu/)
[tune the docker on ubuntu](https://docs.docker.com/engine/install/linux-postinstall/)

Now it is all done and it is possible to use docker
## How to build container using docker
Use the set of the following commands to make and launch the containers:
Build the container:

    docker build -t yourdockerlogin/yourdockerfolder:v.X.X .
    
Launch the container:

    docker run --network host -d yourdockerlogin/yourdockerfolder:v.X.X
Now the container is running!
You can use the same search query as before.

To exit the container you need to use *exit* command while inside of the container

To see the active containers use

    docker ps
To stop the container you need to use the callsign of this container and write in code:

    docker stop <container name>
 You can also push it to your container using the docker push command:
 

    docker push yourdockerlogin/yourdockerfolder:v.X.X
  It will appear at your own account in docker!
  ## Downloading docker on a different VM
  You may also want to just use the Docker and skip the part with the github and download the already working container with ML model on a different VM
  Here you just need to install docker and use a command to pull the image:
  

    git pull yourdockerlogin/yourdockerfolder:v.X.X
Then just use **docker run**  again:

    docker run --network host -d yourdockerlogin/yourdockerfolder:v.X.X
And make a needed search query using different VM IP-address

 
And that's it! Now you can predict pricing in Saint Petersburg real estate using outdated data =)
