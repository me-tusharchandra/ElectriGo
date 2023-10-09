# ElectriGo

Project Name: ElectriGo.📌

Whenever we buy an electric vehicle, one needs to install majorly three applications onto our mobile phones
1) Application provided by the government to locate nearby govt charging stations
2) Application provided by EV manufacturers like OLA to check the battery and status of the EV.
3) Application developed by individuals/groups during hackathons like RBH where people get a better understanding of how to improve the life of their EVs

Introducing ElectriGo, a one-stop solution for every EV present in the market. It provides the ability to locate nearby both AC/DC private and public charging stations that are fetched using API’s provided by the government. The users can book the charging docks for a specific period of time before they reach there. Furthermore, the application offers emergency services like calling a battery swap van. Once called, users can effortlessly replace the battery of their electric vehicle, ensuring a seamless experience. Our application involves rigorous monitoring and maintaining the SOC of the EV. Using our ML algorithms, with high accuracy, we predict SOC which is used to calculate range estimation, battery health, etc.

![Case Study](ElectriGo-CaseStudy.png)

We've also pinpointed a segment of significant stakeholders in the Indian EV market which is the rickshaw owners who lack Android You devices. Specifically, there's a notable group of over 1.5 million+ battery-powered EV rickshaws. We have finally created a multilingual chatbot that provides support about the nearest charging station, open charging slots, etc. This chatbot has a very simple UI and it enhances accessibility to almost all the left-out audience.

With ElectriGo, we can dramatically enhance EV Adoptability in future and aim to bring standardisation in the EV industry by affiliating with the government and making it a mandatory thing for electric vehicles in the future.

**ANDROID APPLICATION**
> The ElectriGo App, developed using Java, is a pioneering solution designed to transform the electric mobility landscape. With a focus on serving EV rickshaw owners and promoting environmental sustainability, this application is a game-changer in the realm of sustainable transportation.

**ML MODEL DESCRIPTION**
>In this project, we have tackled the task of predicting the State of Charge (SoC) in a battery system using machine learning techniques. The State of Charge represents the remaining energy in a battery as a percentage of its total capacity and is crucial for managing battery performance and utilization.





**Steps Taken**:

1) Data Collection: We gathered a dataset containing relevant features such as battery characteristics, usage patterns, and environmental factors.
2) Data Preprocessing: We cleaned and preprocessed the dataset, handled missing values. This step is crucial for creating accurate and reliable predictive models.
3) Feature Selection: We have reduced the noise by selecting the most relevant features of the dataset for predicting the SoC.
4) Model Training: Using a training dataset, we have trained models such as linear regression and random forest regression to learn the relationships between input features and the target SoC values. This involves adjusting model parameters to minimize prediction errors.
5) Model Evaluation: To evaluate the model, we considered RMSE value as Root Mean Squared Error (RMSE), Mean Absolute Error (MAE), and R-squared.
6) Upcoming: We are considering to implement a real-time app-based solution for continuous SoC prediction in battery systems.

Video Presentation: [Click Here](https://youtu.be/dyb1eDYfdy4)