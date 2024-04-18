pip3 install Django
sudo apt install python3-Django

cd HyperPOS

sudo rm -rf db.sqlite3

python3 manage.py migrate

python3 manage.py collectstatic

echo "Next, please create a superuser:"
python3 manage.py createsuperuser

# Move back to the parent directory
cd ..

echo "Now, we will build the Docker container."

sudo docker build -t hyperpos .

read -p "Do you want to start the container now? (yes/no): " choice

if [ "$choice" = "yes" ]; then
    sudo docker run -it -d -p 8000:8000 hyperpos
    echo "The HyperPOS container has been successfully started."
else
    echo "Thanks for completing the installation."
fi
