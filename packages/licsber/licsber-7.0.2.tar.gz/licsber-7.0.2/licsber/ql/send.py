import os.path

import notify


def send(file_magic: str, log_list: list, ignore: bool = False) -> None:
    filepath, filename = os.path.split(file_magic)

    log_list.insert(0, f"Root Path: {filepath}")

    title = filename.split('.')[0]
    if ignore:
        log_text = '\n'.join(log_list)
        print('ignore:', title, log_text, sep='\n')
        return

    log_text = '\n\n'.join(log_list)
    notify.push_config['CONSOLE'] = False
    notify.send(title, log_text)
