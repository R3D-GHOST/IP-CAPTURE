arch=uname -m
if [[ ("$arch" == *'arm'*) || ("$arch" == *'Android'*) ]]; then
   ssh -R 80:localhost:8080 nokey@localhost.run -T -n
elif [[ "$arch" == *'x86_64'* ]]; then
   ssh -R 80:localhost:8080 nokey@localhost.run -T -n
elif
    ssh -R 80:localhost:8080 nokey@localhost.run -T -n
fi