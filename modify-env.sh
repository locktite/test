#!/bin/bash

# Ask the user if they want to add the PATH to the global or local environment
echo "Do you want to add the PATH to the global or local environment?"
read -p "Enter 'global' or 'local': " env

# If the user entered 'global', add the PATH to the /etc/environment file
if [ "$env" == "global" ]; then
  read -p "Enter the PATH you want to add: " path
  echo "PATH=$path" >> /etc/environment
  source /etc/environment

# If the user entered 'local', add the PATH to the ~/.bashrc file
elif [ "$env" == "local" ]; then
  read -p "Enter the PATH you want to add: " path
  echo "export PATH=$path:$PATH" >> ~/.bashrc
  source ~/.bashrc
fi

# Ask the user if they want to add generic data to the environment
read -p "Do you want to add generic data to the environment? (y/n) " add_data

# If the user wants to add data, ask for the data and add it to the appropriate configuration file
if [ "$add_data" == "y" ]; then
  # Keep asking for data until the user's input is blank
  while :
  do
    read -p "Enter the data you want to add (blank to stop): " data
    if [ -z "$data" ]; then
      break
    fi
    # Print a comment showing the syntax of the export command
    echo "Syntax: export VARNAME=value"
    export $data
  done
fi

echo "Done! The PATH and generic data have been added to your environment."
