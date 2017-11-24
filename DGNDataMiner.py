from SenzorDataDownloader import Data_manager as DM, CSV_Manger as CM, FTP_client as FTPC
from Config import Configuration, MinerConfiguration
from Logger import Logger

from datetime import datetime
import re
import os

class Initializer(object):

    def check_input(self, date_string):
        datetime.strptime(str(date_string), '%Y-%m-%d')

    def process(self, start_date, end_date):

        config_instance = MinerConfiguration()
        logger_instance = Logger()
        data_manager_instance = DM()
        ftp_client_instance = FTPC()
        csv_manager_instance = CM(config_instance, logger_instance, data_manager_instance)

        logger_instance.clear_log_file(config_instance.DGN_LOG_FILE_PATH)
        logger_instance.add_log_message("Data processing started", config_instance.DGN_LOG_FILE_PATH, config_instance.LOGGER_START)
        connection = ftp_client_instance.connect_to_ftp(config_instance.FTP_HOST, config_instance.FTP_LOGIN, config_instance.FTP_PSWD)
        start_date_object = data_manager_instance.convert_string_date_to_date_object(start_date)
        end_date_object = data_manager_instance.convert_string_date_to_date_object(end_date)
        dates = data_manager_instance.get_dates_set(start_date_object, end_date_object)
        dates_batches_list = data_manager_instance.cut_dates_set_by_index(dates, config_instance.DGN_COUNT_OF_DAYS_IN_ONE_STEP)

        data_manager_instance.create_dir_with_date_stamp(config_instance.RUN_DATE, config_instance.DGN_LOCAL_DIR)
        download_dir = os.path.join(config_instance.DGN_LOCAL_DIR, config_instance.RUN_DATE)

        for week_dates_list in dates_batches_list:
            file_names = data_manager_instance.get_file_names_from_dates(week_dates_list, config_instance.DGN_FTP_FILE_EXTENSION)
            data_manager_instance.create_dir_with_date_stamp(week_dates_list[0], download_dir)
            week_download_dir = os.path.join(download_dir, week_dates_list[0])

            for file in file_names:
                logger_instance.add_log_message("Processing file: " + str(file), config_instance.DGN_LOG_FILE_PATH, config_instance.LOGGER_INFO)
                csv_file_path = os.path.join(week_download_dir, file[:-4] + '.csv')

                logger_instance.add_log_message("Downloading data from FTP", config_instance.DGN_LOG_FILE_PATH, config_instance.LOGGER_INFO)
                ftp_client_instance.download_data_from_ftp(connection, config_instance.FTP_DIR_PATH, week_download_dir, file)

                logger_instance.add_log_message("Clearing data", config_instance.DGN_LOG_FILE_PATH, config_instance.LOGGER_INFO)
                file_content = data_manager_instance.read_file_lines(os.path.join(week_download_dir, file))
                string_lines = re.split(r'\n', file_content)
                pure_data_lines = csv_manager_instance.get_pure_data_lines_from_csv(string_lines, config_instance.DATA_LINES_POINTER, config_instance.INDEXES_OF_NEEDED_DGN_DATA)
                lines_with_correct_date_time_stamp = data_manager_instance.adjust_date_time_stamp_in_lines(pure_data_lines, '/', 'T', ' ')

                logger_instance.add_log_message("Converting file: " + str(file) + " to CSV format", config_instance.DGN_LOG_FILE_PATH, config_instance.LOGGER_INFO)
                csv_manager_instance.write_data_to_csv(csv_file_path, lines_with_correct_date_time_stamp, config_instance.CSV_DELIMITER)

            logger_instance.add_log_message("Connecting week CSV files", config_instance.LOG_FILE_PATH, config_instance.LOGGER_INFO)
            csv_files = data_manager_instance.list_files_with_given_extension(week_download_dir, config_instance.CONNECTED_FILES_EXTENSION)
            this_week_csv_file_name = data_manager_instance.create_file_name_from_dates(week_dates_list[0], week_dates_list[-1], '',config_instance.CONNECTED_FILES_EXTENSION)
            this_week_csv_summary_file_name = data_manager_instance.create_file_name_from_dates(week_dates_list[0], week_dates_list[-1], '_period_summary',config_instance.CONNECTED_FILES_EXTENSION)
            csv_manager_instance.connect_text_files_from_list_to_one(week_download_dir, csv_files, this_week_csv_file_name)
            csv_manager_instance.split_csv_line_data_and_clear_lines(this_week_csv_file_name, this_week_csv_summary_file_name, config_instance.DGN_HEADERS, str(config_instance.CSV_DELIMITER), ',')
            logger_instance.add_log_message("Files processing finalized", config_instance.LOG_FILE_PATH, config_instance.LOGGER_INFO)

            ftp_client_instance.disconnect_from_ftp(connection)
            logger_instance.add_log_message("Data processing end", config_instance.LOG_FILE_PATH, config_instance.LOGGER_END)

if __name__ == '__main__':

    while True:
        end_date = raw_input('Start of download (date as YYYY-MM-DD): ')
        start_date = raw_input('End of download - in the past(date as YYYY-MM-DD): ')
        try:
            Initializer().check_input(start_date)
            Initializer().check_input(end_date)
        except ValueError:
            print 'Bad date time format for one of given dates, please check spelling and repeat input'
            continue
        else:
            print 'Running processing for dates from: ' + str(start_date) + ' to: ' + str(end_date) + '! Process description can be found at given logger file'
            Initializer().process(start_date, end_date)
            print 'Process finalized'
            exit()