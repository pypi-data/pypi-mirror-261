from typing import Optional
from raga import TestSession, ModelABTestRules, FMARules, LQRules, LDTRules, EventABTestRules, Filter, OcrRules, OcrAnomalyRules, \
    DARules, FMA_LLMRules, ClassImbalanceRules, SBRules, IPDRules



def model_ab_test(test_session:TestSession,
                  dataset_name: str, 
                  test_name: str, 
                  modelA: str, 
                  modelB: str,
                  type: str, 
                  rules: ModelABTestRules, 
                  aggregation_level:  Optional[list] = [],
                  gt: Optional[str] = "", 
                  filter: Optional[str] = ""):
    dataset_id = ab_test_validation(test_session, dataset_name, test_name, modelA, modelB, type, rules, gt, aggregation_level)    
    return {
            "datasetId": dataset_id,
            "experimentId": test_session.experiment_id,
            "name": test_name,
            "modelA": modelA,
            "modelB": modelB,
            "type": type,
            "rules": rules.get(),
            "aggregationLevels": aggregation_level,
            'filter':filter,
            'gt':gt,
            'test_type':'ab_test'
        }

def event_ab_test(test_session:TestSession, 
                  dataset_name: str, 
                  test_name: str, 
                  modelA: str,                  
                  modelB: str,                  
                  object_detection_modelA: str,                
                  object_detection_modelB: str,                
                  type: str, 
                  sub_type:str,
                  rules: EventABTestRules, 
                  aggregation_level:  Optional[list] = [],
                  output_type:Optional[str] = "", 
                  filter: Optional[Filter] = None):
    dataset_id = ab_event_test_validation(test_session, dataset_name, test_name, modelA, modelB, type, sub_type, rules, object_detection_modelA, object_detection_modelB, aggregation_level)    
    payload = {
            "datasetId": dataset_id,
            "experimentId": test_session.experiment_id,
            "name": test_name,
            "modelA": modelA,
            "modelB": modelB,
            "objectDetectionModelA":object_detection_modelA,
            "objectDetectionModelB":object_detection_modelB,
            "type": type,
            "subType":sub_type,
            "rules": rules.get(),
            "aggregationLevels": aggregation_level,
            'filter':"",
            'outputType':output_type,
            'test_type':'event_ab_test'
        }
    if isinstance(filter, Filter):
         payload["filter"] = filter.get()
    return payload

def ab_event_test_validation(test_session:TestSession, 
                       dataset_name: str, 
                       test_name: str, 
                       modelA: str,                        
                       modelB:str,                        
                       type: str, 
                       sub_type: str,
                       rules: ModelABTestRules,    
                       object_detection_modelA: str,
                       object_detection_modelB: str,                  
                       aggregation_level:Optional[list] = []):
    from raga.constants import INVALID_RESPONSE, INVALID_RESPONSE_DATA, REQUIRED_ARG_V2

    assert isinstance(test_session, TestSession), f"{REQUIRED_ARG_V2.format('test_session', 'instance of the TestSession')}"
    assert isinstance(dataset_name, str) and dataset_name, f"{REQUIRED_ARG_V2.format('dataset_name', 'str')}"

    res_data = test_session.http_client.get(f"api/dataset?projectId={test_session.project_id}&name={dataset_name}", headers={"Authorization": f'Bearer {test_session.token}'})

    if not isinstance(res_data, dict):
            raise ValueError(INVALID_RESPONSE)
    
    dataset_id = res_data.get("data", {}).get("id")

    if not dataset_id:
        raise KeyError(INVALID_RESPONSE_DATA)
    
    assert isinstance(test_name, str) and test_name, f"{REQUIRED_ARG_V2.format('test_name', 'str')}"
    assert isinstance(modelA, str) and modelA, f"{REQUIRED_ARG_V2.format('modelA', 'str')}"
    assert isinstance(modelB, str) and modelB, f"{REQUIRED_ARG_V2.format('modelB', 'str')}"
    assert isinstance(object_detection_modelA, str) and object_detection_modelA, f"{REQUIRED_ARG_V2.format('object_detection_modelA', 'str')}"
    assert isinstance(object_detection_modelB, str) and object_detection_modelB, f"{REQUIRED_ARG_V2.format('object_detection_modelB', 'str')}"
    assert isinstance(sub_type, str), f"{REQUIRED_ARG_V2.format('sub_type', 'str')}"
    assert isinstance(type, str), f"{REQUIRED_ARG_V2.format('type', 'str')}"
    assert isinstance(rules, ModelABTestRules) and rules.get(), f"{REQUIRED_ARG_V2.format('rules', 'instance of the ModelABTestRules')}"

    if aggregation_level:
        assert isinstance(aggregation_level, list), f"{REQUIRED_ARG_V2.format('aggregation_level', 'str')}"

    return dataset_id

def ab_test_validation(test_session:TestSession, 
                       dataset_name: str, 
                       test_name: str, 
                       modelA: str, 
                       modelB: str,
                       type: str, 
                       rules: ModelABTestRules,
                       gt: Optional[str] = "", 
                       aggregation_level:Optional[list] = []):
    from raga.constants import INVALID_RESPONSE, INVALID_RESPONSE_DATA, REQUIRED_ARG_V2

    assert isinstance(test_session, TestSession), f"{REQUIRED_ARG_V2.format('test_session', 'instance of the TestSession')}"
    assert isinstance(dataset_name, str) and dataset_name, f"{REQUIRED_ARG_V2.format('dataset_name', 'str')}"

    res_data = test_session.http_client.get(f"api/dataset?projectId={test_session.project_id}&name={dataset_name}", headers={"Authorization": f'Bearer {test_session.token}'})

    if not isinstance(res_data, dict):
            raise ValueError(INVALID_RESPONSE)
    
    dataset_id = res_data.get("data", {}).get("id")

    if not dataset_id:
        raise KeyError(INVALID_RESPONSE_DATA)
    
    assert isinstance(test_name, str) and test_name, f"{REQUIRED_ARG_V2.format('test_name', 'str')}"
    assert isinstance(modelA, str) and modelA, f"{REQUIRED_ARG_V2.format('modelA', 'str')}"
    assert isinstance(modelB, str) and modelB, f"{REQUIRED_ARG_V2.format('modelB', 'str')}"
    assert isinstance(type, str), f"{REQUIRED_ARG_V2.format('type', 'str')}"
    assert isinstance(rules, ModelABTestRules) and rules.get(), f"{REQUIRED_ARG_V2.format('rules', 'instance of the ModelABTestRules')}"

    if aggregation_level:
        assert isinstance(aggregation_level, list), f"{REQUIRED_ARG_V2.format('aggregation_level', 'str')}"

    if type == "labelled":
        assert isinstance(gt, str) and gt, f"{REQUIRED_ARG_V2.format('gt', 'str')}"

    if type == "unlabelled" and isinstance(gt, str) and gt:
        raise ValueError("gt is not required on unlabelled type.")
    
    return dataset_id

def failure_mode_analysis(test_session:TestSession, 
                          dataset_name:str, 
                          test_name:str, 
                          model:str, 
                          gt:str,
                          rules:FMARules,
                          output_type:str,
                          type:str,
                          clustering:Optional[dict]={},
                          aggregation_level:Optional[list]=[],
                          object_detection_model:Optional[str]="",
                          object_detection_gt:Optional[str]="",
                          embedding_col_name:Optional[str]="",
                          ):
    
    dataset_id = failure_mode_analysis_validation(test_session=test_session, dataset_name=dataset_name, test_name=test_name, model=model, gt=gt, type=type, rules=rules, output_type=output_type, aggregation_level=aggregation_level, clustering=clustering)
    response = {
            "datasetId": dataset_id,
            "experimentId": test_session.experiment_id,
            "name": test_name,
            "model": model,
            "gt": gt,
            "type": type,
            "rules": rules.get(),
            "test_type":"cluster",
            "filter":"",
            "outputType":output_type,
            "aggregationLevels":aggregation_level,
        }
    if output_type == "event_detection":
        response['objectDetectionModel'] = object_detection_model
        response['objectDetectionGT'] = object_detection_gt

    if output_type == "instance_segmentation":
        response['embeddingColName'] = embedding_col_name

    if clustering:
        response['clusterId'] = clustering
    return response

def failure_mode_analysis_validation(test_session:TestSession, dataset_name:str, test_name:str, model:str, gt:str, rules:FMARules, output_type:str, type:str, aggregation_level:Optional[list]=[], clustering:Optional[dict]=None):
    from raga.constants import INVALID_RESPONSE, INVALID_RESPONSE_DATA, REQUIRED_ARG_V2

    assert isinstance(test_session, TestSession), f"{REQUIRED_ARG_V2.format('test_session', 'instance of the TestSession')}"
    assert isinstance(dataset_name, str) and dataset_name, f"{REQUIRED_ARG_V2.format('dataset_name', 'str')}"
    res_data = test_session.http_client.get(f"api/dataset?projectId={test_session.project_id}&name={dataset_name}", headers={"Authorization": f'Bearer {test_session.token}'})

    if not isinstance(res_data, dict):
            raise ValueError(INVALID_RESPONSE)
    
    dataset_id = res_data.get("data", {}).get("id")

    if not dataset_id:
        raise KeyError(INVALID_RESPONSE_DATA)
    assert isinstance(test_name, str) and test_name, f"{REQUIRED_ARG_V2.format('test_name', 'str')}"
    assert isinstance(model, str) and model, f"{REQUIRED_ARG_V2.format('model', 'str')}"
    assert isinstance(gt, str) and gt, f"{REQUIRED_ARG_V2.format('gt', 'str')}"
    assert isinstance(type, str) and type, f"{REQUIRED_ARG_V2.format('type', 'str')}"
    assert isinstance(rules, FMARules) and rules, f"{REQUIRED_ARG_V2.format('rules', 'instance of the FMARules')}"
    assert isinstance(output_type, str) and output_type, f"{REQUIRED_ARG_V2.format('output_type', 'str')}"

    if output_type == "object_detection":
         if type == "embedding" and not clustering:
              raise ValueError(f"{REQUIRED_ARG_V2.format('clustering', 'clustering function')}")
         if type == "metadata":
            assert isinstance(aggregation_level, list) and aggregation_level, f"{REQUIRED_ARG_V2.format('aggregation_level', 'list')}"
    return dataset_id

def clustering(test_session:TestSession, dataset_name:str, method:str, embedding_col:str, level:str, args: dict, interpolation:bool=False, force:Optional[bool]=False):
    from raga.constants import REQUIRED_ARG_V2

    assert isinstance(method, str) and method, f"{REQUIRED_ARG_V2.format('method', 'str')}"
    assert isinstance(embedding_col, str) and embedding_col, f"{REQUIRED_ARG_V2.format('embedding_col', 'str')}"
    assert isinstance(level, str) and level, f"{REQUIRED_ARG_V2.format('level', 'str')}"
    cluster = {
        "method": method,
        "embeddingCol": embedding_col,
        "level": level,
        "args": args,
        "interpolation": interpolation
    }
    if test_session is None and dataset_name is None:
        return cluster
    else:
        dataset_id = clustering_validation(test_session, dataset_name)
        api_end_point = 'api/experiment/test/cluster'
        payload = {
            "datasetId": dataset_id,
            "forceRecreate": force,
            "clustering": cluster
        }
        from raga.constants import INVALID_RESPONSE
        from raga.utils import wait_for_status
        res_data = test_session.http_client.post(api_end_point, data=payload, headers={"Authorization": f'Bearer {test_session.token}'})
        data = res_data.get('data')
        job_id = data.get('jobId')
        if not isinstance(res_data, dict):
            raise ValueError(INVALID_RESPONSE)
        if job_id is not None:
            wait_for_status(test_session, job_id=job_id, spin=True)
        return data.get('clusterId')

def clustering_validation(test_session:TestSession, dataset_name:str):
    from raga.constants import INVALID_RESPONSE, INVALID_RESPONSE_DATA

    res_data = test_session.http_client.get(f"api/dataset?projectId={test_session.project_id}&name={dataset_name}", headers={"Authorization": f'Bearer {test_session.token}'})

    if not isinstance(res_data, dict):
            raise ValueError(INVALID_RESPONSE)
    dataset_id = res_data.get("data", {}).get("id")

    if not dataset_id:
        raise KeyError(INVALID_RESPONSE_DATA)
    return dataset_id

def labelling_quality_test(test_session:TestSession, 
                           dataset_name:str, 
                           test_name:str, 
                           type:str, 
                           output_type: str, 
                           rules:LQRules,
                           gt:Optional[str] = "",
                           mistake_score_col_name: Optional[str]="",
                           train_model_column_name: Optional[str]="",
                           field_model_column_name: Optional[str]="",
                           embedding_train_col_name: Optional[str]="",
                           embedding_field_col_name: Optional[str]="",
                           embedding_col_name:Optional[str]=""):
    
    dataset_id = labelling_quality_test_validation(test_session, dataset_name, test_name, type, output_type, rules)
    payload = {
            "experimentId": test_session.experiment_id,
            "name": test_name,
            "type": type,
            "outputType": output_type,
            "rules": rules.get(),
            "filter":"",
        }
    
    if output_type == "instance_segmentation":
        payload["gt"] = gt
        
    if train_model_column_name is not None and train_model_column_name != "" and embedding_field_col_name is not None and embedding_field_col_name != "":
        payload["trainDatasetId"]= dataset_id
        payload["fieldDatasetId"]= dataset_id
        payload["trainModelColumnName"] = train_model_column_name
        payload["fieldModelColumnName"] = field_model_column_name
        payload["embeddingTrainColName"] = embedding_train_col_name
        payload["embeddingFieldColName"] = embedding_field_col_name
        payload["test_type"] = "labelling_consistency"
    else:
        payload["datasetId"] = dataset_id
        payload["mistakeScoreColName"] = mistake_score_col_name
        payload["embeddingColName"] = embedding_col_name
        payload["test_type"] = "labelling_quality"
    
    return payload


def labelling_quality_test_validation(test_session:TestSession, dataset_name:str, test_name:str, type:str, output_type:str,  rules:LQRules):
    from raga.constants import INVALID_RESPONSE, INVALID_RESPONSE_DATA, REQUIRED_ARG_V2

    assert isinstance(test_session, TestSession), f"{REQUIRED_ARG_V2.format('test_session', 'instance of the TestSession')}"
    assert isinstance(dataset_name, str) and dataset_name, f"{REQUIRED_ARG_V2.format('dataset_name', 'str')}"
    res_data = test_session.http_client.get(f"api/dataset?projectId={test_session.project_id}&name={dataset_name}", headers={"Authorization": f'Bearer {test_session.token}'})

    if not isinstance(res_data, dict):
            raise ValueError(INVALID_RESPONSE)
    dataset_id = res_data.get("data", {}).get("id")

    if not dataset_id:
        raise KeyError(INVALID_RESPONSE_DATA)
    
    assert isinstance(test_name, str) and test_name, f"{REQUIRED_ARG_V2.format('test_name', 'str')}"
    assert isinstance(type, str) and type, f"{REQUIRED_ARG_V2.format('type', 'str')}"
    assert isinstance(output_type, str) and output_type, f"{REQUIRED_ARG_V2.format('output_type', 'str')}"
    assert isinstance(rules, LQRules) and rules, f"{REQUIRED_ARG_V2.format('rules', 'str')}"
    return dataset_id

def ocr_missing_test_analysis(test_session:TestSession,
                      dataset_name:str,
                      test_name:str,
                      model:str,
                      type:str,
                      output_type: str,
                      rules:OcrRules):

    dataset_id = ocr_missing_test_analysis_validation(test_session, dataset_name, test_name, model, type, output_type, rules)
    return {
        "datasetId": dataset_id,
        "experimentId": test_session.experiment_id,
        "name": test_name,
        "model":model,
        "type": type,
        "outputType": output_type,
        "rules": rules.get(),
        "test_type":"ocr_test"
    }

def ocr_missing_test_analysis_validation(test_session:TestSession, dataset_name:str, test_name:str, model:str, type:str, output_type:str, rules:OcrRules):
    from raga.constants import INVALID_RESPONSE, INVALID_RESPONSE_DATA, REQUIRED_ARG_V2

    assert isinstance(test_session, TestSession), f"{REQUIRED_ARG_V2.format('test_session', 'instance of the TestSession')}"
    assert isinstance(dataset_name, str) and dataset_name, f"{REQUIRED_ARG_V2.format('dataset_name', 'str')}"
    res_data = test_session.http_client.get(f"api/dataset?projectId={test_session.project_id}&name={dataset_name}", headers={"Authorization": f'Bearer {test_session.token}'})

    if not isinstance(res_data, dict):
        raise ValueError(INVALID_RESPONSE)
    dataset_id = res_data.get("data", {}).get("id")

    if not dataset_id:
        raise KeyError(INVALID_RESPONSE_DATA)

    assert isinstance(test_name, str) and test_name, f"{REQUIRED_ARG_V2.format('test_name', 'str')}"
    assert isinstance(type, str) and type, f"{REQUIRED_ARG_V2.format('type', 'str')}"
    assert isinstance(model, str) and model, f"{REQUIRED_ARG_V2.format('model', 'str')}"
    assert isinstance(output_type, str) and output_type, f"{REQUIRED_ARG_V2.format('output_type', 'str')}"
    assert isinstance(rules, OcrRules) and rules, f"{REQUIRED_ARG_V2.format('rules', 'str')}"
    return dataset_id

def ocr_anomaly_test_analysis(test_session:TestSession,
                              dataset_name:str,
                              test_name:str,
                              model:str,
                              type:str,
                              output_type: str,
                              rules:OcrRules):

    dataset_id = ocr_anomaly_test_analysis_validation(test_session, dataset_name, test_name, model, type, output_type, rules)
    return {
        "datasetId": dataset_id,
        "experimentId": test_session.experiment_id,
        "name": test_name,
        "model":model,
        "type": type,
        "outputType": output_type,
        "rules": rules.get(),
        "test_type":"ocr_test"
    }

def ocr_anomaly_test_analysis_validation(test_session:TestSession, dataset_name:str, test_name:str, model:str, type:str, output_type:str, rules:OcrAnomalyRules):
    from raga.constants import INVALID_RESPONSE, INVALID_RESPONSE_DATA, REQUIRED_ARG_V2

    assert isinstance(test_session, TestSession), f"{REQUIRED_ARG_V2.format('test_session', 'instance of the TestSession')}"
    assert isinstance(dataset_name, str) and dataset_name, f"{REQUIRED_ARG_V2.format('dataset_name', 'str')}"
    res_data = test_session.http_client.get(f"api/dataset?projectId={test_session.project_id}&name={dataset_name}", headers={"Authorization": f'Bearer {test_session.token}'})

    if not isinstance(res_data, dict):
        raise ValueError(INVALID_RESPONSE)
    dataset_id = res_data.get("data", {}).get("id")

    if not dataset_id:
        raise KeyError(INVALID_RESPONSE_DATA)

    assert isinstance(test_name, str) and test_name, f"{REQUIRED_ARG_V2.format('test_name', 'str')}"
    assert isinstance(type, str) and type, f"{REQUIRED_ARG_V2.format('type', 'str')}"
    assert isinstance(model, str) and model, f"{REQUIRED_ARG_V2.format('model', 'str')}"
    assert isinstance(output_type, str) and output_type, f"{REQUIRED_ARG_V2.format('output_type', 'str')}"
    assert isinstance(rules, OcrAnomalyRules) and rules, f"{REQUIRED_ARG_V2.format('rules', 'str')}"
    return dataset_id


def active_learning(test_session:TestSession,
                    dataset_name:str,
                    test_name:str,
                    type:str,
                    output_type: str,
                    embed_col_name: str,
                    budget: int):

    dataset_id = active_learning_validation(test_session, dataset_name, test_name, type, output_type, embed_col_name, budget)
    return {
        "datasetId": dataset_id,
        "experimentId": test_session.experiment_id,
        "name": test_name,
        "type": type,
        "outputType": output_type,
        "embeddingColName": embed_col_name,
        "budget": budget,
        "test_type":"active_learning"
    }

def active_learning_validation(test_session:TestSession, dataset_name:str, test_name:str, type:str, output_type:str, embed_col_name:str, budget:int):
    from raga.constants import INVALID_RESPONSE, INVALID_RESPONSE_DATA, REQUIRED_ARG_V2

    assert isinstance(test_session, TestSession), f"{REQUIRED_ARG_V2.format('test_session', 'instance of the TestSession')}"
    assert isinstance(dataset_name, str) and dataset_name, f"{REQUIRED_ARG_V2.format('dataset_name', 'str')}"
    res_data = test_session.http_client.get(f"api/dataset?projectId={test_session.project_id}&name={dataset_name}", headers={"Authorization": f'Bearer {test_session.token}'})

    if not isinstance(res_data, dict):
        raise ValueError(INVALID_RESPONSE)
    dataset_id = res_data.get("data", {}).get("id")

    if not dataset_id:
        raise KeyError(INVALID_RESPONSE_DATA)

    assert isinstance(test_name, str) and test_name, f"{REQUIRED_ARG_V2.format('test_name', 'str')}"
    assert isinstance(type, str) and type, f"{REQUIRED_ARG_V2.format('type', 'str')}"
    assert isinstance(output_type, str) and output_type, f"{REQUIRED_ARG_V2.format('output_type', 'str')}"
    assert isinstance(budget, int) and output_type, f"{REQUIRED_ARG_V2.format('output_type', 'str')}"
    assert isinstance(embed_col_name, str) and embed_col_name, f"{REQUIRED_ARG_V2.format('embed_col_name', 'str')}"
    return dataset_id

def semantic_similarity(test_session:TestSession,
                        dataset_name:str,
                        test_name:str,
                        type:str,
                        output_type: str,
                        embed_col_name: str,
                        rules: LQRules,
                        generated_embed_col_name: Optional[str] = ""):

    dataset_id = semantic_similarity_validation(test_session, dataset_name, test_name, type, output_type, embed_col_name, rules, generated_embed_col_name)
    payload =  {
        "datasetId": dataset_id,
        "experimentId": test_session.experiment_id,
        "name": test_name,
        "type": type,
        "outputType": output_type,
        "embeddingColName": embed_col_name,
        "rules": rules.get(),
    }
    if generated_embed_col_name is not None and generated_embed_col_name!="":
        payload["generatedEmbeddingColName"] = generated_embed_col_name
        payload["test_type"] = "semantic_similarity"
    else:
        payload["test_type"] = "nearest-neighbour"

    return payload

def semantic_similarity_validation(test_session:TestSession, dataset_name:str, test_name:str, type:str, output_type:str, embed_col_name:str, rules: LQRules, generated_embed_col_name: Optional[str] = ""):
    from raga.constants import INVALID_RESPONSE, INVALID_RESPONSE_DATA, REQUIRED_ARG_V2

    assert isinstance(test_session, TestSession), f"{REQUIRED_ARG_V2.format('test_session', 'instance of the TestSession')}"
    assert isinstance(dataset_name, str) and dataset_name, f"{REQUIRED_ARG_V2.format('dataset_name', 'str')}"
    res_data = test_session.http_client.get(f"api/dataset?projectId={test_session.project_id}&name={dataset_name}", headers={"Authorization": f'Bearer {test_session.token}'})

    if not isinstance(res_data, dict):
        raise ValueError(INVALID_RESPONSE)
    dataset_id = res_data.get("data", {}).get("id")

    if not dataset_id:
        raise KeyError(INVALID_RESPONSE_DATA)

    assert isinstance(test_name, str) and test_name, f"{REQUIRED_ARG_V2.format('test_name', 'str')}"
    assert isinstance(type, str) and type, f"{REQUIRED_ARG_V2.format('type', 'str')}"
    assert isinstance(output_type, str) and output_type, f"{REQUIRED_ARG_V2.format('output_type', 'str')}"
    assert isinstance(embed_col_name, str) and embed_col_name, f"{REQUIRED_ARG_V2.format('embed_col_name', 'str')}"
    assert isinstance(rules, LQRules) and rules, f"{REQUIRED_ARG_V2.format('rules', 'str')}"
    return dataset_id

def nearest_duplicate(test_session:TestSession,
                      dataset_name:str,
                      test_name:str,
                      type:str,
                      output_type: str,
                      embed_col_name: str,
                      rules: LQRules):
    return semantic_similarity(test_session, dataset_name, test_name, type, output_type, embed_col_name, rules)


def data_leakage_test(test_session:TestSession,
                      dataset_name:str,
                      test_name:str,
                      type:str,
                      output_type: str,
                      rules: LQRules,
                      sub_type:Optional[str] = "",
                      train_dataset_name: Optional[str] = "",
                      train_embed_col_name: Optional[str] = "",
                      embed_col_name: Optional[str] = ""):

    dataset_id = data_leakage_test_validation(test_session, dataset_name, test_name, type, output_type)
    payload =  {
        "datasetId": dataset_id,
        "experimentId": test_session.experiment_id,
        "name": test_name,
        "type": type,
        "outputType": output_type,
        "rules": rules.get()
    }

    if train_dataset_name is not None and train_dataset_name!="" and train_embed_col_name is not None and train_embed_col_name!="" and embed_col_name is not None and embed_col_name!="":
        trainDataset_id = data_leakage_test_validation(test_session, train_dataset_name, test_name, type, output_type)
        payload["trainDatasetId"] = trainDataset_id
        payload["embeddingColName"] = embed_col_name
        payload["trainEmbeddingColName"] = train_embed_col_name
        payload["test_type"] = "data_leakage"
    else:
        payload["subType"] = sub_type
        payload["test_type"] = "data_augmentation"

    return payload

def data_leakage_test_validation(test_session:TestSession, dataset_name:str, test_name:str, type:str, output_type:str):
    from raga.constants import INVALID_RESPONSE, INVALID_RESPONSE_DATA, REQUIRED_ARG_V2
    assert isinstance(test_session, TestSession), f"{REQUIRED_ARG_V2.format('test_session', 'instance of the TestSession')}"
    assert isinstance(dataset_name, str) and dataset_name, f"{REQUIRED_ARG_V2.format('dataset_name', 'str')}"
    res_data = test_session.http_client.get(f"api/dataset?projectId={test_session.project_id}&name={dataset_name}", headers={"Authorization": f'Bearer {test_session.token}'})

    if not isinstance(res_data, dict):
        raise ValueError(INVALID_RESPONSE)
    dataset_id = res_data.get("data", {}).get("id")

    if not dataset_id:
        raise KeyError(INVALID_RESPONSE_DATA)

    assert isinstance(test_name, str) and test_name, f"{REQUIRED_ARG_V2.format('test_name', 'str')}"
    assert isinstance(type, str) and type, f"{REQUIRED_ARG_V2.format('type', 'str')}"
    assert isinstance(output_type, str) and output_type, f"{REQUIRED_ARG_V2.format('output_type', 'str')}"
    return dataset_id

def data_augmentation_test(test_session:TestSession,
                      dataset_name:str,
                      test_name:str,
                      type:str,
                      sub_type:str,
                      output_type: str,
                      rules: DARules,):
    return data_leakage_test(test_session, dataset_name, test_name, type, output_type, rules, sub_type)


def label_drift_test(test_session: TestSession,
                     referenceDataset: str,
                     evalDataset: str,
                     test_name: str,
                     type: str,
                     output_type: str,
                     gt: str,
                     rules: LDTRules):

    ref_res_data = test_session.http_client.get(f"api/dataset?projectId={test_session.project_id}&name={referenceDataset}", headers={"Authorization": f'Bearer {test_session.token}'})
    ref_dataset_id = ref_res_data.get("data", {}).get("id")

    eval_res_data = test_session.http_client.get(f"api/dataset?projectId={test_session.project_id}&name={evalDataset}", headers={"Authorization": f'Bearer {test_session.token}'})
    eval_dataset_id = eval_res_data.get("data", {}).get("id")

    response = {
        "referenceDatasetId" : ref_dataset_id,
        "evalDatasetId": eval_dataset_id,
        "name": test_name,
        "gt": gt,
        "type": type,
        "test_type": "label-drift-detection",
        "outputType": output_type,
        "rules": rules.get(),
    }

    return response


def fma_structured_data(test_session: TestSession,
                        dataset_name: str,
                        test_name: str,
                        model: str,
                        gt: str,
                        rules: LQRules,
                        output_type: str,
                        type: str,
                        embedding: str,
                        clustering: Optional[dict] = {},
                        ):
    dataset_id = fma_structured_data_validation(test_session=test_session, dataset_name=dataset_name,
                                                test_name=test_name, model=model, gt=gt, type=type, rules=rules,
                                                output_type=output_type,
                                                clustering=clustering, embedding=embedding)
    response = {
        "datasetId": dataset_id,
        "experimentId": test_session.experiment_id,
        "name": test_name,
        "model": model,
        "gt": gt,
        "type": type,
        "rules": rules.get(),
        "test_type": "fma_sd",
        "filter": "",
        "embeddingColName":embedding,
        "outputType": output_type
    }

    if clustering:
        response['clusterId'] = clustering
    return response

def fma_structured_data_validation(test_session: TestSession, dataset_name: str, test_name: str, model: str, gt: str,
                                   rules: LQRules, output_type: str, type: str, embedding:str,
                                   clustering: Optional[dict] = None):
    from raga.constants import INVALID_RESPONSE, INVALID_RESPONSE_DATA, REQUIRED_ARG_V2

    assert isinstance(test_session,
                      TestSession), f"{REQUIRED_ARG_V2.format('test_session', 'instance of the TestSession')}"
    assert isinstance(dataset_name, str) and dataset_name, f"{REQUIRED_ARG_V2.format('dataset_name', 'str')}"
    res_data = test_session.http_client.get(f"api/dataset?projectId={test_session.project_id}&name={dataset_name}",
                                            headers={"Authorization": f'Bearer {test_session.token}'})

    if not isinstance(res_data, dict):
        raise ValueError(INVALID_RESPONSE)

    dataset_id = res_data.get("data", {}).get("id")

    if not dataset_id:
        raise KeyError(INVALID_RESPONSE_DATA)
    assert isinstance(test_name, str) and test_name, f"{REQUIRED_ARG_V2.format('test_name', 'str')}"
    assert isinstance(model, str) and model, f"{REQUIRED_ARG_V2.format('model', 'str')}"
    assert isinstance(gt, str) and gt, f"{REQUIRED_ARG_V2.format('gt', 'str')}"
    assert isinstance(type, str) and type, f"{REQUIRED_ARG_V2.format('type', 'str')}"
    assert isinstance(rules,LQRules) and rules, f"{REQUIRED_ARG_V2.format('rules', 'instance of the LQRules')}"
    assert isinstance(output_type, str) and output_type, f"{REQUIRED_ARG_V2.format('output_type', 'str')}"
    assert isinstance(embedding, str) and output_type, f"{REQUIRED_ARG_V2.format('embedding', 'str')}"

    return dataset_id

def scenario_imbalance(test_session: TestSession,
                        dataset_name: str,
                        test_name: str,
                        rules: SBRules,
                        output_type: str,
                        type: str,
                        embedding: Optional[str] = None,
                        clustering: Optional[dict] = {},
                        aggregationLevels: Optional[list] = []
                        ):
    dataset_id = scenario_imbalance_validation(test_session=test_session, dataset_name=dataset_name,
                                                test_name=test_name, type=type, rules=rules,
                                                output_type=output_type,
                                                clustering=clustering, embedding=embedding,
                                                aggregationLevels=aggregationLevels)
    response = {
        "datasetId": dataset_id,
        "experimentId": test_session.experiment_id,
        "name": test_name,
        "type": type,
        "rules": rules.get(),
        "test_type": "scenario_imbalance",
        "embeddingColName":embedding,
        "outputType": output_type,
        "aggregationLevels": aggregationLevels
    }

    if clustering:
        response['clusterId'] = clustering
    return response

def scenario_imbalance_validation(test_session: TestSession, dataset_name: str, test_name: str, type: str,
                                   rules: SBRules, output_type: str, embedding: Optional[str] = None,
                                   clustering: Optional[dict] = None,
                                  aggregationLevels: Optional[list] = None):
    from raga.constants import INVALID_RESPONSE, INVALID_RESPONSE_DATA, REQUIRED_ARG_V2

    assert isinstance(test_session,
                      TestSession), f"{REQUIRED_ARG_V2.format('test_session', 'instance of the TestSession')}"
    assert isinstance(dataset_name, str) and dataset_name, f"{REQUIRED_ARG_V2.format('dataset_name', 'str')}"
    res_data = test_session.http_client.get(f"api/dataset?projectId={test_session.project_id}&name={dataset_name}",
                                            headers={"Authorization": f'Bearer {test_session.token}'})

    if not isinstance(res_data, dict):
        raise ValueError(INVALID_RESPONSE)

    dataset_id = res_data.get("data", {}).get("id")

    if not dataset_id:
        raise KeyError(INVALID_RESPONSE_DATA)
    assert isinstance(test_name, str) and test_name, f"{REQUIRED_ARG_V2.format('test_name', 'str')}"
    assert isinstance(type, str) and type, f"{REQUIRED_ARG_V2.format('type', 'str')}"
    assert isinstance(rules,SBRules) and rules, f"{REQUIRED_ARG_V2.format('rules', 'instance of the SBRules')}"
    assert isinstance(output_type, str) and output_type, f"{REQUIRED_ARG_V2.format('output_type', 'str')}"
    return dataset_id



def failure_mode_analysis_llm(test_session:TestSession,
                              dataset_name:str,
                              test_name:str,
                              model:str,
                              gt:str,
                              rules:FMA_LLMRules,
                              type:str,
                              output_type:str,
                              prompt_col_name: str,
                              model_column: str,
                              gt_column: str,
                              embedding_col_name: str,
                              model_embedding_column: str,
                              gt_embedding_column: str,
                              clustering:Optional[dict]={},
                              ):

    dataset_id = failure_mode_analysis_llm_validation(test_session=test_session, dataset_name=dataset_name, test_name=test_name, model=model, gt=gt, rules=rules, output_type=output_type, model_column= model_column, gt_column = gt_column, model_embedding_column = model_embedding_column, gt_embedding_column =  gt_embedding_column, clustering=clustering)
    testRules = rules.get()

    metricList = {}
    for rulesDict in testRules:
        if(rulesDict["evalMetric"] == "BLEU"):
            metricList["BLEU"] = "bleu_score"
        elif(rulesDict["evalMetric"] == "ROUGE"):
            metricList["ROUGE"] = "rouge_score"
        elif(rulesDict["evalMetric"] == "METEOR"):
            metricList["METEOR"] = "meteor_score"
        elif(rulesDict["evalMetric"] == "CosineSimilarity"):
            metricList["CosineSimilarity"] = "cosine_score"
        elif(rulesDict["evalMetric"] == "user_feedback"):
            metricList["user_feedback"] = "user_feedback"

    response = {
        "datasetId": dataset_id,
        "experimentId": test_session.experiment_id,
        "name": test_name,
        "model": model,
        "gt": gt,
        "rules": rules.get(),
        "promptColName": prompt_col_name,
        "modelColName" : model_column,
        "gtColName" : gt_column,
        "embeddingColName": embedding_col_name,
        "modelEmbeddingColName" : model_embedding_column,
        "gtEmbeddingColName": gt_embedding_column,
        "test_type":"fma-llm",
        "type": type,
        "metricList": metricList,
        "outputType":output_type
    }

    if clustering:
        response['clusterId'] = clustering
    return response

def failure_mode_analysis_llm_validation(test_session:TestSession, dataset_name:str, test_name:str, model:str, gt:str, rules:FMA_LLMRules, output_type:str, model_column:str, gt_column:str, model_embedding_column:str, gt_embedding_column:str, clustering:Optional[dict]=None):
    from raga.constants import INVALID_RESPONSE, INVALID_RESPONSE_DATA, REQUIRED_ARG_V2

    assert isinstance(test_session, TestSession), f"{REQUIRED_ARG_V2.format('test_session', 'instance of the TestSession')}"
    assert isinstance(dataset_name, str) and dataset_name, f"{REQUIRED_ARG_V2.format('dataset_name', 'str')}"
    res_data = test_session.http_client.get(f"api/dataset?projectId={test_session.project_id}&name={dataset_name}", headers={"Authorization": f'Bearer {test_session.token}'})

    if not isinstance(res_data, dict):
        raise ValueError(INVALID_RESPONSE)

    dataset_id = res_data.get("data", {}).get("id")

    if not dataset_id:
        raise KeyError(INVALID_RESPONSE_DATA)
    assert isinstance(test_name, str) and test_name, f"{REQUIRED_ARG_V2.format('test_name', 'str')}"
    assert isinstance(model, str) and model, f"{REQUIRED_ARG_V2.format('model', 'str')}"
    assert isinstance(gt, str) and gt, f"{REQUIRED_ARG_V2.format('gt', 'str')}"
    assert isinstance(model_column, str) and model_column, f"{REQUIRED_ARG_V2.format('model_column', 'str')}"
    assert isinstance(gt_column, str) and gt_column, f"{REQUIRED_ARG_V2.format('gt_column', 'str')}"
    assert isinstance(model_embedding_column, str) and model_embedding_column, f"{REQUIRED_ARG_V2.format('model_embedding_column', 'str')}"
    assert isinstance(gt_embedding_column, str) and gt_embedding_column, f"{REQUIRED_ARG_V2.format('gt_embedding_column', 'str')}"
    assert isinstance(rules, FMA_LLMRules) and rules, f"{REQUIRED_ARG_V2.format('rules', 'instance of the FMARules')}"
    assert isinstance(output_type, str) and output_type, f"{REQUIRED_ARG_V2.format('output_type', 'str')}"

    return dataset_id


def class_imbalance_test(test_session: TestSession,
                         dataset_name: str,
                         test_name: str,
                         type: str,
                         output_type: str,
                         annotation_column_name: str,
                         rules: ClassImbalanceRules):

    dataset_id = class_imbalance_test_validation(test_session=test_session, dataset_name=dataset_name, test_name=test_name, type=type, output_type=output_type, annotation_column_name=annotation_column_name, rules=rules)

    return {
        "datasetId": dataset_id,
        "experimentId": test_session.experiment_id,
        "name": test_name,
        "test_type": "class-imbalance",
        "type": type,
        "outputType": output_type,
        "annotationColumnName": annotation_column_name,
        "rules": rules.get(),
    }

def class_imbalance_test_validation(test_session: TestSession,
                                    dataset_name: str,
                                    test_name: str,
                                    type: str,
                                    output_type: str,
                                    annotation_column_name: str,
                                    rules: ClassImbalanceRules):

    from raga.constants import INVALID_RESPONSE, INVALID_RESPONSE_DATA, REQUIRED_ARG_V2
    assert isinstance(test_session, TestSession), f"{REQUIRED_ARG_V2.format('test_session', 'instance of the TestSession')}"
    assert isinstance(dataset_name, str) and dataset_name, f"{REQUIRED_ARG_V2.format('dataset_name', 'str')}"
    res_data = test_session.http_client.get(f"api/dataset?projectId={test_session.project_id}&name={dataset_name}", headers={"Authorization": f'Bearer {test_session.token}'})

    if not isinstance(res_data, dict):
        raise ValueError(INVALID_RESPONSE)

    dataset_id = res_data.get("data", {}).get("id")
    if not dataset_id:
        raise KeyError(INVALID_RESPONSE_DATA)

    assert isinstance(test_name, str) and test_name, f"{REQUIRED_ARG_V2.format('test_name', 'str')}"
    assert isinstance(type, str) and type, f"{REQUIRED_ARG_V2.format('type', 'str')}"
    assert isinstance(output_type, str) and output_type, f"{REQUIRED_ARG_V2.format('output_type', 'str')}"
    assert isinstance(annotation_column_name, str) and annotation_column_name, f"{REQUIRED_ARG_V2.format('annotation_column_name', 'str')}"
    assert isinstance(rules, ClassImbalanceRules) and rules, f"{REQUIRED_ARG_V2.format('rules', 'instance of the ClassImbalanceRules')}"
    return dataset_id


def image_property_drift(test_session: TestSession,
                         reference_dataset_name: str,
                         eval_dataset_name: str,
                         rules: IPDRules,
                         test_name: str,
                         type: str,
                         output_type: str,
                         ):
    reference_dataset_id = image_property_drift_data_validation(test_session=test_session,
                                                                dataset_name=reference_dataset_name,
                                                                test_name=test_name, rules=rules,
                                                                output_type=output_type, type=type)
    eval_dataset_id = image_property_drift_data_validation(test_session=test_session,
                                                           dataset_name=eval_dataset_name,
                                                           test_name=test_name, rules=rules,
                                                           output_type=output_type, type=type)

    response = {
        "datasetId": reference_dataset_id,
        "evalDatasetId": eval_dataset_id,
        "experimentId": test_session.experiment_id,
        "name": test_name,
        "type": type,
        "rules": rules.get(),
        "test_type": "image-property-drift",
        "outputType": output_type
    }

    return response

def image_property_drift_data_validation(test_session: TestSession, dataset_name: str, test_name: str,
                                   rules: IPDRules, output_type: str, type: str):
    from raga.constants import INVALID_RESPONSE, INVALID_RESPONSE_DATA, REQUIRED_ARG_V2

    assert isinstance(test_session,
                      TestSession), f"{REQUIRED_ARG_V2.format('test_session', 'instance of the TestSession')}"
    assert isinstance(dataset_name, str) and dataset_name, f"{REQUIRED_ARG_V2.format('dataset_name', 'str')}"
    res_data = test_session.http_client.get(f"api/dataset?projectId={test_session.project_id}&name={dataset_name}",
                                            headers={"Authorization": f'Bearer {test_session.token}'})


    if not isinstance(res_data, dict):
        raise ValueError(INVALID_RESPONSE)

    dataset_id = res_data.get("data", {}).get("id")

    if not dataset_id:
        raise KeyError(INVALID_RESPONSE_DATA)
    assert isinstance(test_name, str) and test_name, f"{REQUIRED_ARG_V2.format('test_name', 'str')}"
    assert isinstance(type, str) and type, f"{REQUIRED_ARG_V2.format('type', 'str')}"
    assert isinstance(rules,IPDRules) and rules, f"{REQUIRED_ARG_V2.format('rules', 'instance of the IPDRules')}"
    assert isinstance(output_type, str) and output_type, f"{REQUIRED_ARG_V2.format('output_type', 'str')}"

    return dataset_id
