import time

package_start_ms = int(round(time.time() * 1000))

# package import
import json
import numpy as np
import tensorflow as tf

package_end_ms = int(round(time.time() * 1000))

model_load_start_ms = int(round(time.time() * 1000))

# Model Load 
sp_smdm_dnn_model = tf.keras.models.load_model('/var/task/lambda-with-docker-container/model/dnn_sp_smdm_model')
bz_smsm_dnn_model = tf.keras.models.load_model('/var/task/lambda-with-docker-container/model/dnn_bz_smsm_model')

model_load_end_ms = int(round(time.time() * 1000))


def handler(event, context):
    
    function_start_ms = int(round(time.time() * 1000))

    data_pre_process_start_ms = int(round(time.time() * 1000))

    body = event["body-json"]

    # event 로부터 feature 전처리
    lr = body["lr"]
    lc = body["lc"]
    rc = body["rc"]
    ld = body["ld"]
    rd = body["rd"]
    lnnz = body["lnnz"]
    rnnz = body["rnnz"]

    # 모델 입력으로 사용할 input_feature 생성
    input_feature = np.array([[lr,lc,rc,ld,rd,lnnz,rnnz]])
    
    data_pre_process_end_ms = int(round(time.time() * 1000))
    
    model_inf_start_ms = int(round(time.time() * 1000))

    # input_feature 에 대한 모델별 예측값 생성
    sp_smdm_dnn_result = sp_smdm_dnn_model.predict(input_feature)
    bz_smsm_dnn_result = bz_smsm_dnn_model.predict(input_feature)
    
    model_inf_end_ms = int(round(time.time() * 1000))

    function_end_ms = int(round(time.time() * 1000))

    latency_result = \
        "package import : " + str(package_end_ms - package_start_ms) + " , " + \
        "model load: " + str(model_load_end_ms - model_load_start_ms) + " , " + \
        "function latency : " + str(function_end_ms - function_start_ms) + " , " + \
        "data pre-process : " + str(data_pre_process_end_ms - data_pre_process_start_ms) + " , " + \
        "model inference : " + str(model_inf_end_ms - model_inf_start_ms)

    # 결과 반환
    return {
        'statusCode': 200,
        'body': json.dumps(latency_result)
    }

# # package import
# import json
# import numpy as np
# import tensorflow as tf

# # Model Load 
# sp_smdm_dnn_model = tf.keras.models.load_model('/var/task/lambda-with-docker-container/model/dnn_sp_smdm_model')
# bz_smsm_dnn_model = tf.keras.models.load_model('/var/task/lambda-with-docker-container/model/dnn_bz_smsm_model')

# def handler(event, context):
    
#     body = event["body-json"]

#     # event 로부터 feature 전처리
#     lr = body["lr"]
#     lc = body["lc"]
#     rc = body["rc"]
#     ld = body["ld"]
#     rd = body["rd"]
#     lnnz = body["lnnz"]
#     rnnz = body["rnnz"]

#     # 모델 입력으로 사용할 input_feature 생성
#     input_feature = np.array([[lr,lc,rc,ld,rd,lnnz,rnnz]])
    
#     # input_feature 에 대한 모델별 예측값 생성
#     sp_smdm_dnn_result = sp_smdm_dnn_model.predict(input_feature)
#     bz_smsm_dnn_result = bz_smsm_dnn_model.predict(input_feature)
    
#     # sp_smdm 이 최적일 경우
#     if (sp_smdm_dnn_result[0] <= bz_smsm_dnn_result[0]):
#         optim_method = "sp_smdm"
#     # bz_smsm 이 최적일 경우
#     else:
#         optim_method = "bz_smsm"
    
# 	# 결과 생성
#     result = "sp_smdm : " + str(sp_smdm_dnn_result[0]) + " , " + \
# 		"bz_smsm : " + str(bz_smsm_dnn_result[0]) + " , " + \
# 		"optim_method : " + optim_method

# 	# 결과 반환
#     return {
#         'statusCode': 200,
#         'body': json.dumps(result)
#     }
