if [[ "$(docker images -q)" ]]; then
  echo "hello world"
else
  echo "no image"
fi 
