Readme 

Installation : 

1. Upload Dataset in GCP cloud bucket. create a json file<API key to access the Google BigQuery> from GCP 
2. Now using biquery module in python , get the dataset in python - using bigquery module <ensure python and json file are in same directory>
3. First verify the python file app.py on localServer and make sure it launches - http://127.0.0.1:8050/
4. Install herokuapp
5. Create a app in heroku using heroku dashboard.
6. Refer the guidelines on Heroku on Dashboard page, where app is ceated to set remote repository
7. Clone repo  and run the command pip install -r requirements.txt
8. Use below steps :	
	heroku git:remote -a <appname created in heroku dashboard>
	go to the folder where githib repo is cloned
	git init .
	git commit -am "message of commit"
	git push heroku master
	heroku open
9. check heroku logs for further details 