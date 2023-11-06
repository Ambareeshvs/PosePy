# PosePy: The Yoga Trainer

Yoga and Fitness exercises are very beneficial to personal health and fitness; however, they can also be ineffective and potentially 
dangerous if performed incorrectly by the user. Such mistakes are made when the user does not use the proper form, or pose. 
PosePy, a web application that detects a user's pose and provides personalized recommendations on how the user can improve their postures. 
This process is done in real time in order to be more interactive with the user. PosePy uses Mediapipe Pose Solutions to detect user postures and then 
evaluates the user's pose with standard yoga postures using intersegmental joint angles as a comparison metric. The proposed approach maintains low 
computational complexity and, unlike other yoga trainers available, it does not require a huge dataset for training its model.


## Team Members

1. Amal Pradeep Pothan(https://github.com/amalpothan)
2. Ambareesh V Sankaran(https://github.com/Ambareeshvs)
3. Anugrah V(https://github.com/new-piedpiper)
4. Rithik Rajesh(https://github.com/rithikrajeshnair)

> Guided by Prof. Bincy Antony M, Government College Of Engineering,Kannur


## How It Works?
Step 1: Click the "Start Stream" button to on the camera.

Step 2: Do the yoga pose infront of the camera.

Step 3: The recognised pose and corrections for that pose will display on the screen.

Step 4: Click the "Stop Stream" button to off the camera.


## Libraries Used
- Mediapipe
- OpenCV
- Flask


## How To Configure
- Download the whole project and keep it in folder.
- Install the libraries defined above.
- Navigate to the newly made folder and activate the environment if any.


## How To Run

```sh
set FLASK_ENV=development
flask run
```
