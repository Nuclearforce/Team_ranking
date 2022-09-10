# author: Christiaan Brits
# test script to test the outputs from team_ranking.py. 
# This script will run team_ranking.py with the input_file defined as a variable for example python3 test.py. 

import subprocess

def compare_result(input_file, result):
    result2=[]
    file_location="output_files/"+"output"+input_file
    with open(file_location,"r") as input:
        for line in input:
            result2.append(line.strip())
    if result==result2:
        print("testcase passes")
    else:
        print("testcase failed")
        print(result2)
        print(result)

def main():
    test_command_line="python3 team_ranking.py"

    #test1, change input file name and expected result
    input_file_one= "test1.txt"
    result_test1=['1. Tarantulas, 6 pts', '2. Lions, 5 pts', '3. FC Awesome, 1 pts', '3. Snakes, 1 pts', '5. Grouches, 0 pts']
    run_command=test_command_line+" "+input_file_one
    subprocess.run(run_command, shell=True)
    compare_result(input_file_one, result_test1)

    #test2 change input file name and expected result
    input_file_two= "test2.txt"
    result_test2=['1. Tarantulas, 6 pts', '2. Lions, 5 pts', '3. Unicorns, 3 pts', '4. FC Awesome, 1 pts', '4. Snakes, 1 pts', '6. Grouches, 0 pts']
    run_command=test_command_line+" "+input_file_two
    subprocess.run(run_command, shell=True)
    compare_result(input_file_two, result_test2)

    #test3 change input file name and expected result
    input_file_three= "test3.txt"
    result_test3=['1. Tarantulas, 6 pts', '2. Lions, 5 pts', '3. Unicorns, 4 pts', '4. Cheetah, 1 pts', '4. FC Awesome, 1 pts', '4. Snakes, 1 pts', '7. Grouches, 0 pts']
    run_command=test_command_line+" "+input_file_three
    subprocess.run(run_command, shell=True)
    compare_result(input_file_three, result_test3)

if __name__=="__main__":
    main()