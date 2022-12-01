useradd adarsh
echo oracle | passwd --stdin adarsh
echo "adarsh ALL=(ALL) NOPASSWD: ALL"> /etc/sudoers.d/adarsh
chmod 400 /etc/sudoers.d/adarsh

