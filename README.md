# CC Community Creation platform

The project can be cloned into macos and linux distributions via commands below.  
  
mkdir project  
cd project/  
git clone https://github.com/mesoylu/swe573.git  
cd swe573/python3 -m venv env  
source env/bin/activate  
pip install -r backend/requirements.txt  
  
-- given postgresql 12 is installed  
createdb testdb  
createuser testuser  
psql-- on postgresql command line  
  
$ alter user testuser with password 'abc';  
$ grant all privileges on database testdb to testuser;  
$ exit;  
  
cd backend/backend/  
cp variables_template.py variables.py  
vi variables.py  
-- change db credentials  
cd ..  
mkdir static  
vi backend/variables.py  
-- change static filepaths  
python3 manage.py collectstatic  
python3 manage.py migrate  
python3 manage.py runserver  



