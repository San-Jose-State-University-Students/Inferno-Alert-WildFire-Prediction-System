# Inferno-Alert-WildFire-Prediction-System

# Submitted towards Charles Davidson College of Engineering, San Jose State University

Group 12:<br />
          Patel Deep (BS in Software Engineering)<br />
          Patel Nimay (BS in Software Engineering)<br />
          Solanki Jay (BS in Software Engineering)<br />
          Trivedi Soumya (BS in Software Engineering)<br />
          

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


# References:

* A. Srinivasan, “Leveraging Machine Learning to predict wildfires: Contributing to the United Nations Sustainable…,” Medium, Dec. 15, 2020. https://towardsdatascience.com/ leveraging-machine-learning-to-predict-wildfires-contributing-to-the-united-nations-sustainable-a10c5044dcae?gi=8bb471cae7bb (accessed Nov. 11, 2021).
* Berwyn, B. (2018, August 23). How wildfires can affect climate change (and vice versa). Inside Climate News. Retrieved October 13, 2021, from https://insideclimatenews.org/news/23082018/extreme-wildfires-climate-change-global-warming-air-pollution-fire-management-black-carbon-co2/?gclid=CjwKCAjwh5qLBhALEiwAioodswvm5t4B9zB9Y1DyXOL95K-c1jGadth4zRsfAOhmaadDA8eE0K-hpRoC6DcQAvD_BwE.
* Cardille, J. A., Ventura, S. J., & Turner, M. G. (2001). Environmental and Social Factors Influencing Wildfires in the Upper Midwest, United States. Ecological Applications, 11(1), 111–127. https://doi.org/10.1890/1051-0761(2001)011[0111:
EASFIW]2.0.CO;2

* Ghorbanzadeh, O., Valizadeh Kamran, K., Blaschke, T., Aryal, J., Naboureh, A., Einali, J., & Bian, J. (2019). Spatial Prediction of Wildfire Susceptibility Using Field Survey GPS Data and Machine Learning Approaches. Fire (Basel, Switzerland), 2(3), 43–. https://doi.org/10.3390/fire2030043

* “Hybrid artificial intelligence models based on a neuro-fuzzy system and metaheuristic optimization algorithms for spatial prediction of wildfire probability,” Agricultural and Forest Meteorology, vol. 266–267, pp. 198–207, Mar. 2019, doi: 10.1016/j.agrformet.2018.12.015.

* Jain, P., Coogan, S. C. ., Subramanian, S. G., Crowley, M., Taylor, S., & Flanigan, M. D. (2020). A review of machine learning application in wildfire science and management. Environmental Reviews, 28(4), 478–505. https://doi.org/10.1139/er-2020-0019

* J. Brownlee, “How to Connect Model Input Data With Predictions for Machine Learning,” Machine Learning Mastery, Nov. 14, 2019.https://machinelearningmastery
.com/how-to-connect-model-input-data-with-predictions-for-machine-learning/ (accessed Nov. 11, 2021).

* Kaustumbh Jaiswal, “Deploying a Machine Learning Model Using Django: Part-1,” Medium, Jul. 03, 2019. https://medium.com/saarthi-ai/deploying-a-machine-learning-
model-using-django-part-1-6c7de05c8d7.

* K. Nighania, “Various ways to evaluate a machine learning models performance,” Medium, Jan. 30, 2019. https://towardsdatascience.com/various-ways-to-evaluate-a-
machine-learning-models-performance-230449055f15.

* Lall, S., & Mathibela, B. (2016). The application of artificial neural networks for wildfire risk prediction. 2016 International Conference on Robotics and Automation for Humanitarian Applications (RAHA), 1–6. https://doi.org/10.1109/RAHA.2016.7931880

* Lawson, B.D.; Armitage, O.B. 2008. Weather Guide for the Canadian Forest Fire Danger Rating System. Natural Resources Canada, Canadian Forest Service, Northern Forestry Center, Edmonton, AB. 84 p. “Overview | Maps JavaScript API,” Google Developers. https://developers.google.com/maps/documentation/javascript/overview.

* Sayad, Y. O., Mousannif, H., & Al Moatassime, H. (2019). Predictive modeling of wildfires: A new dataset and machine learning approach. Fire Safety Journal, 104, 130–146. https://doi.org/10.1016/j.firesaf.2019.01.006

* S. E. - Artemis.bm, “California wildfires in 2021 have destroyed or damaged 3,500 structures - Artemis.bm,” Artemis.bm - The Catastrophe Bond, Insurance Linked Securities & Investment, Reinsurance Capital, Alternative Risk Transfer and Weather Risk Management site, Oct. 01, 2021.https://www.artemis.bm/news/california-wildfires-in-2021-have-destroyed-or-damaged-3500-structures/.

* The economic impacts of large wildfires | ecosystem . (n.d.). Retrieved October 13, 2021, from https://ewp.uoregon.edu/largefires/content. 

* Turner, J.A.; Lawson, B.D. 1978. Weather in the Canadian Forest Fire Danger Rating System. A user guide to national standards and practices. Environment Canada, Pacific Forest Research Centre, Victoria, BC. BC-X-177.

* Van Wagner, C.E.; Pickett, T.L. 1985. Equations and FORTRAN program for the Canadian Forest Fire Weather Index System. Canadian Forest Service, Ottawa, ON. Forestry Technical Report 33.
