#  To run the project

##  Activating the virtual envt
-  Make sure you have python 3 installed
- Run the command python3 -m venv venv
- Activate the virtual envt with . venv/bin/activate
- Then install requirements with pip install requirements.txt
- After run the file with python youtube.py 

#  NOTE

##  Schedule any time you want with the corresponding commands respectively
-  schedule.every(10).seconds.do(job)
-  schedule.every(10).minutes.do(job)
-  schedule.every().hour.do(job)
-  schedule.every().day.at("10:30").do(job)
-  schedule.every(5).to(10).minutes.do(job)
-  schedule.every().monday.do(job)
-  schedule.every().wednesday.at("13:15").do(job)
-  schedule.every().minute.at(":17").do(job)