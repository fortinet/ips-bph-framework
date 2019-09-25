
NAT_NIC=$1
HOSTONLY_NIC=$2

echo "NAT ONLY NIC: 	$NAT_NIC"
echo "HOST-ONLY NIC:	$HOSTONLY_NIC"

# ACTIVATION
sudo iptables -F
sudo iptables --table nat --delete-chain
sudo iptables --table nat --append POSTROUTING --out-interface $NAT_NIC -j MASQUERADE
sudo iptables --append FORWARD --in-interface $HOSTONLY_NIC -j ACCEPT

# PORT REDIRECTION
sudo iptables -t nat -A PREROUTING -i $HOSTONLY_NIC -p tcp --dport 80 -j REDIRECT --to-ports 8080
sudo iptables -t nat -A PREROUTING -i $HOSTONLY_NIC -p tcp --dport 443 -j REDIRECT --to-ports 8080
sudo iptables -t nat -A PREROUTING -i $HOSTONLY_NIC -p tcp --dport 53 -j REDIRECT --to-ports 53
sudo iptables -t nat -A PREROUTING -i $HOSTONLY_NIC -p udp --dport 53 -j REDIRECT --to-ports 53

# ACCEPT ALL IPS
sudo iptables -t nat -A PREROUTING -i $HOSTONLY_NIC -j REDIRECT
