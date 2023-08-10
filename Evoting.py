import json
# javascript object notation
def main():
    # Opening the json file 
    file1 = open('election.json')
    candidateSys = json.load(file1)
    
    # use json file
    print("Candidates available in voting: ")
    print("1.modi 2.mamta 3.rahul")

    while(True):
        # try:
        no = int(input("press indivdual no to vote : "))
        break
        #  except TypeError:
        #  continue
    setVote(no, candidateSys)

    print(f"1.modi : {candidateSys['candidates'][0]['votes']} 2.mamta: {candidateSys['candidates'][1]['votes']} 3.rahul: {candidateSys['candidates'][2]['votes']}")

    # saving the json file in electionEnd
    with open('electionEnd.json' , 'w') as file2:
        data = json.dump(candidateSys, file2)
def setVote(candidateNo , candidateSys):
    match candidateNo:
        case 1:
            m = candidateSys['candidates'][0]['votes']
            m += 1
            candidateSys['candidates'][0]['votes'] = m 
            
        case 2:
            m = candidateSys['candidates'][1]['votes']
            m += 1
            candidateSys['candidates'][1]['votes'] = m 
        case 3:
            m = candidateSys['candidates'][2]['votes']
            m += 1
            candidateSys['candidates'][2]['votes'] = m 
        case default:
            print(" Please choose correct symbols")


if __name__ == "__main__":
    main()






