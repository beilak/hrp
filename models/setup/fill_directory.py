from models.directory.acc_type import AccType
from models.db.db_conn import DBConn
import yaml


def fill_acc_type():
    acc_types = set()
    with open('setup_data.yaml') as f:
        for line in yaml.safe_load(f)["acc_types"]:
            for type_key in line:
                acc_types.add(AccType(acc_type_id=type_key, name=line[type_key]["name"]))
    DBConn.insert(acc_types)


# Fill Account type tables
fill_acc_type()
