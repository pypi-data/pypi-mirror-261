from mando import command, main

from ketacli.sdk.base.client import *
from ketacli.sdk.request.list import list_assets_request
from ketacli.sdk.request.get import get_asset_by_id_request

from ketacli.sdk.output.output import list_output, describe_output, get_asset_output


@command
def login(name="keta", endpoint="http://localhost:9000", token=""):
    do_login(name=name, endpoint=endpoint, token=token)


@command
def logout():
    do_logout()

@command
def list(asset_type, groupId=-1, order="desc", pageNo=1, pageSize=10, prefix="", sort="updateTime", fields = ""):
    req = list_assets_request(asset_type, groupId, order, pageNo, pageSize, prefix, sort)
    resp = request_get(req["path"], req["query_params"], req["custom_headers"]).json()
    output_fields = []
    if len(fields.strip()) > 0:
        output_fields = fields.strip().split(",")
    table = list_output(asset_type, output_fields=output_fields, resp=resp)
    if table is None:
        print(f"we cannot find any {asset_type}")
    else:
        print(table)    
        
@command
def get(asset_type, asset_id, fields=""):
    req = get_asset_by_id_request(asset_type=asset_type, asset_id=asset_id)
    resp = request_get(req["path"], req["query_params"], req["custom_headers"]).json()
    output_fields = []
    if len(fields.strip()) > 0:
        output_fields = fields.strip().split(",")
    table = get_asset_output(output_fields=output_fields, resp=resp)
    table.align = "l"
    if table is None:
        print(f"we cannot find any {asset_type}")
    else:
        print(table)    
        
@command
def describe(asset_type):
    req = list_assets_request(asset_type)
    resp = request_get(req["path"], req["query_params"], req["custom_headers"]).json()
    table = describe_output(asset_type, resp=resp)
    if table is None:
        print(f"we cannot find any {asset_type}")
    else:
        print(table)

if __name__=="__main__":
    main()


        
        
    