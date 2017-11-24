#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime


class Configuration(object):

    LINKS_ARRAY = ['http://www.emsbrno.cz/p.axd/cs/%C5%BDab%C4%8Dice.PPS.MZLUUAB.html',
                   'http://www.emsbrno.cz/p.axd/cs/Vigantice.MZLUUAB.html',
                   'http://www.emsbrno.cz/p.axd/cs/Marchegg.MZLUUAB.html',
                   'http://www.emsbrno.cz/p.axd/cs/Kameni%C4%8Dky.MZLUUAB.html',
                   'http://www.emsbrno.cz/p.axd/cs/Jev%C3%AD%C4%8Dko.MZLUUAB.html',
                   'http://www.emsbrno.cz/p.axd/cs/Edelhof.MZLUUAB.html',
                   'http://www.emsbrno.cz/p.axd/cs/Doksany.MZLUUAB.html',
                   'http://www.emsbrno.cz/p.axd/cs/Byst%C5%99ice.n_u_.P._t_.doln%C3%AD.topoly.MZLUUAB.html',
                   'http://www.emsbrno.cz/p.axd/cs/Byst%C5%99ice.n_u_.P_u_._t_.horn%C3%AD.topoly.MZLUUAB.html',
                   'http://www.emsbrno.cz/p.axd/cs/Byst%C5%99ice.n_u_.P_u_._t_.horn%C3%AD.tr%C3%A1vn%C3%ADk.MZLUUAB.html',
                   'http://www.emsbrno.cz/p.axd/cs/Sumperalm.MZLUUAB.html'
        ]

    USER_NAME = ''
    PASSWORD = ''

    EXPORT_DIR = ''


class MinerConfiguration (object):

    START_DATE = '2016-11-28'
    END_DATE = '2016-11-21'
    RUN_DATE = str( datetime.datetime.now().strftime("%Y-%m-%d-%H-%M"))
    COUNT_OF_DAYS_IN_ONE_STEP = 8

    FTP_HOST = ''
    FTP_LOGIN = ''
    FTP_PSWD = ''
    FTP_DIR_PATH = ''
    FTP_FILE_EXTENSION = '.mnd'

    CZECH_GLOBE_FTP_ADDRESS = ''
    CZECH_GLOBE_FTP_PORT = 21
    CZECH_GLOBE_FTP_USER = ''
    CZECH_GLOBE_FTP_PASSWORD = ''
    CZECH_GLOBE_FTP_DIRS = ['/Scinti_Polk', '/Scinti_Doman']
    CZECH_GLOBE_FTP_DIRS_FILE_EXTENSION = '.csv'

    LOG_FILE_PATH = ''
    LOGGER_START = '--START--'
    LOGGER_ERROR = '--ERROR--'
    LOGGER_WARNING = '--WARNING--'
    LOGGER_INFO = '--INFO--'
    LOGGER_FAILURE = '--FAILURE--'
    LOGGER_SUCCESS = '--SUCCESS--'
    LOGGER_END = '--END--'

    LOCAL_DIR = ''
    CONNECTED_FILES_EXTENSION = '.csv'
    WEEK_FILE = str(START_DATE) + '_' + str(END_DATE) + '.csv'
    WEEK_SUMMARY = str(START_DATE) + '_' + str(END_DATE) + '_week_sum.csv'

    DATA_LINES_POINTER = 'PT'
    CSV_DELIMITER = ';'
    NO_DATA_VALUE = -9999
    INDEXES_OF_NEEDED_DATA = [0, 1, 2, 3, 7, 10, 13, 16, 19, 22, 26, 27, 28, 43, 47, 51, 55, 59, 63, 67, 71, 75, 112]
    HEADERS = ['Time',
               'Structure Function Constant of Refractive Index Fluctuations at Instrument Wavelength',
               'Structure Function Constant of Temperature Fluctuations',
               'Heat Flux',
               'Monin-Obukhov Length',
               'Friction Velocity ',
               'Turbulent Temperature Scale',
               'Momentum Flux',
               'Inner Scale Length ',
               'Dissipation Rate of Turbulent Kinetic Energy',
               'Latent Heat Flux',
               'Water Evapotranspiration',
               'Albedo',
               'WSP Pressure',
               'WSP Temperatur',
               'WSP Relative Humidity A',
               'WSP Relative Humidity B',
               'WSP Relative Humidity C',
               'WSP Temperature Upper',
               'WSP Temperature Lower',
               'WSP Net Radiation',
               'WSP Global Radiation',
               'WSP Reflected Global Radiation',
               'WSP Soil Heat Flux A',
               'WSP Soil Heat Flux B',
               'Error Code']

    DGN_COUNT_OF_DAYS_IN_ONE_STEP = 30
    DGN_FTP_FILE_EXTENSION = '.dgn'
    DGN_LOG_FILE_PATH = ''
    DGN_LOCAL_DIR = ''
    INDEXES_OF_NEEDED_DGN_DATA = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 99, 100, 101, 102, 103]
    DGN_HEADERS = ['Time',
                   'Average XA (Corrected)',
                   'Average YA (Corrected)',
                   'Normalized Std.Dev. XA (Corrected)',
                   'Normalized Std.Dev. YA (Corrected)',
                   'Correlation XA/YA (Corrected)',
                   'Number of Samples',
                   'Average XA',
                   'Average YA',
                   'Average XB',
                   'Average YB',
                   'Std.Dev. XA',
                   'Std.Dev. YA',
                   'Std.Dev. XB',
                   'Std.Dev. YB',
                   'Minimum XA',
                   'Minimum YA',
                   'Minimum XB',
                   'Minimum YB',
                   'Maximum XA',
                   'Maximum YA',
                   'Maximum XB',
                   'Maximum YB',
                   'Correlation XA/YA',
                   'Correlation XB/YB',
                   'Correlation XA/XB',
                   'Correlation YA/YB',
                   'Correlation XA/YB',
                   'Correlation YA/XB',
                   'Channel Flags XA',
                   'Channel Flags YA',
                   'Channel Flags XB',
                   'Channel Flags YB',
                   'Error code']

