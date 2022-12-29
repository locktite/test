#!/bin/bash

# Function to add a user
add_user() {
  # Check if the user already exists
  if id -u "$1" > /dev/null 2>&1; then
    echo "User $1 already exists"
  else
    # Add the user
    useradd "$1"
    echo "User $1 added successfully"
  fi
}

# Function to delete a user
delete_user() {
  # Check if the user exists
  if id -u "$1" > /dev/null 2>&1; then
    # Delete the user
    userdel "$1"
    echo "User $1 deleted successfully"
  else
    echo "User $1 does not exist"
  fi
}

# Function to add a user to a group
add_user_to_group() {
  # Check if the user exists
  if id -u "$1" > /dev/null 2>&1; then
    # Check if the group exists
    if grep "^$2:" /etc/group > /dev/null 2>&1; then
      # Add the user to the group
      usermod -a -G "$2" "$1"
      echo "User $1 added to group $2 successfully"
    else
      echo "Group $2 does not exist"
    fi
  else
    echo "User $1 does not exist"
  fi
}

# Function to remove a user from a group
remove_user_from_group() {
  # Check if the user exists
  if id -u "$1" > /dev/null 2>&1; then
    # Check if the group exists
    if grep "^$2:" /etc/group > /dev/null 2>&1; then
      # Remove the user from the group
      gpasswd -d "$1" "$2"
      echo "User $1 removed from group $2 successfully"
    else
      echo "Group $2 does not exist"
    fi
  else
    echo "User $1 does not exist"
  fi
}

# Function to count the number of users in each group
count_users_in_groups() {
  # Get a list of all groups
  groups=$(cut -d: -f1 /etc/group)

  # Iterate over the groups and count the number of users in each group
  for group in $groups; do
    # Get the list of users in the group
    users=$(grep "^$group:" /etc/group | cut -d: -f4)

    # Count the number of users in the group
    count=$(echo "$users" | wc -w)

    # Print the group name and the number of users
    echo "$group: $count"
  done
}


# Function to export all data to HTML
export_to_html() {
  # Create the HTML file
  echo "<html>" > user_data.html
  echo "<head>" >> user_data.html
  echo "<title>User Data</title>" >> user_data.html
  echo "</head>" >> user_data.html
  echo "<body>" >> user_data.html

  # Add a heading to the HTML file
  echo "<h1>User Data</h1>" >> user_data.html

  # Add a table to the HTML file
  echo "<table>" >> user_data.html
  echo "<tr>" >> user_data.html
  echo "<th>Username</th>" >> user_data.html
  echo "<th>Groups</th>" >> user_data.html
  echo "</tr>" >> user_data.html

  # Get a list of all users
  users=$(cut -d: -f1 /etc/passwd)

  # Iterate over the users and add their data to the HTML file
  for user in $users; do
    # Get the list of groups for the user
    groups=$(groups "$user" | cut -d: -f2)

    # Add a row to the HTML table for the user
    echo "<tr>" >> user_data.html
    echo "<td>$user</td>" >> user_data.html
    echo "<td>$groups</td>" >> user_data.html
    echo "</tr>" >> user_data.html
  done

  # Close the table and the body and html tags
  echo "</table>" >> user_data.html
  echo "</body>" >> user_data.html
  echo "</html>" >> user_data.html
}
