__module_name__ = "rhythmbox"
__module_version__ = "1.2"
__module_description__ = "Plugin for Rhythymbox integration"

import hexchat
import subprocess


def np(word, word_eol, userdata):
    output = subprocess.check_output([
        'rhythmbox-client',
        '--print-playing-format' if hexchat.get_pluginpref('np_format') else '--print-playing',
	hexchat.get_pluginpref('np_format') if hexchat.get_pluginpref('np_format') else ''
    ])
    output = output.strip()  # Has a trailing newline
    hexchat.command('me {0} "{1}"'.format(hexchat.get_pluginpref('np_message') if hexchat.get_pluginpref('np_message') else 'is listening to', output) )
    return hexchat.EAT_ALL

def np_set_format(word, word_eol, userdata):
    if len(word_eol) == 1:
        if hexchat.del_pluginpref('np_format'):
            hexchat.prnt('Deleted the format')
        else:
            hexchat.prnt('Failed to delete')
        return hexchat.EAT_ALL

    if hexchat.set_pluginpref('np_format', word_eol[1]):
        hexchat.prnt('Success')
    else:
        hexchat.prnt('Failed')
    return hexchat.EAT_ALL

def np_set_message(word, word_eol, userdata):
    if len(word_eol) == 1:
        if hexchat.del_pluginpref('np_message'):
            hexchat.prnt('Deleted the message')
        else:
            hexchat.prnt('Failed to delete')
        return hexchat.EAT_ALL

    if hexchat.set_pluginpref('np_message', word_eol[1]):
        hexchat.prnt('Success')
    else:
        hexchat.prnt('Failed')
    return hexchat.EAT_ALL

hexchat.hook_command('np', np)
hexchat.hook_command('np_set_format', np_set_format)
hexchat.hook_command('np_set_message', np_set_message)
