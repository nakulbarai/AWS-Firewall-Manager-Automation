import boto3
import time
import cfnresponse
import json
import os

def get_mandatory_evar(evar_name):
    if not evar_name in os.environ:
        raise RuntimeError("Missing environment variable: {}".format(evar_name))
    return os.environ[evar_name]

def lambda_handler(event, context):

    client = boto3.client('waf-regional')
    token = client.get_change_token()
    print token
    Ruleid1 = get_mandatory_evar("Rule1")
    Ruleid2 = get_mandatory_evar("Rule2")
    Ruleid3 = get_mandatory_evar("Rule3")
    Ruleid4 = get_mandatory_evar("Rule4")
    Ruleid5 = get_mandatory_evar("Rule5")
    Ruleid6 = get_mandatory_evar("Rule6")
    Ruleid7 = get_mandatory_evar("Rule7")
    Ruleid8 = get_mandatory_evar("Rule8")
    Ruleid9 = get_mandatory_evar("Rule9")
    Ruleid10 = get_mandatory_evar("Rule10")
    rulegroup = client.create_rule_group(
                    Name='pac-rulegroup-test1',
                    MetricName='cdn',
                    ChangeToken= token['ChangeToken']
                )
    print rulegroup
    time.sleep(10)
    updatetoken = client.get_change_token()
    updateRuleGrp = client.update_rule_group(
                        RuleGroupId= rulegroup['RuleGroup']['RuleGroupId'],
                        Updates=[
                                    {
                                        'Action': 'INSERT',
                                        'ActivatedRule': {
                                            'Priority': 10,
                                            'RuleId': Ruleid1,
                                            'Action': {
                                                'Type': 'BLOCK'
                                            },
                                            'OverrideAction': {
                                                'Type': 'COUNT'
                                            },
                                            'Type': 'REGULAR'
                                        }
                                    },
                                    {
                                        'Action': 'INSERT',
                                        'ActivatedRule': {
                                            'Priority': 20,
                                            'RuleId': Ruleid2,
                                            'Action': {
                                                'Type': 'BLOCK'
                                            },
                                            'OverrideAction': {
                                                'Type': 'COUNT'
                                            },
                                            'Type': 'REGULAR'
                                        }
                                    },
                                    {
                                        'Action': 'INSERT',
                                        'ActivatedRule': {
                                            'Priority': 30,
                                            'RuleId': Ruleid3,
                                            'Action': {
                                                'Type': 'BLOCK'
                                            },
                                            'OverrideAction': {
                                                'Type': 'COUNT'
                                            },
                                            'Type': 'REGULAR'
                                        }
                                    },
                                    {
                                        'Action': 'INSERT',
                                        'ActivatedRule': {
                                            'Priority': 40,
                                            'RuleId': Ruleid4,
                                            'Action': {
                                                'Type': 'BLOCK'
                                            },
                                            'OverrideAction': {
                                                'Type': 'COUNT'
                                            },
                                            'Type': 'REGULAR'
                                        }
                                    },
                                    {
                                        'Action': 'INSERT',
                                        'ActivatedRule': {
                                            'Priority': 50,
                                            'RuleId': Ruleid5,
                                            'Action': {
                                                'Type': 'BLOCK'
                                            },
                                            'OverrideAction': {
                                                'Type': 'COUNT'
                                            },
                                            'Type': 'REGULAR'
                                        }
                                    },
                                    {
                                        'Action': 'INSERT',
                                        'ActivatedRule': {
                                            'Priority': 60,
                                            'RuleId': Ruleid6,
                                            'Action': {
                                                'Type': 'BLOCK'
                                            },
                                            'OverrideAction': {
                                                'Type': 'COUNT'
                                            },
                                            'Type': 'REGULAR'
                                        }
                                    },
                                    {
                                        'Action': 'INSERT',
                                        'ActivatedRule': {
                                            'Priority': 70,
                                            'RuleId': Ruleid7,
                                            'Action': {
                                                'Type': 'BLOCK'
                                            },
                                            'OverrideAction': {
                                                'Type': 'COUNT'
                                            },
                                            'Type': 'REGULAR'
                                        }
                                    },
                                    {
                                        'Action': 'INSERT',
                                        'ActivatedRule': {
                                            'Priority': 80,
                                            'RuleId': Ruleid8,
                                            'Action': {
                                                'Type': 'BLOCK'
                                            },
                                            'OverrideAction': {
                                                'Type': 'COUNT'
                                            },
                                            'Type': 'REGULAR'
                                        }
                                    },
                                    {
                                        'Action': 'INSERT',
                                        'ActivatedRule': {
                                            'Priority': 90,
                                            'RuleId': Ruleid9,
                                            'Action': {
                                                'Type': 'BLOCK'
                                            },
                                            'OverrideAction': {
                                                'Type': 'COUNT'
                                            },
                                            'Type': 'REGULAR'
                                        }
                                    },
                                    {
                                        'Action': 'INSERT',
                                        'ActivatedRule': {
                                            'Priority': 100,
                                            'RuleId': Ruleid10,
                                            'Action': {
                                                'Type': 'BLOCK'
                                            },
                                            'OverrideAction': {
                                                'Type': 'COUNT'
                                            },
                                            'Type': 'REGULAR'
                                        }
                                    },
                                ],
                        ChangeToken= updatetoken['ChangeToken']
                    )
    ruleGrpId = {'ruleGrpId': rulegroup['RuleGroup']['RuleGroupId']}
    physicalResourceId = 'FWM-RULE-GRP-ID-' + context.log_stream_name
    cfnresponse.send(event, context, cfnresponse.SUCCESS, ruleGrpId, physicalResourceId=physicalResourceId)
    return updateRuleGrp
