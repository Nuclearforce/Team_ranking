#created by Christiaan Brits
#rank teams in a league using python3
#takes 1 argument, the input.txt filename in the input_files folder, for example python3 team_ranking.py test1.txt.

#import
import logging
import sys
import re

#logger config
logging.basicConfig(
    #show all info >= debug level
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("log/debug.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

#read in from .txt file and calculate scores
def process_data(input_file):
    logging.info("Reading file and calculating results")
    input_file="input_files/"+input_file
    team_ranking={}
    #open file in read mode
    with open(input_file,"r") as input:
        for line in input:
            #split by numbers and remove whitespaces and commas
            try:
                team_one,score_one,team_two,score_two=re.findall('\d+|\D+',line.replace(',','').strip())
            except:
                logging.error("Input file error")

            #calculate score
            if score_one==score_two:                
                score_one=1
                score_two=1
            elif score_one>score_two:
                score_one=3
                score_two=0
            else:
                score_one=0
                score_two=3

            #update team_ranking
            if team_one.strip() in team_ranking:
                team_ranking[team_one.strip()]+=score_one
            else:
                team_ranking.update({team_one.strip():score_one})
            if team_two.strip() in team_ranking:
                team_ranking[team_two.strip()]+=score_two
            else:
                team_ranking.update({team_two.strip():score_two})

    return team_ranking

#sorting the team based on total scores, if the scores are equal sort alphabetically
def sort_team_ranking(team_ranking):    
    logging.info("Sorting results")
    sorted_team_ranking=sorted(team_ranking.items(),key=lambda dict_key_value:(-dict_key_value[1], dict_key_value[0]))
    return sorted_team_ranking

#assign rank to team and print to file in output_files folder
def assign_rank(sorted_team_ranking,file_name):    
    logging.info("Assigning ranking")
    output_file_name="output_files/"+"output"+file_name
    rank=[]
    position=1
    equal=0
    num_teams=len(sorted_team_ranking)
    team_standing=[]

    #create list of scores
    for team,score in sorted_team_ranking: 
        rank.append(score)

    #create rank based ont he scores
    for i in range(0,num_teams):
        if i<(num_teams-1):
            if rank[i]>rank[i+1]:
                rank[i]=position
                position+=1+equal
                equal=0
            elif rank[i]==rank[i+1]:
                rank[i]=position
                equal+=1
        else:
            rank[i]=position

    with open(output_file_name,'w') as f:
        for index,(team,score) in enumerate(sorted_team_ranking):
            team_standing.append(str(rank[index])+". " +team+", "+str(score)+" pts")
            print( str(rank[index])+". " +team+", "+str(score)+" pts",file=f)

    #don't really need to return this
    return team_standing

def main():
    try:
        team_ranking=process_data(sys.argv[1])
    except:
        logging.error("The input_file needs to be given as an argument")

    sorted_team_ranking=sort_team_ranking(team_ranking)
    team_ranking_output=assign_rank(sorted_team_ranking, sys.argv[1])
    logging.info("Completed, have a nice day!")

if __name__=="__main__":
    main()
    