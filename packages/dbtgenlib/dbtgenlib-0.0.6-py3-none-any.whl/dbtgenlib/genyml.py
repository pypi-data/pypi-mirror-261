import click
import json
import os
import yaml as yml
import logging


@click.command()
@click.option('--select', required=False, type=str)


def file_exists(file_path):
    return os.path.exists(file_path)

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def read_yaml_file(file_path):
    with open(file_path, 'r') as file:
        return yml.safe_load(file)

def open_read_file(file_path):

    if not file_exists(file_path):
        print(f"{file_path} does not exist, please regenerate the dbt docs for the correct files or check where your files exist again")
        return None 
    else:
        suffix = os.path.basename(file_path).split('.')[-1]
        if suffix == 'json':
            return read_json_file(file_path)
        elif suffix == 'yml':
            return read_yaml_file(file_path)
        else:
            print(f"Please check {file_path}, '{suffix}' is not the right file we need to process this data ")
            return None 


def logger_snytax_change(select,manifest_data):
    if type(select) != type(None):
        if '\\' in manifest_data['nodes'][list(manifest_data['nodes'].keys())[0]]['original_file_path']:
            select = select.replace('/','\\')
        else:
            select = select.replace('\\','/')
    else:
        pass


def dbtdocgen(select, manifest_data, dbtproject):
    
    keys_list = []
    names_set = set()

    for node, data in manifest_data['nodes'].items():
        if 'unique_key' in data['unrendered_config']:
            names = str(data['fqn'][-2])
            names_set.add(names)

    distinct_names = list(names_set)

    for name in distinct_names:
        yaml = '\nversion: 2\n\nmodels:\n\n'

        for node, data in sorted(list(manifest_data['nodes'].items()), key=lambda x: x[1]['fqn'][-1]):
            if name in data['fqn'][-2]:
                if 'unique_key' in data['unrendered_config'] and len(data['fqn']) != 0 and dbtproject['name'] == data['fqn'][0]:
                    yaml += f"- name: {data['fqn'][-1]}\n"
                    yaml += "  description: This is a table in staging\n"
                    yaml += "  columns:\n"
                    yaml += f"   - name: {data['unrendered_config']['unique_key']}\n"
                    yaml += "     description: This is a surrogate key\n"
                    # yaml += "     tests:\n"
                    # yaml += f"      - not_null\n"
                    # yaml += f"      - unique\n"
                    yaml += f"      \n"
                    file_name = f"_{name}_doc.yml"  # Use the name as the file name
                    file_path = os.path.join("\\".join(data['original_file_path'].split('\\')[:-1]), file_name)  
                    # Specify the output folder path

                else:
                    continue
            
                with open(file_path, 'w') as file:
                    if type(select) != type(None):
                        if str(select) in data['original_file_path']:
                            file.write(yaml)
                    else:
                        file.write(yaml)

                keys_list.append(data['unrendered_config']['unique_key'].strip())

    return keys_list


try:
    logging.info("checking if your manifest file and dbt project yml exists brb")

    manifest_data = open_read_file("target/manifest.json")
    dbtproject = open_read_file("dbt_project.yml")

    logging.info("GREAT SUCCESS! both exist welldone!!!!")
except:
    logging.error("ummmmm not good... please do a dbt doc generate and retry")

try:
    logging.info("okay cool, creating the yml files now :)")

    if __name__ == '__main__':
        logger_snytax_change(manifest_data=manifest_data)
        dbtdocgen(manifest_data=manifest_data, dbtproject=dbtproject)

    logging.info("ohhh girl!!! very niceeee, you should see them in each sub folder now!")

except:
    logging.error("ohhh girl!!! not very niceeee, fix it")
