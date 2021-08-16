# package import
import json
import numpy as np
import tensorflow as tf
import tensorflow as tf

# Model Load 
sp_smdm_dnn_model = tf.keras.models.load_model('/var/task/lambda-with-docker-container/model/dnn_sp_smdm_model')
bz_smsm_dnn_model = tf.keras.models.load_model('/var/task/lambda-with-docker-container/model/dnn_bz_smsm_model')

def handler(event, context):
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hi')
    }
