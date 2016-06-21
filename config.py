import os


ftp_site = os.environ.get('FTP_SITE', 'wp1.kiwix.org')
ftp_user = os.environ.get('FTP_USER', 'ftp')
ftp_pass = os.environ.get('FTP_PASS')  # going to need to get one of these

which_wiki = os.environ.get('WHICH_WIKI', 'enwiki_2016-06')

acceptable_epsilon = os.environ.get('EPSILON', 20)  # allowed slippage between pages and all

max_num_candidate_sets = int(os.environ.get('MAX_NUM_SETS', 2))

testing = bool(os.environ.get('TESTING', True))

if testing:
    target_size = 1000000
else:
    target_size = int(os.environ.get('SIZE', 100000))  # in bytes
