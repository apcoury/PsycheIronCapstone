# NASA Psyche Capstone Project: Visualizing Space Data Footprints

  16 Psyche is an asteroid that orbits the sun between Jupiter and Mars, and inspired the name of the mission led by ASU and NASA to visit this asteroid, launching in 2022. It is hypothesized to have an iron core, and its study could lead to further advancements in the knowledge we have about Earth’s core. The Psyche mission will be the first to investigate a world of metal as opposed to that of ice and rock.
  
  Our team implemented a solution to take NASA SPICE Toolkit Kernels which contain graphical information from NASA space missions, a corresponding shape model, and user input such as a specific time and instrument. Then we  export a .csv file with coordinates of where the shape model intersects with the instrument’s field of view. 

## Getting Started

  This project can run on Windows, Linux, or Mac OS. 
  
  Compatible IDE's include:
* VS Code (used for this example)
* Pycharm
* Sublime
* Notepad++
* Other python-compatible IDE's (the above are just the ones that have been successfully used)
  
### Prerequisites

You will need to install a version of Python (3.6 or greater): [Python Download] (https://www.python.org/)

Then have an interpreter and IDE of your choice installed.

### Installing

First, clone this repo to your computer by running the following command in your terminal in the directory you would like to download it to (or download the zip file and extract the files to that directory)

```
git clone git@github.com:apcoury/PsycheIronCapstone.git
```

Then, open the folder in your IDE and, if applicable, open an instance of the terminal. Otherwise, open a separate terminal and navigate to the directory where the folder was cloned. 

Navigate to the PythonGUI folder and open the psyche_app.py file. Then, in the terminal, enter the following commands for each dependency needed (import *dependency* is at the top of the file to show needed dependencies). For example:

```
pip install spiceypy
```

Once all the dependencies are installed, run the following command in the terminal. 

```
python psyche_app.py
```

The following application window should appear and you can now successfully use the application:

![Image of Application Demo](https://github.com/apcoury/PsycheIronCapstone/blob/master/images/PythonGUIExample.PNG)

## Deployment

  Once the application is functioning. Go to the NAIF SPICE Toolkit Website. Click on 'Data' in the list of links on the left hand side. Then, click the link 'PDS Archived SPICE Data Sets', then click the 'PDS SPICE Archives' link. Scroll down to the bottom of the page and click on 'Archive Link' for whatever mission you would like to use with the system (this example uses Cassini). Then, navigate to the data->dsk folder and download the most recent .bds file to your computer (in the same directory as the other files).

  After saving the .bds file, use the application (as demonstrated in the above image) to specify a time frame, reference number, target and observer numbers, and import and select the current kernel. Then presh the 'export kernel' button and a file will be generated with points where the camera's field of view intersects with the body of the chosen mission figure at the chosen time.
  
  Once you find and open the file in your directory the program has worked successfully. If you are having issues getting installation or deployment to work. Make sure you are using an updated version of python, have installed all necessary dependencies, and stored a valid .bds file to your local directory.

## Built With

* [NAIF SPICE Toolkit](https://maven.apache.org/) - Database to pull data from
* [SpiceyPy](https://spiceypy.readthedocs.io/en/master/) - Dependency to access the SPICE Toolkit Functions
* [Meshlab](http://www.meshlab.net/) - 3D visualization of the shape model

## Contributors

* **Abrahm Coury** - [apcoury](https://github.com/apcoury)
* **Saharaj Asa** - [SaharajAsa](https://github.com/SaharajAsa)
* **Edwin Jose** - [SlivMus](https://github.com/SlivMus)
* **Pragathi Gopal** - [pragu5411](https://github.com/pragu5411)
* **Christopher Warren** - [cwarren131](https://github.com/cwarren131)
* **Yifan Tian** - [yifantian46](https://github.com/yifantian46)

## Acknowledgments

* Thanks to our project sponsors Cassie Bowman and Scott Dickenshied, and our professor Ryan Meuth for their help and feedback on the project
