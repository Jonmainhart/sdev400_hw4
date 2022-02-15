import logging
import boto3
from boto3.dynamodb.conditions import Key, Attr


# table of certain name exists
def table_exists(table_name):
    """
    Checks if a table exists with a given name.
    :param table_name: str
    :return: True if table exists, otherwise False
    
    Some portions of this code Copyright 2010-2019 
    Amazon.com, Inc. or its affiliates. All Rights Reserved.
    
    MoviesListTables.py
    """
    dynamodb = boto3.resource('dynamodb')
    
    tables_available = []
    for table in dynamodb.tables.all():
        tables_available.append(table.name) # Amazon
    if table_name in tables_available:
        return True
    return False
    
def create_table(table_definition):
    """
    create a table using a table definition.
    
    :param table_definition: dict
    """
    
    dynamodb = boto3.resource('dynamodb')
    
    # dump into variables
    name_table = table_definition["TableName"]
    schema_key = table_definition["KeySchema"]
    definition_attribute = table_definition["AttributeDefinitions"]
    throughput_provision = table_definition["ProvisionedThroughput"]
    
    dynamodb.create_table(
        TableName=name_table,
        KeySchema=schema_key,
        AttributeDefinitions=definition_attribute,
        ProvisionedThroughput=throughput_provision)

def batch_write(items):
    """
    populate table with a batch of items
    :param items: dict
    """
    
    dynamodb = boto3.client('dynamodb')
    
    dynamodb.batch_write_item(RequestItems=items)

def get_items(table_name):
    """
    gets the items from the table
    
    :return: dict
    """
    
    dynamodb = boto3.resource('dynamodb')
    
    response = dynamodb.Table(table_name).scan()
    
    return response

def update_record(table_name, item):
    """
    updates item record
    :param table_name: str
    :param item: dict
    """
    dynamodb = boto3.resource('dynamodb')
    # assign variables
    item_id = item["ID"]
    name = item["name"]
    win = item["wins"]
    tie = item["ties"]
    loss = item["losses"]
    # overwrite the record
    # put_item() will overwrite item with same Key
    dynamodb.Table(table_name).put_item(
        Item={
            'ID': item_id,
            'name': name,
            'wins': win,
            'ties': tie,
            'losses': loss
        })

def del_table(table_name):
    """
    deletes specified table.
    :param table_name: str
    """
    dynamodb = boto3.client('dynamodb')
    
    dynamodb.delete_table(TableName=table_name)
