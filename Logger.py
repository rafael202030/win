from time import strftime, gmtime
import os

class Logger(object):

    LOGGER_START = '--START--'
    LOGGER_ERROR = '--ERROR--'
    LOGGER_WARNING = '--WARNING--'
    LOGGER_INFO = '--INFO--'
    LOGGER_FAILURE = '--FAILURE--'
    LOGGER_SUCCESS = '--SUCCESS--'
    LOGGER_END = '--END--'

    def add_log_message(self, message_text, log_file_path, log_type):
        with open(log_file_path, 'ab') as f:
            if os.path.exists(log_file_path):
                f.writelines(self.create_message_text(message_text, log_type))
                f.close()
            else:
                print 'Log file path is not valid: ' + str(log_file_path)


    def create_message_text(self, message_string, log_type):
        message_text = '[' + str(strftime("%Y-%m-%d %H:%M:%S", gmtime())) + ']:['+ str(log_type).upper() +']:   ' + message_string + os.linesep
        return message_text

    def clear_log_file(self, log_file):
        with open(log_file, 'wb'):
            pass

    def check_if_log_file_is_not_empty(self, log_file):
        if os.path.exists(log_file) and os.path.getsize(log_file) > 0:
            return True
        else:
            return False