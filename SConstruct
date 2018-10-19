print("Start of SConstruct")

DefaultEnvironment(tools=['example'], ENV_NAME='default')

env = Environment(tools=['example'], ENV_NAME='first one')
cloned = env.Clone(ENV_NAME='cloned')

SConscript('src/SConscript', exports=['env','cloned'])

print("End of SConstruct")
