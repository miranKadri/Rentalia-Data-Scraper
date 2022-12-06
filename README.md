# Scraper for rentalia website:

This project has a sole purpose of extracting data for hotels listed in rentalia website. Rentalia website is a hotel listings and booking website in spain, you can book your hotels, compare listing, inquire, etc. Follow the steps given below to set the system up.

* To get started create a directory for this project, inside that directory create a virtual environment for the project using the folling command:   
  `python -m venv virtual_env`
  
* Once you have set up the environment you will type `virtual_env\Scripts\Activate` in cmd to activate the virtual enviroment. 
* I have included a `requirements.txt`  file that contains all required libraries with their versions to run the program, you can install all the libraries by executing the command `pip install -r requirements.txt`  
* Now inside the direcctory 'Driver' you will find a chrome driver file. You can change that driver based on which version of chrome you are using or which browser do you have.  

You are now good to go, Run the following command to start the scraper.  
`python retalia.py`  

You can pass the name of the regions as arguments after your python file name in the cmd like this:  
`python retalia.py "costa brava" "gava"` 
Make sure you pass the names under `""`.

I have included six locations "Costa Brava", "Alicante", "Barcelona", "Madrid", "Castelldefels", and "Gavà" for now, wo when you don't put any arguments in cmd it will by default take these names. 
You will find the scraped data inside Data directory in the form csv file. keep in mind that the data will get reflected inside that csv file only when the execution is completed or halted.
I will be upgrading the code file to take arguments in cmd so that user can type the cities they want to extract the data from in cmd.

--Do visit back again in some time for updates--

Also, any suggestions on how this project could further be developed are welcomed, feel free to reach out to me at mirankadri9@outlook.com✅.

 
