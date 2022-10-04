from models.directory.db_acc_type import AccType
from models.directory.db_measure import Measure


from hrp.db.db_conn import DBConn
import yaml


def fill_acc_types(lines):
    acc_types = set()
    for line in lines:
        for type_key in line:
            acc_types.add(AccType(acc_type_id=type_key, name=line[type_key]["name"]))
    return acc_types


def fill_measures(lines):
    measures = set()
    for line in lines:
        for type_key in line:
            measures.add(Measure(measure_id=type_key, name=line[type_key]["name"]))
    return measures


def fill_data():
    with open('setup_directory_data.yaml') as f:
        yaml_data = yaml.safe_load(f)
        acc_types = fill_acc_types(yaml_data['acc_types'])
        measures = fill_measures(yaml_data['measures'])

        if len(acc_types) > 0:
            try:
                DBConn.insert(acc_types)
            except Exception as error:
                print(str(error))
        if len(measures) > 0:
            try:
                DBConn.insert(measures)
            except Exception as error:
                print(str(error))


if __name__ == "__main__":
    # Fill Account type tables
    fill_data()
