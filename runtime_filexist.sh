[ -e $1 ]
if [ $? == 0 ]
then
	echo "file: $1 exist"
	ls -l $1
else
	echo "file $1 does not exist"
fi


