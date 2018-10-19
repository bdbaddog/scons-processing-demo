# Sample tool
import SCons.Builder


def _example_emitter(target, source, env):
    print("In Tool example _example_emitter() [Environment:%s]"%env.get('ENV_NAME','Unknown'))
    return target, source

def _example_scanner(node, env, path):
    print("In Tool example _example_scanner(%s, env, %s) [Environment:%s]"%(
        str(node), path, env.get('ENV_NAME','Unknown')))

    return []

example_scanner = SCons.Scanner.Scanner(
    function = _example_scanner,
    skeys = ['.exin']
)

_example_builder = SCons.Builder.Builder(
    action = 'echo example $SOURCES $TARGETS',
    suffix = '.example',
    src_suffix = '.exin',
    emitter = _example_emitter,
)

def generate(env):
    print("In Tool example generate() [Environment:%s]"%env.get('ENV_NAME','Unknown'))
    
    env['BUILDERS']['Example'] = _example_builder

    env.Append(SCANNERS = example_scanner)

def exists(env):
    print("In Tool example exists() [Environment:%s]"%env.get('ENV_NAME','Unknown'))
    return True