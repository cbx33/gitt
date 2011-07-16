BASE="/home/john/testscript"
OUTPUT="/home/john/outputs"
START=0

function runcommand {
	if [ "$2" == "" ]; then
		echo "$1" > ${OUTPUT}/`printf "%02d" $START`.txt
		$1 &>> ${OUTPUT}/`printf "%02d" $START`.txt
	else
		echo "$2" > ${OUTPUT}/`printf "%02d" $START`.txt
		$1 &>> ${OUTPUT}/`printf "%02d" $START`.txt
	fi
	let "START += 1"
}

if [ ! -d "$BASE" ]; then
	mkdir $BASE
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

runcommand 'mkdir coderepo' 'mkdir coderepo'
runcommand 'cd coderepo'
runcommand 'git init'
runcommand 'touch my_first_committed_file'
runcommand 'git add my_first_committed_file'
runcommand 'git commit -m "My First Ever Commit"'
runcommand 'echo "Change1" > my_first_committed_file'
runcommand 'touch my_second_committed_file'
runcommand 'touch my_third_committed_file'
runcommand 'git --no-pager status' 'git status'
runcommand 'git add my_first_committed_file'
runcommand 'echo "Change1" > my_second_committed_file'
runcommand 'git add my_second_committed_file'
runcommand 'git --no-pager status' 'git status'
runcommand 'echo "Change2" >> my_second_committed_file'
runcommand 'git --no-pager status' 'git status'
runcommand 'git commit -m "Made a few changes to first and second files"'
runcommand 'git --no-pager status' 'git status'
runcommand 'git commit -a -m "Finished adding initial files"'
runcommand 'git --no-pager status' 'git status'
runcommand 'git add my_third_committed_file'
runcommand 'git --no-pager status' 'git status'
runcommand 'git reset my_third_committed_file'
runcommand 'git --no-pager status' 'git status'

