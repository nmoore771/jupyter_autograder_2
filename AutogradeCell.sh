echo "Testing Cell #: $1"
echo "In Notebook: $2"
python3 scoop.py $@
gcc -w answer.c -o answer
if [ $? -eq 0 ]; then
    echo "Code compiles!"
    ./answer 
    echo "Code Executes!"
    exit $?
else
    echo "Code failed to compile!"
    exit -1
fi
exit 0