import json 
import click
import yaml as yml
from genyml import genyml 

catalog_data = genyml.open_read_file("target/catalog.json","json")
manifest_data = genyml.open_read_file("target/manifest.json","json")
dbtproject = genyml.open_read_file("dbt_project.yml","yaml")


@click.command()
@click.option('--select', required=False, type=str)
def dbdoc_gen(select):
    
    # with open(r"target/catalog.json") as catalog_file:
    #     catalog_data = json.load(catalog_file)

    # with open(r"target/manifest.json") as manifest_file:
    #     manifest_data = json.load(manifest_file)
        
    # with open(r"dbt_project.yml") as project_file:
    #     dbtproject = yml.safe_load(project_file)

    # if type(select) != type(None):
    #     if '\\' in manifest_data['nodes'][list(manifest_data['nodes'].keys())[0]]['original_file_path']:
    #         select = select.replace('/','\\')
    #     else:
    #         select = select.replace('\\','/')
    # else:
    #     pass

    genyml.logger_snytax_change(manifest_data=manifest_data)

    tables = {}
    dbdiagram_string = ""
    keys_dict = {}

    for node,data in manifest_data['nodes'].items():
        if 'unrendered_config' in data.keys():
            for keys, value in data['unrendered_config'].items():
                node = node.split('.')[-1]
                if 'unique_key' in keys:
                    keys_dict[node] = value.strip()

    for model, data in catalog_data['nodes'].items():
        if ('fct' in model or 'dim' in model) and dbtproject['name'] == model.split('.')[1]:
                columns_datatypes = {}
                for col_name, col_metadata in data['columns'].items():
                    columns_datatypes[col_name] = col_metadata['type']
                tables[model] = columns_datatypes

    with open("dbdiagram_string.txt", "w") as f:

        for table, cols in tables.items():
            if dbtproject['name'] == table.split('.')[1]:
                dbdiagram_string = dbdiagram_string + "Table " + f'"{table}"' + " {\n"
                for col, dtype in cols.items():
                    if col.lower() in keys_dict.values() and col.lower().split('_')[-1] == 'skey':
                        dbdiagram_string = dbdiagram_string + f'"{col.lower()}"' + " " + f'"{dtype.lower()}"' + " " + "[pk]" "\n"
                    else:
                        dbdiagram_string = dbdiagram_string + f'"{col.lower()}"' + " " + f'"{dtype.lower()}"' + "\n"
            dbdiagram_string = dbdiagram_string + "}\n"

        print(dbdiagram_string, file=f)

        duplicates = []
        for from_table, from_cols in tables.items():
            for from_col in from_cols.keys():
                for to_table, to_cols in tables.items():
                    if from_table != to_table:
                        for to_col in to_cols.keys():
                            if to_col == from_col and (('id' in to_col.lower() or 'id' in from_col.lower()) or ('skey' in to_col.lower() or 'skey' in from_col.lower())):
                                if ''.join([from_table,from_col,to_table,to_col]) not in duplicates:
                                    print(f"Ref: "f'"{from_table.lower()}"'"."f'"{from_col.lower()}"' " - " f'"{to_table.lower()}"'"."f'"{to_col.lower()}"', file=f)
                                    duplicates.extend([''.join([from_table,from_col,to_table,to_col]),''.join([to_table,to_col,from_table,from_col])])

    f.close()
    
if __name__ == '__main__':
    dbdoc_gen()