import sys
from console_interface import start_message
import database_main
import logging

logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="a",
                    format="%(asctime)s %(levelname)s %(message)s")


def main(database_action_info: dict):
    database = database_main.Database()

    if database_action_info['action'] == 'import':
        try:
            database.import_data(database_action_info['rooms_path'], 'rooms')
            database.import_data(database_action_info['students_path'], 'students')
            logging.info('Import is successful')
        # принято указывать тип ошибки, либо просто отталкивайся от дефолтного питонячего класса 
        except:
            logging.error('Import error')
            sys.exit(1)

    elif database_action_info['action'] == 'export':
        try:
            database.export_data(database_action_info['export_path'], database_action_info['export_type'])
            logging.info('Export is successful')
        # принято указывать тип ошибки, либо просто отталкивайся от дефолтного питонячего класса 
        except:
            logging.error('Export failed')
            sys.exit(1)
    logging.info('Finished')
    sys.exit(0)


if __name__ == '__main__':
    logging.info('Started')
    #в логгерах принято использовать лейзи форматтинг
    logging.info('Input arguments: ' + ', '.join(sys.argv[1:]))
    database_action_info = start_message()
    logging.info('Settings: ' + str(database_action_info))
    main(database_action_info)
