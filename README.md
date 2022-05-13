# Inferno-Alert-WildFire-Prediction-System

# Submitted towards Charles Davidson College of Engineering, San Jose State University

Group 12:<br />
          Patel Deep (BS in Software Engineering)<br />
          Patel Nimay (BS in Software Engineering)<br />
          Solanki Jay (BS in Software Engineering)<br />
          Trivedi Soumya (BS in Software Engineering)<br />

# Link to the Github Repository: 

https://github.com/San-Jose-State-University-Students/Inferno-Alert-WildFire-Prediction-System

# Table of Content: 

This file contains information on following aspects of our project:

* Abstract<br />
* Tools/Technologies used<br />
* Code Structure<br />
* Setup/Install Instructions<br />
* References<br />

# ABSTRACT: 

The United States has witnessed more than 1.8 billion acres of land getting burnt this year alone and the number is suspected to increase (CNN). These fires gulp the vegetation disturbing the ecological balance in nature and destroying everything along the way.  Predicticting such fires beforehand will not only reduce the cost to combat these fires but also save thousands of lives.<br />

Existing fire alert applications don't alert people until the fire is ablaze. They don’t predict future instances mainly due to the fear of the loss of business in the tourism sector. Businesses will suffer a loss if such alerts are provided in advance; As in the case of Lake Tahoe: Visitors were unaware about the susceptibility of a wildfire breakout and restaurants were afraid that they would lose money if they told visitors not to come. <br />

The project aims to build up on the existing fire detection models and datasets to fabricate an application that alerts people nearing a fire risk zone. This alert might save billions of dollars and livestock. The project takes into consideration the history of that place and the environmental factors such as: wind, FFMC, temperature, DMC etc. to make as accurate a prediction as possible displaying its results on a web application. <br />

# Tools/Technologies used: 

Here is the list of all tools we are using for this project: <br />
 
* React (FrontEnd): We created a web application UI for manually putting values<br />
* Node.js (FrontEnd): Javascript runtime environment for executing JS code<br />
* Google Maps Javascript API (UI Maps): Integrating a dynamic map for user input<br />
* OpenWeatherMap API(UI MAps): Fetching weather data for the selected location<br />
* npm PackageRunner (FrontEnd): Package manager for Node.js code execution<br />
* VSCode (FrontEnd): Source code editor for Front end web app development <br />
* Google Colab(ML Model): Used as cloud-based Jupyter Notebook environment<br />
* Flask (API Development): Develop custom API for FWI calculation <br />
* Jupyter Notebooks (ML Algorithm): Create and share documents with live code <br />
* Google Data Studio (Dataset): Create data visualization from custom dataset<br />
* RStudio (Data Analytics): Creating custom dataset by merging subset data <br />
* Jira (Issue Tracking and Ticketing): Keep track of progress and responsibilities<br />
* Selenium (Testing): Used to automate web app testing activity once it is made<br />
* BrowserStack Automate (Testing): Used to run Selenium test scripts on localhost<br />
* TestRail (Testing): To write test case, design test strategies and test management<br />
* Whatsapp Group Calling (Team Meetings): For team coordination in project work <br />
* Zoom (Project Advisor Meetings): For updating advisor with our progress<br />
* Diagrams.net (UML Diagrams): Design and develop software architecture<br />
* Lucid Chart (UI Mockups): Design and develop software architecture <br />
* Google Drive (Documentation): Document sharing and documentation purposes<br />
* Github (Software hosting): Sharing dataset and coding files and hosting web app<br />

# Code Structure:

### ReactJS <br />

![image](https://github.com/San-Jose-State-University-Students/Inferno-Alert-WildFire-Prediction-System/blob/main/images/ReactJS%20Code%20Structure.png)

<br />One of the advantages of ReactJS is that you can divide your code in small snippets called components. These snippets of code can be reused throughout the application. So it can be said that a web application in ReactJS is created by integrating these components together. Most ReactJS applications have App.js, index.js, and index.css files. The App.js file is the main file where all the components are brought together. In our application, the App.js file contains the TitleBar, Home, and New Prediction components. These three components are made from combining all the other components defined in the code (for a better understanding, look at the diagram above). Additionally, each component can have its own CSS file that contains code specific to that component. The index.js file is used to tell where the code needs to be rendered. In our application, index.js is used to render the App component. In our code, index.js can be thought of as the starting point of the entire application. Finally, index.css file contains the CSS code that is applicable to the entire application.

### Flask

Flask is a lightweight framework of python where integration of front-end and back-end is very efficient. Our application utilizes Flask as the service layer, with app.py connecting the machine learning algorithms to the front-end react. The app.py has classes that accept weather data from react and apply it to python formulas, which then calculate the Fine Fuel Moisture Code (FFMC), the Duff Code (DC), and the Duff Moisture Code (DUC), from which BUI, ISI, and FWI values are obtained. These numbers are then fed into the Machine Learning model, which predicts the likelihood of a fire. The prediction is called in app.py and displayed to the user on the front-end.

# Setup/Build Instructions: -

Here are the steps to follow in order to get the web application up and running on localhost:
<br />
1. Following items need to be installed or should be ready:
* Node.js<br />
* A stable version of python 3.8.<br />
* A valid Text Editior (VS Code or Notepad)<br />
* A browserwith stable version<br />
2. Generate API keys:
* Go to https://openweathermap.org/api and create a free account<br />
* Then subscirbe to the One Call API plan for free<br />
* Among the given options, select the free option of Get API key. This is the left most option.<br />
* This should generate API key in your My API Keys section in top right under your name.<br />
* Similarly, go to https://developers.google.com/maps/documentation/javascript/overview and select "Get Started"<br />
* Create/Login to your Google Cloud Platform. Create a billing account which is available on free trial for 3 months.<br />
* Now, go to API section and create API key for Maps Javascript API section.<br />
* This key will be visible in Credentials section.<br />
3. Code setup: 
* Download the zip file and unzip the source code.<br />
* Go to "Inferno-Alert-WildFire-Prediction-System-main\src\components\weather\WeatherForm.js" inside the folder and on line 15 of WeatherForm.js, add your    OpenWeatherMap API key at very end after " = " and before " ` ".<br />
* Save the file and close it.<br />
* Go to "Inferno-Alert-WildFire-Prediction-System-main\src\components\location\MapInterface.js" inside the folder and on line 6 of MapInterface.js, add your Google Maps Javascript API key at the very end between the double quotes.<br />
* Save the file and close it.<br />
4. Execute the program:
* Open your prefered CLI and navigate to the directory path inside the folder.<br />
* Execute following commands in your CLI:<br />
*         pip install flask
*         pip install matlibplot
*         pip install pandas
*         pip install scikit-learn==0.24.1
* Then, execute a final command,<br />
*         python app.py
* The above command shall also be executed anytime there is a need to run the web application again<br />
* After this, leave the CLI window as it is, and open a new and seperate window<br />
* Here too, navigate yourself inside the source code folder.<br />
* Here, run following command<br />
*         npm install
* Then, execute a final command,<br />
*         npm start
* The above command should automatically open a tab in your browser with the application running. The above command shall also be executed anytime there is a need to run the web application again<br />
* Everytime the application needs to be run again, the following two commands should be executed after navigating to this project folder in two separate windows of the CLI:
*         npm start
*         python app.py

# References:

* A. Srinivasan, “Leveraging Machine Learning to predict wildfires: Contributing to the United Nations Sustainable…,” Medium, Dec. 15, 2020. https://towardsdatascience.com/leveraging-machine-learning-to-predict-wildfires-contributing-to-the-united-nations-sustainable-a10c5044dcae?gi=8bb471cae7bb (accessed Nov. 11, 2021).

* Gulati, A. P. (2021, October 21). Forest fire prediction using machine learning. Analytics Vidhya. Retrieved May 13, 2022, from https://www.analyticsvidhya.com/blog/2021/10/forest-fire-prediction-using-machine-learning/ 

* Academind. (2021, May 5). React Crash Course for Beginners 2021 - Learn ReactJS from Scratch in this 100% Free Tutorial! [Video]. YouTube. https://www.youtube.com/watch?v=Dorf8i6lCuk

* Berwyn, B. (2018, August 23). How wildfires can affect climate change (and vice versa). Inside Climate News. Retrieved October 13, 2021, from https://insideclimatenews.org/news/23082018/extreme-wildfires-climate-change-global-warming-air-pollution-fire-management-black-carbon-co2/?gclid=CjwKCAjwh5qLBhALEiwAioodswvm5t4B9zB9Y1DyXOL95K-c1jGadth4zRsfAOhmaadDA8eE0K-hpRoC6DcQAvD_BwE.

* Cardille, J. A., Ventura, S. J., & Turner, M. G. (2001). Environmental and Social Factors Influencing Wildfires in the Upper Midwest, United States. Ecological Applications, 11(1), 111–127. https://doi.org/10.1890/1051-0761(2001)011[0111:
EASFIW]2.0.CO;2

* Code Commerce. (2022, January 20). Build A React JS Weather App - OpenWeatherMap API - Tutorial [Video]. YouTube. https://www.youtube.com/watch?v=UjeXpct3p7M

* Ghorbanzadeh, O., Valizadeh Kamran, K., Blaschke, T., Aryal, J., Naboureh, A., Einali, J., & Bian, J. (2019). Spatial Prediction of Wildfire Susceptibility Using Field Survey GPS Data and Machine Learning Approaches. Fire (Basel, Switzerland), 2(3), 43–. https://doi.org/10.3390/fire2030043

* Halliday, L. [Leigh Halliday]. (2020, May 18). Google Maps & Google Places in React [Video]. YouTube. https://www.youtube.com/watch?v=WZcxJGmLbSo

* “Hybrid artificial intelligence models based on a neuro-fuzzy system and metaheuristic optimization algorithms for spatial prediction of wildfire probability,” Agricultural and Forest Meteorology, vol. 266–267, pp. 198–207, Mar. 2019, doi: 10.1016/j.agrformet.2018.12.015.

* Jain, P., Coogan, S. C. ., Subramanian, S. G., Crowley, M., Taylor, S., & Flanigan, M. D. (2020). A review of machine learning application in wildfire science and management. Environmental Reviews, 28(4), 478–505. https://doi.org/10.1139/er-2020-0019

* J. Brownlee, “How to Connect Model Input Data With Predictions for Machine Learning,” Machine Learning Mastery, Nov. 14, 2019. https://machinelearningmastery.com/how-to-connect-model-input-data-with-predictions-for-machine-learning/ (accessed Nov. 11, 2021).

* Kaustumbh Jaiswal, “Deploying a Machine Learning Model Using Django: Part-1,” Medium, Jul. 03, 2019. https://medium.com/saarthi-ai/deploying-a-machine-learning-model-using-django-part-1-6c7de05c8d7.

* K. Nighania, “Various ways to evaluate a machine learning models performance,” Medium, Jan. 30, 2019. https://towardsdatascience.com/various-ways-to-evaluate-a-machine-learning-models-performance-230449055f15.

* Lall, S., & Mathibela, B. (2016). The application of artificial neural networks for wildfire risk prediction. 2016 International Conference on Robotics and Automation for Humanitarian Applications (RAHA), 1–6. https://doi.org/10.1109/RAHA.2016.7931880

* Lawson, B.D.; Armitage, O.B. 2008. Weather Guide for the Canadian Forest Fire Danger Rating System. Natural Resources Canada, Canadian Forest Service, Northern Forestry Center, Edmonton, AB. 84 p. “Overview | Maps JavaScript API,” Google Developers. https://developers.google.com/maps/documentation/javascript/overview.

* Sayad, Y. O., Mousannif, H., & Al Moatassime, H. (2019). Predictive modeling of wildfires: A new dataset and machine learning approach. Fire Safety Journal, 104, 130–146. https://doi.org/10.1016/j.firesaf.2019.01.006

* S. E. - Artemis.bm, “California wildfires in 2021 have destroyed or damaged 3,500 structures - Artemis.bm,” Artemis.bm - The Catastrophe Bond, Insurance Linked Securities & Investment, Reinsurance Capital, Alternative Risk Transfer and Weather Risk Management site, Oct. 01, 2021.https://www.artemis.bm/news/california-wildfires-in-2021-have-destroyed-or-damaged-3500-structures/.

* The economic impacts of large wildfires | ecosystem . (n.d.). Retrieved October 13, 2021, from https://ewp.uoregon.edu/largefires/content. 

* Turner, J.A.; Lawson, B.D. 1978. Weather in the Canadian Forest Fire Danger Rating System. A user guide to national standards and practices. Environment Canada, Pacific Forest Research Centre, Victoria, BC. BC-X-177.

* Van Wagner, C.E.; Pickett, T.L. 1985. Equations and FORTRAN program for the Canadian Forest Fire Weather Index System. Canadian Forest Service, Ottawa, ON. Forestry Technical Report 33.
