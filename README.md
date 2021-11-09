**Image Server**
<br /><br />
imageServer is the project done to store images of 3 different sizes ( _small, medium, large_ ) image<br />

**how anyone can run my project, steps are as follow**
<br /><br />
  git clone https://github.com/gkrishnans/imageServer.git -b original<br />
  cd imageServer<br />
  python3 -m venv venv<br />
  source venv/bin/activate<br />
  pip install -r requirements.txt<br />
  export name=""<br />
  export password=""<br />
  flask run<br />
<br />
**Tools and Libraries used**
<br /><br />
  flask + MongoDB<br />
  Flask-Pymongo<br />
  pillow<br />
<br />
**Features**
<br /><br />
  you can also download image from the server<br />
  you can add tags for each image<br />
  you can categories them accordingly<br />
