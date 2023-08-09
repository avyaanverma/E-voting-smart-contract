candidateSys = {"modi":0, "mamta": 0, "rahul": 0 }
def setVote(candidateNo):
    match candidateNo:
        case 1:
            m = candidateSys.get("modi")
            m += 1
            candidateSys["modi"] = m
        case 2:
            m = candidateSys.get("mamta")
            m += 1
            candidateSys["mamta"] = m
        case 3:
            m = candidateSys.get("rahul")
            m += 1
            candidateSys["rahul"] = m
        case default:
            print(" Please choose correct symbols")


# use json file
print("Candidates available in voting: ")
print("1.modi 2.mamta 3.rahul")

while(True):
    # try:
    no = int(input("press indivdual to vote : "))
    print(type(no))
    break
    # except TypeError:
    #     continue
setVote(no)

print(f'1.modi : {candidateSys["modi"]} 2.mamta: {candidateSys["mamta"]}  3.rahul: {candidateSys["rahul"]}')






