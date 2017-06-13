for run in {1..100000}
do
  echo $run
  pypy test.py  
  pypy q6_2.py < input.txt > output.txt
  pypy q6_3.py < input.txt > output1.txt
  diff output.txt output1.txt
  if [ $? != 0 ]; then
      exit 1
  fi
done
