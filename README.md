
# FLASK API with uWSGI on a 1&1 IONOS VPS

How to run a python flask api, on a IONOS VPS, with uWSGI and route it to your ip with nginx.

- [Setup](#setup)
  * [Git](#git)
  * [File setup](#file-setup)
  * [Server setup](#server-setup)
  * [Server strukture](#server-strukture)
  * [Setup VENV](#setup-venv)
  * [Checking service state](#Checking-service-state)
- [API Reference](#api-reference)
- [Troubleshooting](#Troubleshooting)
  * [uWSGI service](#uWSGI-service)
- [stoecklin.io 🚀](#🚀-stoecklin.io)
  * [Acknowledgements](#acknowledgements)

## Setup
Small description how to upload the files, obducted by the git clone.
### Git
Clone the project in to your repostiory
```bash
  git clone git@github.com:Kehrblech/user_api_ionos.git
```
### File setup
Go to the provided requirements folder and edit the file myapp.

Edit the server_name to your VPS IP or your given DNS-Hostname or even both.
``` ini
    server {
        listen 80;
        server_name 0.0.0.0 your-domain.example;

        location / {
            include uwsgi_params;
            uwsgi_pass unix:/tmp/myapp.sock;
        }
    }
```
This file need to be linked later on, therefore please dont give it an file extenstion.
### Server setup
Before we start we need to setup some things on our VPS.
#### uWSGI User
```bash
    sudo adduser username
```
Go to the provided api_genie folder and edit the file myapp.ini.
```ini
    [uwsgi]
    uid = username
```
Use your IONOS VPS update it with the command:
```bash
  sudo apt update
```
Install following packages:
```bash
  sudo apt install python3 python3-pip python3-venv
  sudo apt install flask
  sudo apt install nginx
```
After successfully installing pip, run following commands:
```bash
  pip install flask uwsgi
  pip install flask-restful
  pip3 install flask
```
#### Setup Firewall
```bash
    sudo apt install ufw
    sudo ufw enable
    sudo ufw allow 80/tcp
```
### Server strukture
```bash
    /var/www/api_genie/
    ├── /venv/ (this folder virtual enviroment folder need to be installed by you)
    ├── app.py
    ├── zehntausend.py
    ├── myapp.ini
    └── requirements.txt

    /etc/nginx/sites-available/
    └── myapp

    /etc/systemd/system/
    └── myapp.service
```
You need to upload the api_genie & requirements folder to your VPS, via your preferd method. In my Case that would be SFTP. 

Upload the api_genie folder to following path:
```bash
    /var/www/
```
Upload the file myapp from the requirements folder to the following path: 
```bash
    /etc/nginx/sites-available
```
Upload the file myapp.service from the requirements folder to the following path: 
```bash
    /etc/systemd/system/
```
Afterwards open up a terminal and type:
```bash
    sudo ln -s /etc/nginx/sites-available/myapp /etc/nginx/sites-enabled/
```
to symbolic link the content.

After creating the symbolic link, you can test the configuration and restart NGINX to apply the changes:
```bash
    sudo nginx -t
    sudo systemctl restart nginx
```
### Setup VENV
You need to set up a virtual environment for your application, to run securely.
#### Install VENV
Navigate to app root folder:
```bash
    cd /var/www/api_genie
```
Create a new virtual environment using venv(for simplicity we named the folder venv):
```bash
    python3 -m venv venv
```
#### Activate VENV
Activate the virtual environment in the app root location:
```bash
    source venv/bin/activate
```
You will see the name of your virtual environment in your command prompt to indicate that it's active. You can now start developing your Flask API in the virtual environment.
#### Installing dependencies 
You need to install all the dependencies again in your virtual enviroment.
```bash
    pip install flask
    pip install flask_restful
    pip install uwsgi
```
#### Deactivate VENV
 When you're done, you can deactivate the virtual environment by running: 
```bash
    deactivate
```
### Checking service state
To start the service, open up a terminal and type:
```bash
    sudo systemctl enable myapp
    sudo systemctl start myapp
```
To check the status again use: 
```bash
    sudo systemctl status myapp
```
## API Reference

#### Get all items

```http
  GET /user
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `random`  | `string` |  Fetches random user       |

#### Get user with id 

```http
  GET /user/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int`    | **Required**. Id of user to fetch |

#### Get users in array

```http
  GET /user/size={num}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `num`     | `int`    | **Required**. Defines array size  |


#### Get user with specific gender

```http
  GET /user/{gender}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `gender`  | `string` | **Required**. diverse/female/male |

#### Get array of users with specific gender

```http
  GET /user/{gender}/size={num}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `gender`  | `string` | **Required**. diverse/female/male |
| `num`     | `int`    | **Required**. Size of Array       |
## Troubleshooting
### uWSGI service
#### Check the state
```bash
    sudo systemctl status myapp
```
if its not running try to start it again using:
```bash
    sudo systemctl daemon-reload
    sudo systemctl restart myapp
```
#### Further service troubleshooting
Following command could help you to identify the Problem:
```bash
    sudo journalctl -u myapp
```

## 🚀 stoecklin.io



### Author

- [@Kehrblech](https://www.github.com/Kehrblech)


### Acknowledgements

 - Idea from [random-data-api.com](https://random-data-api.com/)
 - Avatars from [dicebear.com](https://www.dicebear.com/)


