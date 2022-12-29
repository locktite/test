#!/bin/bash
# chmod +x firewall_rules.sh
# ./firewall_rules.sh > firewall_rules.html

# Create the HTML header
#!/bin/bash

# Create the HTML header
echo "<html>"
echo "<head>"
echo "<style>"
echo "table, th, td { border: 1px solid black; border-collapse: collapse; }"
echo "th, td { padding: 5px; }"
echo "</style>"
echo "</head>"
echo "<body>"

# Create the table for the firewall rules
echo "<h1>Firewall Rules</h1>"
echo "<table>"
echo "<tr>"
echo "<th>Protocol</th>"
echo "<th>Source IP</th>"
echo "<th>Source Port</th>"
echo "<th>Destination IP</th>"
echo "<th>Destination Port</th>"
echo "<th>Action</th>"
echo "<th>Opposite Command</th>"
echo "</tr>"

# Loop through each line of the firewall rules and extract the relevant information
while read -r line; do
  # Extract the protocol, source IP, source port, destination IP, destination port, and action
  protocol=$(echo "$line" | awk '{print $1}')
  src_ip=$(echo "$line" | awk '{print $2}')
  src_port=$(echo "$line" | awk '{print $3}')
  dst_ip=$(echo "$line" | awk '{print $4}')
  dst_port=$(echo "$line" | awk '{print $5}')
  action=$(echo "$line" | awk '{print $6}')

  # Generate the opposite command
  if [ "$action" == "ACCEPT" ]; then
    opposite_cmd="iptables -I INPUT -p $protocol -s $src_ip --sport $src_port -d $dst_ip --dport $dst_port -j DROP"
  elif [ "$action" == "DROP" ]; then
    opposite_cmd="iptables -I INPUT -p $protocol -s $src_ip --sport $src_port -d $dst_ip --dport $dst_port -j ACCEPT"
  else
    opposite_cmd="N/A"
  fi

  # Add a row to the table for this rule
  echo "<tr>"
  echo "<td>$protocol</td>"
  echo "<td>$src_ip</td>"
  echo "<td>$src_port</td>"
  echo "<td>$dst_ip</td>"
  echo "<td>$dst_port</td>"
  echo "<td>$action</td>"
  echo "<td>$opposite_cmd</td>"
  echo "</tr>"
done < <(iptables -S)

echo "</table>"

# Close the HTML
echo "</body>"
echo "</html>"

