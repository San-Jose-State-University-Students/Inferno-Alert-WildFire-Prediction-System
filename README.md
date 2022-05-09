# Inferno-Alert-WildFire-Prediction-System

# Submitted towards Charles Davidson College of Engineering, San Jose State University

Group 12:
          Patel Deep (BS in Software Engineering)
          Patel Nimay (BS in Software Engineering)
          Solanki Jay (BS in Software Engineering)
          Trivedi Soumya (BS in Software Engineering)
          

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
* python app.py<br />
* The above command shall also be executed anytime there is a need to run the web application again<br />
* After this, leave the CLI window as it is, and open a new and seperate window<br />
* Here too, navigate yourself inside the source code folder.<br />
* Here, run following command<br />
*         npm install
* Then, execute a final command,<br />
*         npm start
* The above command should automatically open a tab in your browser with the application running. The above command shall also be executed anytime there is a need to run the web application again<br />
