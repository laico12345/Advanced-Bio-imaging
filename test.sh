SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"

docker run -v $SCRIPTPATH:/app cwlabcourse

if [ $? -eq 0 ]; then
    echo "Tests successfully passed..."
else
    echo "Expected output was not found..."
fi
