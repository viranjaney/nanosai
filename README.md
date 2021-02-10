# nanos.ai

### Getting Started
```
unzip nanosai-main.zip

Open terminal

cd nanosai-main
```
#### Virtual environment
```
python3 -m venv .     #create virtual environment

source bin/activate   #activate virtual environment

python -m pip install --upgrade pip  #upgrade pip or some packages won’t be downloaded
```
#### Install packages
```
pip3 install -r requirements.txt   #install required packages
```

#### Running the Tests
```
python3 nanosai.py   #run this file to get keywords from nanos.ai

Ex:
(nanosai) admin$ python3 nanosai.py 
Enter Product/Services/Keyword : digital marketing
Important keywords: {'marketing', 'technology', 'advertising', 'business', 'digital'}


python3 huubsh.py    #get keywords from huubsh.com 

Ex:
(nanosai) admins$ python3 huubsh.py 
Geben Sie Produkt / Dienstleistung / Schlüsselwort ein : gitarre
Wichtige Schlüsselwörter: {'guitar', 'saiten', 'gitarre', 'gitarren'}
```
