SOURCE="/home/john/source"
BASE="/home/john/base"
OUTPUT="/home/john/output"
COM_STRING="john@satsuki:~$"
START=0

export GIT_PAGER=""
export GIT_AUTHOR_NAME='John Haskins'
export GIT_AUTHOR_EMAIL='john.haskins@tamagoyakiinc.koala'
export GIT_COMMITTER_NAME=$GIT_AUTHOR_NAME
export GIT_COMMITTER_EMAIL=$GIT_COMMITTER_EMAIL

export GIT_COMMITTER_DATE=$GIT_AUTHOR_DATE
export GIT_AUTHOR_DATE=2005-01-01T12:35:00

if [ ! -d "$BASE" ]; then
	mkdir $BASE
fi

if [ ! -d "$SOURCE" ]; then
	mkdir $SOURCE
fi

if [ ! -d "$OUTPUT" ]; then
	mkdir $OUTPUT
fi

# Change Directory to the OUTPUT and cleanup
cd $OUTPUT
rm * -Rf

# Change Directory to the BASE and cleanup
cd $BASE
rm * -Rf

cd $SOURCE

TOGA=$( ls )

cd $BASE

for i in $TOGA; do
	echo ${i}
	    while read line; do
    echo $line
    if [ "*" == ${line:0:1} ]; then
		echo "Non outputable"
		eval ${line:1}
	fi
	echo "${COM_STRING}" ${line} > ${OUTPUT}/${i}
	#echo "${line}" ${line} >> ${OUTPUT}/${i}
	eval ${line} &>> ${OUTPUT}/${i}
    done < $SOURCE/${i}
done

#runcommand 'mkdir coderepo' 'mkdir coderepo'
#runcommand 'cd coderepo'
#runcommand 'git init'
#runcommand 'touch my_first_committed_file'
#runcommand 'git add my_first_committed_file'
#runcommand 'git commit -m "My First Ever Commit"'
#runcommand 'echo "Change1" > my_first_committed_file'
#runcommand 'touch my_second_committed_file'
#runcommand 'touch my_third_committed_file'
#runcommand 'git --no-pager status' 'git status'
#runcommand 'git add my_first_committed_file'
#runcommand 'echo "Change1" > my_second_committed_file'
#runcommand 'git add my_second_committed_file'
#runcommand 'git --no-pager status' 'git status'
#runcommand 'echo "Change2" >> my_second_committed_file'
#runcommand 'git --no-pager status' 'git status'
#runcommand 'git commit -m "Made a few changes to first and second files"'
#runcommand 'git --no-pager status' 'git status'
#runcommand 'git commit -a -m "Finished adding initial files"'
#runcommand 'git --no-pager status' 'git status'
#runcommand 'git add my_third_committed_file'
#runcommand 'git --no-pager status' 'git status'
#runcommand 'git reset my_third_committed_file'
#runcommand 'git --no-pager status' 'git status'

