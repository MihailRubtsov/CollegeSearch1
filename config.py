import os

from database_manager.manager import Manager

db_manager = Manager(os.path.join(os.getcwd(), 'Instituti.db'))
