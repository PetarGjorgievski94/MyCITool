# MyCITool

## Introduction
MyCITool is a relatively light implementation of python code in order to automatically download a targeted repository application, build it and deploy it on a container.

## Requirements 
This tool requires a docker daemon to be running. 

In order to use this tool, you must config your global git credentials using:

`git config --global user.name "YourUsername"`

`git config --global user.email YourEmail@example.com`

## Install dependancies
Clone the repo and run the following command:

`pip install -r requirements.txt`

## Usage

Run the `MyCITool.py` script and provide a like of the repository you would like to use.

## Limitation

This version was designed to work with a single repository: https://github.com/guyyosan/python-cherry-container

So, in order to execute it, copy this repository link and provide it as input to the tool.
It is developed as a proof of concept and is relatively simple. The input can be further parametrized and built upon.
