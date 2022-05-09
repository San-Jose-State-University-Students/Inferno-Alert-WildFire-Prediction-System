# Inferno-Alert-WildFire-Prediction-System

# Submitted towards Charles Davidson College of Engineering, San Jose State University

Group 12:
          Patel Deep (BS in Software Engineering)
          Patel Nimay (BS in Software Engineering)
          Solanki Jay (BS in Software Engineering)
          Trivedi Soumya (BS in Software Engineering)
          
# code Structure: -
# Setup/BUild Instructions: -

Here are the steps tp follow in order to get the web application up and running on localhost:

(1) Following items need to be installed or should be ready:
    Node.js
    A stable version of python.
    A valid Text Editior (VS Code or Notepad)
    A browserwith stable version

(2) Generate API keys:
    Go to openweathermap.org/api and create a free account
    Then subscirbe to the One Call API plan for free
    Among the given options, select the free option of Get API key
    This should generate API key in your My API Keys section in top right under your name.
    Similarly, go to https://developers.google.com/maps/documentation/javascript/overview and select "Get Started"
    Create/Login to your Google Cloud Platform account which is available on free trial for 3 months.
    Now, go to API section and create API key for Maps Javascript API section.
    This key will be visible in Credentials section.
    
(3) Code setup: 
    Download the zip file and unzip the source code.
    Go to "Inferno-Alert-WildFire-Prediction-System-main\src\components\weather\WeatherForm.js" inside the folder and on line 15 of WeatherForm.js, add your    OpenWeatherMap API key at very end just before closeing " ' ".
    Save the file and close it.
    Go to "Inferno-Alert-WildFire-Prediction-System-main\src\components\location\MapInterface.js" inside the folder and on line 6 of MapInterface.js, add your Google Maps Javascript API key at the very end.
    Save the file and close it.

(4) Execute the program:
    Open your prefered CLI and navigate to the directory path inside the folder.
    Execute following commands in your CLI:
    pip install flask
    pip install matlibplot
    pip install pandas
    
    Then, execute a final command,
    python app.py
    The above command shall also be executed anytime there is a need to run the web application again
    After this, leave the CLI window as it is, and open a new and seperate window
    Here too, navigate yourself inside the source code folder.
    Here, run following command
    npm install
    Then, execute a final command,
    npm start
    The above command should automatically open a tab in your browser with the application running. The above command shall also be executed anytime there is a need to run the web application again
