BASE="/home/john/testscript"
OUTPUT="/home/john/outputs"

if [ ! -d "$BASE" ]; then
	mkdir $BASE
fi

if [ ! -d "$OUTPUT" ]; then
	mkdir $OUTPUT
fi

# Change Directory to the BASE
cd $BASE

rm * -Rf

mkdir coderepo
cd coderepo
git init &> "${OUTPUT}/1.txt"
touch my_first_committed_file &> "${OUTPUT}/2.txt"
git add my_first_committed_file &> "${OUTPUT}/3.txt"
git commit -m "My First Ever Commit" &> "${OUTPUT}/4.txt"
echo "Change1" > my_first_committed_file &> "${OUTPUT}/5.txt"
touch my_second_committed_file &> "${OUTPUT}/6.txt"
touch my_third_committed_file &> "${OUTPUT}/7.txt"
git --no-pager status &> "${OUTPUT}/8.txt"
git add my_first_committed_file &> "${OUTPUT}/9.txt"
echo "Change1" > my_second_committed_file &> "${OUTPUT}/10.txt"
git add my_second_committed_file &> "${OUTPUT}/11.txt"
git --no-pager status &> "${OUTPUT}/12.txt"
echo "Change2" >> my_second_committed_file &> "${OUTPUT}/13.txt"
git --no-pager status &> "${OUTPUT}/14.txt"
git commit -m "Made a few changes to first and second files" &> "${OUTPUT}/15.txt"
git status &> "${OUTPUT}/16.txt"
git commit -a -m "Finished adding initial files" &> "${OUTPUT}/17.txt"
git status &> "${OUTPUT}/18.txt"
git add my_third_committed_file &> "${OUTPUT}/19.txt"
git status &> "${OUTPUT}/20.txt"
git reset my_third_committed_file &> "${OUTPUT}/21.txt"
git status &> "${OUTPUT}/22.txt"
