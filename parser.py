


#parse owl script
def parse_payload():
    with open("payload.owl") as f:
        data = f.read()
        instruction_list = data.splitlines(data)
        
    print(data)
    print(instruction_list)
    returns = []
    for i in instruction_list:
        try:
            cmd,parm = i.split(" ")
            returns.append({"cmd":cmd,"parm":parm})
        except:
            returns.append({"cmd":i,"parm":""})

    return returns 


if __name__ =="__main__":
    returns = parse_payload()
    print(returns)




