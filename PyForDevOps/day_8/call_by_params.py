def check_environment(list_of_env,test_env):
    output = []
    for env in list_of_env:
        if env.lower() == "aws":
            output.append("you are in AWS")
        elif env.lower() == "azure":
            output.append("you are in Azure")
        else:
            output.append("You are in other env")
    
    return output


