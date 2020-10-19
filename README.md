# population-rollup
Insight Data Engineering - Coding Challenge
<br />
<br />
1. In this challenge, I dropped the missing values directly.

2. For the part of calculating average population percent change (PPCHG), I dropped the rows that contain 0 values in the year of 2000. 

3. The python version I used in this challenge is python 3.8, and the package/library I used is pandas.

4. I cannot pass your tester because it gave me the error "ModuleNotFoundError: No module named 'pandas'", which means that your tester service does not support pandas I think.

5. I did 2 tests locally, and I provided the results in the directory "insight_testsuite/tests". (I provided the result with the input of the whole dataset as my 2nd try.)

6. Big update! I created a new version without using pandas. The new version is named "population-rollup-no-Pandas.py". I used this new version and finally passed the tester.
