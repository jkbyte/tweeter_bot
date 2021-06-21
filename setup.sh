#!/bin/bash

#Create and initialize a python virtual environment
echo "Creating virtual env - .venv"
python3 -m venv .venv

echo "Sourcing virtual env - .venv"
source .venv/bin/activate 

#Creating directory to put things in 
mkdir setup

#Move relevant file into setup directory
echo "Moving function files into setup dir"
cp sparrow.py setup/
cp ssm_secrets.py setup/
cd ./setup

#Install require package 
echo "pip install requirement from requirement file"
pip install -r ../requirements.txt -t .

#Prepare the deployment package
zip -r ../package.zip ./*

#Clean up the set up dir
cd ..
rm -rf ./setup
deactivate
rm -rf ./.venv

#Changing back to the dir before 
# echo "Opening folder containing function package"

# open .

