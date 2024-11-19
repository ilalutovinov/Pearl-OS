<h1 align="center">Welcome to the project Pearl OS! <img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="40"></h1>
<br />

![Cover.png)](Documents/Cover.png)

<br />

# Project: Peral OS - Arduino UNO Integration with Raspberry Pi


# <img src="Documents/Pearl_Logo%20png.png" alt="Pearl_Logo png" width="40" style="vertical-align: middle"/> About Peral OS

**Peral OS** is a project aimed at creating an operating system that integrates the capabilities of **Arduino UNO** and **Raspberry Pi** into a unified platform for automation and smart home applications. The project's goal is to achieve full integration of hardware and software solutions, ensuring flexibility and scalability with the ability to control devices and collect data from various sensors.

## Project Goals and Objectives

- **Integration of Arduino UNO and Raspberry Pi**: Development of software that enables Raspberry Pi to interact with Arduino UNO for controlling devices and collecting data from various sensors via serial communication.
  
- **Full integration with the operating system**: Development of a complete operating system that will run on Raspberry Pi and support interaction with the connected Arduino UNO, including device control (such as relays), sensor data reading, and communication between devices.

- **Software Development**: Creation of drivers and libraries to simplify working with Arduino within the integrated system, as well as developing a GUI interface for managing settings and monitoring the system.

- **Process Automation**: Development of an automatic response system based on sensor data (e.g., turning devices on/off based on temperature, humidity, and other factors) with the option for remote control via a web interface or mobile app.

- **Flexibility and Scalability**: Ensuring the ability to connect various sensors and actuators, as well as expanding the system with additional devices and modules.

## System Architecture

- **Raspberry Pi** will act as the central hub of the system, processing data, providing a web interface, and controlling all connected devices.
  
- **Arduino UNO** will be used to collect data from sensors and control actuators (e.g., relays for managing outlets, lights, and other devices).

- **Software** will include an operating system kernel, drivers for Arduino interaction, and a user interface for monitoring and managing the system.
## Technical Components of the Project
### 🛠 &nbsp;Languages and Tools :

<p>
<img src="https://github.com/devicons/devicon/blob/master/icons/html5/html5-original.svg" title="HTML5" alt="HTML" width="40" height="40"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/css3/css3-plain-wordmark.svg"  title="CSS3" alt="CSS" width="40" height="40"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/javascript/javascript-original.svg" title="JavaScript" alt="JavaScript" width="40" height="40"/>&nbsp;
<img src="https://raw.githubusercontent.com/devicons/devicon/6910f0503efdd315c8f9b858234310c06e04d9c0/icons/php/php-original.svg" title="php" alt="php" width="40" height="40"/>&nbsp;
<img src="https://raw.githubusercontent.com/devicons/devicon/6910f0503efdd315c8f9b858234310c06e04d9c0/icons/python/python-original.svg" title="Python"  alt="Python" width="40" height="40"/>&nbsp;
<img src="https://raw.githubusercontent.com/devicons/devicon/6910f0503efdd315c8f9b858234310c06e04d9c0/icons/django/django-plain.svg" title="Django"  alt="Django" width="40" height="40"/>&nbsp;
<img src="https://raw.githubusercontent.com/devicons/devicon/6910f0503efdd315c8f9b858234310c06e04d9c0/icons/docker/docker-original.svg" title="Docker"  alt="Docker" width="40" height="40"/>&nbsp;
<img src="https://raw.githubusercontent.com/devicons/devicon/6910f0503efdd315c8f9b858234310c06e04d9c0/icons/git/git-original.svg" title="Git"  alt="Git" width="40" height="40"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/mysql/mysql-original-wordmark.svg" title="MySQL"  alt="MySQL" width="40" height="40"/>&nbsp;
<img src="https://raw.githubusercontent.com/devicons/devicon/6910f0503efdd315c8f9b858234310c06e04d9c0/icons/visualstudio/visualstudio-plain.svg" title="visualstudio"  alt="visualstudio" width="40" height="40"/>&nbsp;
</p>

---
- **Hardware Components**:
  - Raspberry Pi
  - Arduino UNO
  - Sensors (temperature, humidity, motion, and others)
  - Relays for controlling devices
  - Communication modules (e.g., Wi-Fi or Bluetooth)

- **Software Components**:
  - Python, C/C++
  - Arduino libraries (e.g., Firmata)
  - GUI interface based on Flask or Django for system management
  - Notification systems and data analytics

## Expected Outcomes

- A fully integrated platform where Raspberry Pi and Arduino work together as a unified system.
- The ability to remotely control the system via a web interface or mobile app.
- Automation and real-time device status monitoring.
- A flexible system supporting extensions and the addition of new sensors or actuators.

## Project structure
```bash
Pearl OS/ # Main project folder
│
├── templates/ # Folder for HTML templates
│ ├── accounts/ # Templates for the accounts application
│ │ ├── create-account.html # Registration page
│ │ └── login.html # Login page
│ │
│ ├── pages/ # Folder for individual static pages
│ │ ├── 404.html # Error page 404
│ │ ├── blank.html # Blank page
│ │ ├── buttons.html # Page with buttons
│ │ ├── cards.html # Page with cards
│ │ ├── charts.html # Page with charts
│ │ ├── forms.html # Page with forms
│ │ ├── modals.html # Page with modal windows
│ │ └── tables.html # Page with tables
│ │
│ └── index.html # Main page
│
├── static/ # Folder for static files
│ ├── assets/ # Static resources (CSS, JS, images)
│ │ ├── css/ # CSS files
│ │ │ ├── tailwind.css # Main CSS file
│ │ │ └── tailwind.output.css # Compiled CSS file
│ │ │
│ │ ├── js/ # JS files
│ │ │ ├── charts-bars.js # Script for bar charts
│ │ │ ├── charts-lines.js # Script for line charts
│ │ │ └── charts-pie.js # Script for pie charts
│ │ │
│ │ └── img/ # Images for the project
│ │ ├── login-office.jpeg # Image for login page
│ │ ├── create-account-office.jpeg # Image for registration page
│ │ └── dashboard.png # Image for control panel
│
├── dashboard/ # Application for main control panel
│ ├── __init__.py # Application initialization
│ ├── settings.py # Project settings
│ ├── urls.py # Main URL configuration
│ ├── wsgi.py # For WSGI deployment
│ └── asgi.py # For asynchronous deploy
│
├── manage.py # Script for project management (migrations, server launch, etc.)

```
## Quick start

> 👉 Download the code  

```bash
$ https://github.com/ilalutovinov/Pearl-OS.git
$ cd Pearl-OS 
```

<br />

> 👉 Install modules via `VENV`  

```bash
$ python -m venv env
$ .\env\Scripts\Activate
```

<br />


> 👉 Performing the migration

```bash
$ python manage.py migrate
```

<br />

> 👉 Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />
