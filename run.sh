#!/bin/bash

# Load environment variables from .env file
export $(cat .env | grep -v '^#' | xargs)

# Run the program
./venv/bin/python Web-LLM.py
