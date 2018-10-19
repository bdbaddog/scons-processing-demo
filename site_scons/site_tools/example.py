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



def _example2_scanner(node, env, path):
    print("In Tool example _example2_scanner(%s, env, %s) [Environment:%s]"%(
        str(node), path, env.get('ENV_NAME','Unknown')))

    return []

example2_scanner = SCons.Scanner.Scanner(
    function = _example2_scanner,
    skeys = ['.example']
)

def _example2_emitter(target, source, env):
    print("In Tool example _example2_emitter() [Environment:%s]"%env.get('ENV_NAME','Unknown'))
    return target, source


_example_2_builder = SCons.Builder.Builder(
    action = 'echo example2 $SOURCES $TARGETS',
    suffix = '.example2',
    src_suffix = '.example',
    emitter = _example2_emitter,
)

def generate(env):
    print("In Tool example generate() [Environment:%s]"%env.get('ENV_NAME','Unknown'))
    
    env['BUILDERS']['Example'] = _example_builder
    env['BUILDERS']['Example2'] = _example_2_builder

    env.Append(SCANNERS = [example_scanner, example2_scanner])

def exists(env):
    print("In Tool example exists() [Environment:%s]"%env.get('ENV_NAME','Unknown'))
    return True