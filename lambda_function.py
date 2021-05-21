import json
import numpy as np
import xgboost as xgb

# 모델 불러오기
sp_smdm_xgb_model = xgb.XGBRegressor()
bz_smsm_xgb_model = xgb.XGBRegressor()
sp_smdm_xgb_model.load_model('/var/task/lambda-with-docker-container/model/sp_smdm_xgb.model')
bz_smsm_xgb_model.load_model('/var/task/lambda-with-docker-container/model/bz_smsm_xgb.model')

def lambda_handler(event, context):
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hi')
    }
