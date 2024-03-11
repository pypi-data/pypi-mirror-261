import os
import shutil
import pandas as pd
import mysql.connector


def configure_dataset_directory(csv_files, folder_path, dataset_dir):
    if not os.path.exists(dataset_dir):
        try:
            os.makedirs(dataset_dir)
        except Exception as e:
            print(f"Error creating dataset directory: {e}")
            return False

    for csv in csv_files:
        src_file = os.path.join(folder_path, csv)  # Adjusted source file path
        dst_file = os.path.join(dataset_dir, csv)
        try:
            shutil.copy(src_file, dst_file)
            print(f"Copied {csv} to datasets folder")
        except Exception as e:
            print(f"Error copying {csv}: {e}")
            return False

    return True


def create_df(dataset_dir, csv_files):
    data_path = os.path.join(os.getcwd(), dataset_dir)
    df = {}
    for file in csv_files:
        try:
            file_path = os.path.join(data_path, file)
            df[file] = pd.read_csv(file_path)
        except UnicodeDecodeError:
            file_path = os.path.join(data_path, file)
            df[file] = pd.read_csv(file_path, encoding="ISO-8859-1")
        print(file)
    return df

def clean_tbl_name(filename):
    clean_tbl_name = filename.lower().replace(" ", "").replace("-", "_").replace(r"/", "_").replace("\\", "_").replace("$", "").replace("%", "")
    tbl_name = '{0}'.format(clean_tbl_name.split('.')[0])
    return tbl_name

def clean_colname(dataframe):
    dataframe.columns = [x.lower().replace(" ", "_").replace("-", "_").replace(r"/", "_").replace("\\", "_").replace(".", "_").replace("$", "").replace("%", "") for x in dataframe.columns]
    dataframe.columns = [x if x != 'rank' else 'rank_column' for x in dataframe.columns]
    replacements = {
        'timedelta64[ns]': 'varchar(255)',
        'object': 'varchar(255)',
        'float64': 'float',
        'int64': 'int',
        'datetime64': 'datetime'
    }
    col_str = ", ".join("`{}` {}".format(n, d) for (n, d) in zip(dataframe.columns, dataframe.dtypes.replace(replacements)))
    return col_str, dataframe.columns

def create_table(host, dbname, user, password, tbl_name, col_str):
    try:
        conn = mysql.connector.connect(host=host, user=user, password=password, database=dbname)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS {} ({});".format(tbl_name, col_str))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except mysql.connector.Error as e:
        print("MySQL Error:", e.msg)
        return False

def drop_table(host, dbname, user, password, tbl_name):
    try:
        conn = mysql.connector.connect(host=host, user=user, password=password, database=dbname)
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS {};".format(tbl_name))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except mysql.connector.Error as e:
        print("MySQL Error:", e.msg)
        return False

def insert_into_table(host, dbname, user, password, tbl_name, dataframe):
    try:
        conn = mysql.connector.connect(host=host, user=user, password=password, database=dbname)
        cursor = conn.cursor()
        dataframe = dataframe.where(pd.notnull(dataframe), -1)
        values = dataframe.values.tolist()
        placeholders = ', '.join(['%s'] * len(dataframe.columns))
        columns_str = ', '.join(['`{}`'.format(col) for col in dataframe.columns])
        insert_query = "INSERT INTO {} ({}) VALUES ({});".format(tbl_name, columns_str, placeholders.replace('?', '%s'))
        cursor.executemany(insert_query, values)
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except mysql.connector.Error as e:
        print("MySQL Error:", e.msg)
        return False

        
def import_csv_to_mysql(folder_path, host, dbname, user, password, create_fresh=False):
    csv_files = [file for file in os.listdir(folder_path) if file.endswith(".csv")]

    if not csv_files:
        print("No CSV files found in the selected folder.")
        return False

    dataset_dir = os.path.join(os.getcwd(), 'datasets')
    if not configure_dataset_directory(csv_files, folder_path, dataset_dir):  # Pass folder_path
        print("Error configuring dataset directory.")
        return False


    df = create_df(dataset_dir, csv_files)

    for k, v in df.items():
        tbl_name = clean_tbl_name(k)
        col_str, _ = clean_colname(v)

        if create_fresh:
            drop_table_status = drop_table(host, dbname, user, password, tbl_name)
            if not drop_table_status:
                print(f"Error dropping table {tbl_name}.")
                return False

            create_table_status = create_table(host, dbname, user, password, tbl_name, col_str)
            if not create_table_status:
                print(f"Error creating table {tbl_name}.")
                return False

            insert_into_table_status = insert_into_table(host, dbname, user, password, tbl_name, v)
            if not insert_into_table_status:
                print(f"Error inserting into table {tbl_name}.")
                return False
        else:
            create_table_status = create_table(host, dbname, user, password, tbl_name, col_str)
            if not create_table_status:
                print(f"Error creating table {tbl_name}.")
                return False

            insert_into_table_status = insert_into_table(host, dbname, user, password, tbl_name, v)
            if not insert_into_table_status:
                print(f"Error inserting into table {tbl_name}.")
                return False

    return True
