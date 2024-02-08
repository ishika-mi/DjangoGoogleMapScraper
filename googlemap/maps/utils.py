import os


def clear_logs():
        log_file_path = 'maps/info.log'
        if os.path.exists(log_file_path):
            with open(log_file_path, 'w') as log_file:
                log_file.truncate(0)