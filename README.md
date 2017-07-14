# bucketlist
Bucketlist allows users to record and share things they want to achieve or experience before reaching a certain. In summary, it lets user keep track of their dreams and goals.To use the application, users should first create accounts and then login. A user can the create several bucket lists and add items to it.

How to setup
------------
1. Clone this repository. On git bash use;
    git clone https://github.com/eric-elem/bucketlist

2. Change your working directory to the root folder (bucketlist)
    cd ..\..\bucketlist

3. Install virtualenvwrapper if you don't have it installed yet
    pip install virtualenvwrapper

4. Create a new virtual environment using
    mkvirtualenv env

5. Activate the new virtual environment using
    workon env
    --or--
    env\Scripts\activate 

6. Install flask module and other dependencies using the requirements.txt file (in root directory)
    pip install -r requirements.txt

7. Start the application server by running
    python run.py

8. Using your browser, enter the URL in the form http://server-ip-address:5000 to use the application
    for example http://localhost:5000

