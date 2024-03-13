from mando import command, main

from ketacli.sdk.base.client import *
from ketacli.sdk.request.list import list_assets_request
from ketacli.sdk.output.list import list_output, describe_output


@command
def login(name="keta", endpoint="http://localhost:9000", token=""):
    do_login(name=name, endpoint=endpoint, token=token)


@command
def logout():
    do_logout()

@command
def list(asset_name, groupId=-1, order="desc", pageNo=1, pageSize=10, prefix="", sort="updateTime", fields = ""):
    req = list_assets_request(asset_name, groupId, order, pageNo, pageSize, prefix, sort)
    resp = request_get(req["path"], req["query_params"], req["custom_headers"]).json()
    output_fields = []
    if len(fields.strip()) > 0:
        output_fields = fields.strip().split(",")
    table = list_output(asset_name, output_fields=output_fields, resp=resp)
    if table is None:
        print(f"we cannot find any {asset_name}")
    else:
        print(table)    
@command
def describe(asset_name):
    req = list_assets_request(asset_name)
    resp = request_get(req["path"], req["query_params"], req["custom_headers"]).json()
    table = describe_output(asset_name, resp=resp)
    if table is None:
        print(f"we cannot find any {asset_name}")
    else:
        print(table)

if __name__=="__main__":
    main()


        
        
    