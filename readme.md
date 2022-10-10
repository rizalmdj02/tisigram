# Welcome to Simple News Reading

this simple application to read all most popular article from **The New York Times** 

# Sample Live Application
[Plase Visit](https://tisigram.herokuapp.com/)

# How To Run It
## If you use docker
    https://github.com/rizalmdj02/tisigram.git
    cd tisigram
    docker build -t app:latest .
    docker run -d --name app-data -e "PORT=8765" -e "DEBUG=1" -p 8007:8765 web:latest
    
## If not use docker
    https://github.com/rizalmdj02/tisigram.git
    cd tisigram
    manage.py runserver


# Screen Capture
![alt text](https://github.com/rizalmdj02/tisigram/blob/main/static/css/screencapture-tisigram-herokuapp-2022-10-10-11_48_51.png?raw=true)

