#!/bin/bash

# Parse command-line options
#
# ./sshkey.sh -g               # Generate a new key pair
# ./sshkey.sh -i               # Install an existing key on a remote server
# ./sshkey.sh -p ~/.ssh/id_rsa # Convert the id_rsa private key to the PuTTY format


#!/bin/bash

# Parse command-line options
while getopts "gi" opt; do
  case $opt in
    g)
      # Generate a new SSH key pair
      ssh-keygen -t rsa -b 4096
      ;;
    i)
      # Install an existing key on a remote server
      read -p "Enter the user name for the remote server: " user
      read -p "Enter the hostname of the remote server: " host
      read -p "Enter the path to the private key file: " key_file
      ssh-copy-id -i "$key_file" "$user@$host"
      ;;
    p)
      # Convert the key pair to the PuTTY format
      read -p "Enter the path to the private key file: " key_file
      puttygen "$key_file" -O private -o "${key_file%.*}.ppk"
      ;;
    ?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
  esac
done

