# Library Information Management System
# Developed by Aron Zeru
This Library Information Management System runs on Django Framework. Sqlite3(later will be changed to PostgreSQL) database in the back-end and HTML, and CSS in the front-end.  

**Features:**  
This is a Library Information Management System which contains the following features  
=>**Home page** that contains general information about the system.   
=>**Readers page** – In this feature, the admin can manage all the information of the readers including, “adding new readers”, “updating or modifying readers' data” and “deleting readers' data from the database“.  
=>**Books page** – In this feature, the admin can manage all the information of books including, “adding new books”, “updating or modifying books' data” "Issuing books' to readers" and “deleting books' data from the database“.  
=>**Issued Books page** – In this feature, we will be able to see the list of issued books along with the name and ID of the readers who borrowed the books.  
=>**Login/Logout System** – With this feature, the user can log-in and log-out of the system.  

**Steps to run the project:**  
**Step One:** download and _extract/unzip_ the **LibraryInformationManagementSystem** folder.    
**Step Two:** Open your _VScode editor_ and navigate to the **LibraryInformationManagementSystem** folder.    
**Step Three:** type "_python -m venv PythonEnv_" # This will create the virtual environment with folder name PythonEnv.  
**Step Four:** type "_PythonEnv\Scripts\activate_" and press Enter key on the keyboard #_This will activate the virtual environment._   
**Step Five:** type "_python -m pip install Django_" # This will install Django Framework.  
**Step Six:** type "_cd lims_portal_" and press Enter key on the keyboard # _This will change the directory to the project folder._    
**Step Seven:** type "_python manage.py makemigrations lims_app._"  and press Enter key on the keyboard.  
**Step Eight:** type "_python manage.py migrate._"  and press Enter key on the keyboard.  
**Step Nine:** type "_python manage.py runserver 8080_" press Enter key on the keyboard # _This will make the project to run on port 8080._    
