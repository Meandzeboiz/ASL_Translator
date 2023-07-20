# ASL_Translator
This AI is trained to recognize American Sign Language (ASL) fingerspelling in static images. What sets it apart from the models it was based on is the custom dataset that is in simple terms two datasets combined. after training, the program should be able to reliably and consisently recognize letters, numbers and some special gestures such as space and delete, as well as detect when there is nothing onscreen. This is a complete program albeit a very simple and common project in the end. if I had more time I would have taken time to learn how to make it detect rapid ASL fingerspelling in live camera feed
as well as having it type out outputted letters, numbers spaces and delete letters on a separate screen document or notepad. this would make the program much more unique and practical as the program would work in real time and people interacting with the mute and deaf and see what they are "typing" in ASL.
# Instructions
## Setup and Foundations
Firstly, you need both a jetson nano and an actual computer or laptop. We need the laptop as the jetson nano with its standard 32 gig microSD does not have the memory to hold all the required material and therefore cannot train the AI.
Make sure the jetson nano has pip and its libraries installed and up to date, especially pytorch. In fact, make sure your jetson can get the latest version of python 3 to avoid any annoying errors you may get. Learn how to do all of this online (this is my second time writing this as the first time i accidentally obliterated this entire documentation with on swipe of the trackpad okay? please understand i have slight sanity deficiency from this project)
Similarly, make sure you download the latest version of python 3 for your laptop or desktop computer, and install required libraries, especially pytorch (the version of pytorch must match your version of python to be compatible, at least that was what I dealt with)
In file explorer, go to desktop and make a folder titled with your name (I called mine "JacobChanSecondAttempt" but you probably will choose something else so this folder will be referred to as the "base folder.")
In this folder, make two more folders, one titled data and the other titled models. 
On juicetanz's geoguessr project github page (https://github.com/juicetanz/geoguessr-ai/tree/main), download "reshape.py" and make sure it goes to your base folder. 
On Dusty's jetsoninference github page (https://github.com/dusty-nv/pytorch-classification/tree/819b105087c397c23cd81fd9446b5f0a0213db94), download onnx_export.py, voc.py, nuswide.py, and train.py to your base folder. 
Look back at your base folder and you should see these files and a new folder called pycache that has automatically formed. This folder contains the compressed python variants of the files you just downloaded, so DO NOT DELETE IT.
On your jetson (connect and log in via SSH with putty, then go to VScode and add a host (your jetson's IP address) if you haven't already, then connect with the remote button) open the jetson inference folder in the nvidia folder. Make a new folder here titled with just your name or whatever you want to call it. Leave it alone for now. 
(Note: just as a reminder, this program will not export or function on the jetson without a properly updated pip, pytorch and sufficient version of python). 
## Fetching, organizing and fusing the datasets
We will be getting these datasets off of kaggle, BUT WE WILL NOT BE TRAINING ON THERE. DO NOT TRY TO DOWNLOAD PRETRAINED MODELS FROM THERE, THE H5 TO ONNX WILL BE COMPLETE HELL.
Download these datasets: "ASL Alphabet" by Akash, and "American Sign Language (ASL) Dataset" by Prathum Arikeri. Make sure they go to the data folder located in your base folder. 

