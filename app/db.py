import os
import boto3
from boto3.dynamodb.conditions import Key

AWS_REGION = os.getenv("AWS_REGION", "us-west-1")
TABLE_REGISTRY = os.getenv("DDB_TABLE_REGISTRY", "service_registry")
TABLE_STATUS = os.getenv("DDB_TABLE_STATUS", "service_status")

dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
registry_tbl = dynamodb.Table(TABLE_REGISTRY)
status_tbl = dynamodb.Table(TABLE_STATUS)

def put_service(item: dict):
    registry_tbl.put_item(Item=item)

def list_services():
    resp = registry_tbl.scan()
    return resp.get("Items", [])

def put_status(item: dict):
    status_tbl.put_item(Item=item)

def get_lastest_status(service_id: str):
    # query descending by checked_at (SK) and take first
    resp = status_tbl.query(
        KeyConditionExpression=Key("service_id").eq(service_id),
        ScanIndexForward=False,
        Limit=1,
    )
    items = resp.get("Items", [])
    return items[0] if items else None

def list_status_history(service_id: str, limit: int=20):
    resp = status_tbl.query(
        KeyConditionExpression=Key("service_id").eq(service_id),
        ScanIndexForward=False,
        Limit=Limit
    )
    return resp.get("Items", [])