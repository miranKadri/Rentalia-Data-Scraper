# Scraper for rentalia website:

This project has a sole purpose of extracting data for hotels listed in rentalia website. Rentalia website is a hotel listings and booking website in spain, you can book your hotels, compare listing, inquire, etc. Follow the steps given below to set the system up.

* To get started create a directory for this project, inside that directory create a virtual environment for the project using the folling command:   
  `python -m venv virtual_env`
  
* Once you have set up the environment you will type `virtual_env\Scripts\Activate` in cmd to activate the virtual enviroment. 
* I have included a `requirements.txt` containing all required libraries to run the program, you can install all the libraries by typing `pip install -r requirements.txt`  
* Now inside the direcctory 'Driver' you will find a chrome driver file. You can change that driver based on which version of chrome you are using or which browser do you have.  

You are now good to go, Run the following command to start the scraper.  
`python retalia.py`  

You will find the scraped data inside Data directory in the form csv file. keep in mind that the data will get reflected inside that csv file only when the execution is completed or halted.
 
