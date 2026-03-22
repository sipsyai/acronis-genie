---
title: "Setting up the Python environment"
source: "https://developer.acronis.com/doc/outbound/apis/getting-started/set-up-python.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:27:41.036189"
---

# Setting up the Python environment

Setting up the Python environment

Note

Code samples in the Acronis API guides are in Python (version 3.7). Python was chosen because it is a simple, self-explanatory, easy-to-start, and widely used language.
A basic knowledge of Python is required. Even if you are not familiar with Python, it will not be difficult to understand the code in these guides.
A good way to start with Python is to follow the Python tutorial.



To set up the Python environment in Windows

Download the installer for the latest version of Python 3.
Run the installer.
Select Add Python 3.x to PATH.

Click Install Now.
The installer installs Python and pip (a tool for installing and managing Python packages locally) in your user folder, and adds folders with Python executables to your user path.


Start the command line.
Install the requests package that is required for sending requests to the API:
pip install requests






To set up the Python environment in Mac OS X

Start the terminal.
Install Python 3 and pip (a tool for installing and managing Python packages locally).
Install the requests package that is required for sending requests to the API:
pip install requests






To set up the Python environment in Linux

Start the terminal.
Check if Python 3 is already installed:
python --version


If Python 3 is not installed, install it via your distribution’s package manager.
The command and package names vary.

In Debian and derivatives such as Ubuntu, use apt:
sudo apt-get install python3



In Red Hat and derivatives, use yum:
sudo yum install python3



In SUSE and derivatives, use zypper:
sudo zypper install python3





Install pip (a tool for installing and managing Python packages locally).
Install the requests package that is required for sending requests to the API:
pip install requests