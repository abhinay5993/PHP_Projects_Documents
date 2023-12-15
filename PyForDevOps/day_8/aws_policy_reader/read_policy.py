import json
policy_obj = open("policy.json",'r')
policy = policy_obj.read()
policy_obj.close()


def reject_policy(policy_dict):
    policy_dict = json.loads(policy)
    policy_dict["Statement"][0]["Effect"] = "Reject"
    new_policy = json.dumps(policy_dict)

    new_policy_obj = open("policy_new.json",'w')
    new_policy_obj.write(new_policy)
    new_policy_obj.close()