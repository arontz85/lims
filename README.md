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
**Step Two:** Open your _VScode editor_ and navigate to the **LibraryInformationManagementSystem/lims** folder.    
**Step Three:** type "_python -m venv PythonEnv_" # This will create the virtual environment with folder name PythonEnv.  
**Step Four:** type "_PythonEnv\Scripts\activate_" and press Enter key on the keyboard #_This will activate the virtual environment._   
**Step Five:** type "_python -m pip install Django_" # This will install Django Framework.  
**Step Six:** type "_cd lims_portal_" and press Enter key on the keyboard # _This will change the directory to the project folder._    
**Step Seven:** type "_python manage.py makemigrations lims_app._"  and press Enter key on the keyboard.  
**Step Eight:** type "_python manage.py migrate._"  and press Enter key on the keyboard.  
**Step Nine:** type "_python manage.py runserver 8080_" press Enter key on the keyboard # _This will make the project to run on port 8080._    

**The result on your command line will look like be as follows:**  
PS C:\Users\Aaron\Downloads\lims-main\lims-main\LibraryInformationManagementSystem\lims> python -m venv PythonEnv  
PS C:\Users\Aaron\Downloads\lims-main\lims-main\LibraryInformationManagementSystem\lims> PythonEnv\Scripts\activate  
(PythonEnv) PS C:\Users\Aaron\Downloads\lims-main\lims-main\LibraryInformationManagementSystem\lims> python -m pip install Django  
Collecting Django  
  Obtaining dependency information for Django from https://files.pythonhosted.org/packages/50/1b/7536019fd20654919dcd81b475fee1e54f21bd71b2b4e094b2ab075478b2/Django-5.0.2-py3-none-any.whl.metadata  
  Downloading Django-5.0.2-py3-none-any.whl.metadata (4.1 kB)  
Collecting asgiref<4,>=3.7.0 (from Django)  
  Obtaining dependency information for asgiref<4,>=3.7.0 from https://files.pythonhosted.org/packages/9b/80/b9051a4a07ad231558fcd8ffc89232711b4e618c15cb7a392a17384bbeef/asgiref-3.7.2-py3-none-any.whl.metadata  
  Using cached asgiref-3.7.2-py3-none-any.whl.metadata (9.2 kB)  
Collecting sqlparse>=0.3.1 (from Django)  
  Obtaining dependency information for sqlparse>=0.3.1 from https://files.pythonhosted.org/packages/98/5a/66d7c9305baa9f11857f247d4ba761402cea75db6058ff850ed7128957b7/sqlparse-0.4.4-py3-none-any.whl.metadata  
  Downloading sqlparse-0.4.4-py3-none-any.whl.metadata (4.0 kB)  
Collecting tzdata (from Django)
  Obtaining dependency information for tzdata from https://files.pythonhosted.org/packages/65/58/f9c9e6be752e9fcb8b6a0ee9fb87e6e7a1f6bcab2cdc73f02bb7ba91ada0/tzdata-2024.1-py2.py3-none-any.whl.metadata  
  Downloading tzdata-2024.1-py2.py3-none-any.whl.metadata (1.4 kB)  
Downloading Django-5.0.2-py3-none-any.whl (8.2 MB)  
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.2/8.2 MB 4.0 MB/s eta 0:00:00  
Using cached asgiref-3.7.2-py3-none-any.whl (24 kB)  
Using cached sqlparse-0.4.4-py3-none-any.whl (41 kB)  
Downloading tzdata-2024.1-py2.py3-none-any.whl (345 kB)  
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 345.4/345.4 kB 4.3 MB/s eta 0:00:00  
Installing collected packages: tzdata, sqlparse, asgiref, Django  
Successfully installed Django-5.0.2 asgiref-3.7.2 sqlparse-0.4.4 tzdata-2024.1  

[notice] A new release of pip is available: 23.2.1 -> 24.0  
[notice] To update, run: python.exe -m pip install --upgrade pip  
(PythonEnv) PS C:\Users\Aaron\Downloads\lims-main\lims-main\LibraryInformationManagementSystem\lims> cd lims_portal  
(PythonEnv) PS C:\Users\Aaron\Downloads\lims-main\lims-main\LibraryInformationManagementSystem\lims\lims_portal> python manage.py makemigrations lims_app  
Migrations for 'lims_app':  
  lims_app\migrations\0016_delete_issuedbooks.py  
    - Delete model issuedBooks    
(PythonEnv) PS C:\Users\Aaron\Downloads\lims-main\lims-main\LibraryInformationManagementSystem\lims\lims_portal> python manage.py migrate  
Operations to perform:  
  Apply all migrations: admin, auth, contenttypes, lims_app, sessions  
Running migrations:  
(PythonEnv) PS C:\Users\Aaron\Downloads\lims-main\lims-main\LibraryInformationManagementSystem\lims\lims_portal> python manage.py runserver 8080    
Watching for file changes with StatReloader  
Performing system checks...  

System check identified no issues (0 silenced).  
February 17, 2024 - 08:51:18  
Django version 5.0.2, using settings 'lims_portal.settings'  
Starting development server at http://127.0.0.1:8080/  
Quit the server with CTRL-BREAK.    

**The result on your web browser will be as below:**

![image](https://github.com/arontz85/lims/assets/156838915/be1d6eb3-a8e0-41ee-b97c-1c1d62242b41)
