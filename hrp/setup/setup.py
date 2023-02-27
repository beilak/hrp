import setup_db
import fill_directory
import logging


def main():
    try:
        # SetUp DB
        setup_db.drop_all_tables()
        setup_db.create_all_tables()
        # Fill data
        fill_directory.fill_data()
    except Exception as error:
        log = logging.getLogger()
        log.info(str(error))


if __name__ == "__main__":
    main()
