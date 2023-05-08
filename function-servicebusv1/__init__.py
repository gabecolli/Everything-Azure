import logging
import azure.functions as func
import json

def main(req: func.HttpRequest, msg: func.Out[str]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    

    
    req_body = req.get_json()
    sb_message = json.dumps(req_body)
    msg.set(sb_message)
    

    
    return func.HttpResponse(f"{req_body} was the data you passed from your mobile app.")
    


        