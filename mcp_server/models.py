# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T12:32:09+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field, RootModel, conint, constr


class Algorithm(Enum):
    sgd = 'sgd'


class AwsUserArn(RootModel[constr(pattern=r'arn:aws:iam::[0-9]+:((user/.+)|(root))')]):
    root: constr(pattern=r'arn:aws:iam::[0-9]+:((user/.+)|(root))') = Field(
        ...,
        description='An Amazon Web Service (AWS) user account identifier. The account identifier can be an AWS root account or an AWS Identity and Access Management (IAM) user.',
    )


class BatchPredictionFilterVariable(Enum):
    CreatedAt = 'CreatedAt'
    LastUpdatedAt = 'LastUpdatedAt'
    Status = 'Status'
    Name = 'Name'
    IAMUser = 'IAMUser'
    MLModelId = 'MLModelId'
    DataSourceId = 'DataSourceId'
    DataURI = 'DataURI'


class ComparatorValue(RootModel[constr(pattern=r'.*\S.*|^$', max_length=1024)]):
    root: constr(pattern=r'.*\S.*|^$', max_length=1024) = Field(
        ...,
        description='The value specified in a filtering condition. The <code>ComparatorValue</code> becomes the reference value when matching or evaluating data values in filtering and searching functions.',
    )


class ComputeStatistics(RootModel[bool]):
    root: bool


class DataRearrangement(RootModel[str]):
    root: str


class DataSchema(RootModel[constr(max_length=131071)]):
    root: constr(max_length=131071) = Field(
        ...,
        description='<p>The schema of a <code>DataSource</code>. The <code>DataSchema</code> defines the structure of the observation data in the data file(s) referenced in the <code>DataSource</code>. The DataSource schema is expressed in JSON format.</p> <p> <code>DataSchema</code> is not required if you specify a <code>DataSchemaUri</code> </p> <p>{ "version": "1.0", "recordAnnotationFieldName": "F1", "recordWeightFieldName": "F2", "targetFieldName": "F3", "dataFormat": "CSV", "dataFileContainsHeader": true, "variables": [ { "fieldName": "F1", "fieldType": "TEXT" }, { "fieldName": "F2", "fieldType": "NUMERIC" }, { "fieldName": "F3", "fieldType": "CATEGORICAL" }, { "fieldName": "F4", "fieldType": "NUMERIC" }, { "fieldName": "F5", "fieldType": "CATEGORICAL" }, { "fieldName": "F6", "fieldType": "TEXT" }, { "fieldName": "F7", "fieldType": "WEIGHTED_INT_SEQUENCE" }, { "fieldName": "F8", "fieldType": "WEIGHTED_STRING_SEQUENCE" } ], "excludedVariableNames": [ "F6" ] }</p>',
    )


class DataSourceFilterVariable(Enum):
    CreatedAt = 'CreatedAt'
    LastUpdatedAt = 'LastUpdatedAt'
    Status = 'Status'
    Name = 'Name'
    DataLocationS3 = 'DataLocationS3'
    IAMUser = 'IAMUser'


class DetailsAttributes(Enum):
    PredictiveModelType = 'PredictiveModelType'
    Algorithm = 'Algorithm'


class DetailsValue(RootModel[constr(min_length=1)]):
    root: constr(min_length=1)


class EDPPipelineId(RootModel[constr(min_length=1, max_length=1024)]):
    root: constr(min_length=1, max_length=1024)


class EDPResourceRole(RootModel[constr(min_length=1, max_length=64)]):
    root: constr(min_length=1, max_length=64)


class EDPSecurityGroupId(RootModel[constr(min_length=1, max_length=255)]):
    root: constr(min_length=1, max_length=255)


class EDPSecurityGroupIds(RootModel[List[EDPSecurityGroupId]]):
    root: List[EDPSecurityGroupId]


class EDPServiceRole(RootModel[constr(min_length=1, max_length=64)]):
    root: constr(min_length=1, max_length=64)


class EDPSubnetId(RootModel[constr(min_length=1, max_length=255)]):
    root: constr(min_length=1, max_length=255)


class EntityId(
    RootModel[constr(pattern=r'[a-zA-Z0-9_.-]+', min_length=1, max_length=64)]
):
    root: constr(pattern=r'[a-zA-Z0-9_.-]+', min_length=1, max_length=64)


class EntityName(RootModel[constr(pattern=r'.*\S.*|^$', max_length=1024)]):
    root: constr(pattern=r'.*\S.*|^$', max_length=1024) = Field(
        ...,
        description='A user-supplied name or description of the Amazon ML resource.',
    )


class EntityStatus(Enum):
    PENDING = 'PENDING'
    INPROGRESS = 'INPROGRESS'
    FAILED = 'FAILED'
    COMPLETED = 'COMPLETED'
    DELETED = 'DELETED'


class EpochTime(RootModel[datetime]):
    root: datetime = Field(..., description='A timestamp represented in epoch time.')


class EvaluationFilterVariable(Enum):
    CreatedAt = 'CreatedAt'
    LastUpdatedAt = 'LastUpdatedAt'
    Status = 'Status'
    Name = 'Name'
    IAMUser = 'IAMUser'
    MLModelId = 'MLModelId'
    DataSourceId = 'DataSourceId'
    DataURI = 'DataURI'


class GetBatchPredictionInput(BaseModel):
    BatchPredictionId: EntityId


class GetEvaluationInput(BaseModel):
    EvaluationId: EntityId


class IdempotentParameterMismatchException(RootModel[Any]):
    root: Any


class IntegerType(RootModel[int]):
    root: int = Field(..., description='Integer type that is a 32-bit signed number.')


class InternalServerException(RootModel[Any]):
    root: Any


class InvalidInputException(RootModel[Any]):
    root: Any


class InvalidTagException(RootModel[Any]):
    root: Any


class Label(RootModel[constr(min_length=1)]):
    root: constr(min_length=1)


class LimitExceededException(RootModel[Any]):
    root: Any


class LongType(RootModel[int]):
    root: int = Field(
        ..., description='Long integer type that is a 64-bit signed number.'
    )


class MLModelFilterVariable(Enum):
    CreatedAt = 'CreatedAt'
    LastUpdatedAt = 'LastUpdatedAt'
    Status = 'Status'
    Name = 'Name'
    IAMUser = 'IAMUser'
    TrainingDataSourceId = 'TrainingDataSourceId'
    RealtimeEndpointStatus = 'RealtimeEndpointStatus'
    MLModelType = 'MLModelType'
    Algorithm = 'Algorithm'
    TrainingDataURI = 'TrainingDataURI'


class MLModelName(RootModel[constr(max_length=1024)]):
    root: constr(max_length=1024)


class MLModelType(Enum):
    REGRESSION = 'REGRESSION'
    BINARY = 'BINARY'
    MULTICLASS = 'MULTICLASS'


class Message(RootModel[constr(max_length=10240)]):
    root: constr(max_length=10240) = Field(
        ..., description='Description of the most recent details about an object.'
    )


class PageLimit(RootModel[conint(ge=1, le=100)]):
    root: conint(ge=1, le=100)


class PerformanceMetricsPropertyKey(RootModel[str]):
    root: str


class PerformanceMetricsPropertyValue(RootModel[str]):
    root: str


class PredictorNotMountedException(RootModel[Any]):
    root: Any


class PresignedS3Url(RootModel[str]):
    root: str


class RDSDatabaseName(RootModel[constr(min_length=1, max_length=64)]):
    root: constr(min_length=1, max_length=64) = Field(
        ..., description='The name of a database hosted on an RDS DB instance.'
    )


class RDSDatabasePassword(RootModel[constr(min_length=8, max_length=128)]):
    root: constr(min_length=8, max_length=128) = Field(
        ...,
        description='The password to be used by Amazon ML to connect to a database on an RDS DB instance. The password should have sufficient permissions to execute the <code>RDSSelectQuery</code> query.',
    )


class RDSDatabaseUsername(RootModel[constr(min_length=1, max_length=128)]):
    root: constr(min_length=1, max_length=128) = Field(
        ...,
        description='The username to be used by Amazon ML to connect to database on an Amazon RDS instance. The username should have sufficient permissions to execute an <code>RDSSelectSqlQuery</code> query.',
    )


class RDSInstanceIdentifier(
    RootModel[constr(pattern=r'[a-z0-9-]+', min_length=1, max_length=63)]
):
    root: constr(pattern=r'[a-z0-9-]+', min_length=1, max_length=63) = Field(
        ..., description='Identifier of RDS DB Instances.'
    )


class RDSSelectSqlQuery(RootModel[constr(min_length=1, max_length=16777216)]):
    root: constr(min_length=1, max_length=16777216) = Field(
        ...,
        description='The SQL query to be executed against the Amazon RDS database. The SQL query should be valid for the Amazon RDS type being used.',
    )


class RealtimeEndpointStatus(Enum):
    NONE = 'NONE'
    READY = 'READY'
    UPDATING = 'UPDATING'
    FAILED = 'FAILED'


class Recipe(RootModel[constr(max_length=131071)]):
    root: constr(max_length=131071)


class RedshiftClusterIdentifier(
    RootModel[constr(pattern=r'[a-z0-9-]+', min_length=1, max_length=63)]
):
    root: constr(pattern=r'[a-z0-9-]+', min_length=1, max_length=63) = Field(
        ..., description='The ID of an Amazon Redshift cluster.'
    )


class RedshiftDatabaseName(
    RootModel[constr(pattern=r'[a-z0-9]+', min_length=1, max_length=64)]
):
    root: constr(pattern=r'[a-z0-9]+', min_length=1, max_length=64) = Field(
        ..., description='The name of a database hosted on an Amazon Redshift cluster.'
    )


class RedshiftDatabasePassword(RootModel[constr(min_length=8, max_length=64)]):
    root: constr(min_length=8, max_length=64) = Field(
        ...,
        description='A password to be used by Amazon ML to connect to a database on an Amazon Redshift cluster. The password should have sufficient permissions to execute a <code>RedshiftSelectSqlQuery</code> query. The password should be valid for an Amazon Redshift <a href="https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_USER.html">USER</a>.',
    )


class RedshiftDatabaseUsername(RootModel[constr(min_length=1, max_length=128)]):
    root: constr(min_length=1, max_length=128) = Field(
        ...,
        description='A username to be used by Amazon Machine Learning (Amazon ML)to connect to a database on an Amazon Redshift cluster. The username should have sufficient permissions to execute the <code>RedshiftSelectSqlQuery</code> query. The username should be valid for an Amazon Redshift <a href="https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_USER.html">USER</a>.',
    )


class RedshiftSelectSqlQuery(RootModel[constr(min_length=1, max_length=16777216)]):
    root: constr(min_length=1, max_length=16777216) = Field(
        ...,
        description=' Describes the SQL query to execute on the Amazon Redshift database. The SQL query should be valid for an Amazon Redshift <a href="https://docs.aws.amazon.com/redshift/latest/dg/r_SELECT_synopsis.html">SELECT</a>. ',
    )


class ResourceNotFoundException(RootModel[Any]):
    root: Any


class RoleARN(RootModel[constr(min_length=1, max_length=110)]):
    root: constr(min_length=1, max_length=110) = Field(
        ...,
        description='The Amazon Resource Name (ARN) of an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/roles-toplevel.html#roles-about-termsandconcepts">AWS IAM Role</a>, such as the following: arn:aws:iam::account:role/rolename. ',
    )


class S3Url(RootModel[constr(pattern=r's3://([^/]+)(/.*)?', max_length=2048)]):
    root: constr(pattern=r's3://([^/]+)(/.*)?', max_length=2048) = Field(
        ...,
        description='A reference to a file or bucket on Amazon Simple Storage Service (Amazon S3).',
    )


class ScoreThreshold(RootModel[float]):
    root: float


class ScoreValue(RootModel[float]):
    root: float


class ScoreValuePerLabelMap(RootModel[Optional[Dict[str, ScoreValue]]]):
    root: Optional[Dict[str, ScoreValue]] = None


class SortOrder(Enum):
    asc = 'asc'
    dsc = 'dsc'


class StringType(RootModel[str]):
    root: str = Field(..., description='String type.')


class TagKey(
    RootModel[
        constr(pattern=r'^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$', min_length=1, max_length=128)
    ]
):
    root: constr(
        pattern=r'^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$', min_length=1, max_length=128
    )


class TagKeyList(RootModel[List[TagKey]]):
    root: List[TagKey] = Field(..., max_length=100)


class TagLimitExceededException(RootModel[Any]):
    root: Any


class TagValue(
    RootModel[
        constr(pattern=r'^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$', min_length=0, max_length=256)
    ]
):
    root: constr(
        pattern=r'^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$', min_length=0, max_length=256
    )


class TaggableResourceType(Enum):
    BatchPrediction = 'BatchPrediction'
    DataSource = 'DataSource'
    Evaluation = 'Evaluation'
    MLModel = 'MLModel'


class TrainingParameters(RootModel[Optional[Dict[str, StringType]]]):
    root: Optional[Dict[str, StringType]] = None


class UpdateBatchPredictionInput(BaseModel):
    BatchPredictionId: EntityId
    BatchPredictionName: EntityName


class UpdateBatchPredictionOutput(BaseModel):
    BatchPredictionId: Optional[EntityId] = None


class UpdateDataSourceInput(BaseModel):
    DataSourceId: EntityId
    DataSourceName: EntityName


class UpdateDataSourceOutput(BaseModel):
    DataSourceId: Optional[EntityId] = None


class UpdateEvaluationInput(BaseModel):
    EvaluationId: EntityId
    EvaluationName: EntityName


class UpdateEvaluationOutput(BaseModel):
    EvaluationId: Optional[EntityId] = None


class UpdateMLModelInput(BaseModel):
    MLModelId: EntityId
    MLModelName: Optional[EntityName] = None
    ScoreThreshold_1: Optional[ScoreThreshold] = Field(None, alias='ScoreThreshold')


class UpdateMLModelOutput(BaseModel):
    MLModelId: Optional[EntityId] = None


class VariableName(RootModel[str]):
    root: str = Field(
        ...,
        description="The name of a variable. Currently it's used to specify the name of the target value, label, weight, and tags.",
    )


class VariableValue(RootModel[str]):
    root: str = Field(
        ...,
        description="The value of a variable. Currently it's used to specify values of the target value, weights, and tag variables and for filtering variable values.",
    )


class Verbose(RootModel[bool]):
    root: bool = Field(
        ...,
        description='Specifies whether a describe operation should return exhaustive or abbreviated information.',
    )


class VipURL(
    RootModel[
        constr(
            pattern=r'https://[a-zA-Z0-9-.]*\.amazon(aws)?\.com[/]?', max_length=2048
        )
    ]
):
    root: constr(
        pattern=r'https://[a-zA-Z0-9-.]*\.amazon(aws)?\.com[/]?', max_length=2048
    )


class FloatLabel(RootModel[float]):
    root: float


class XAmzTarget(Enum):
    AmazonML_20141212_AddTags = 'AmazonML_20141212.AddTags'


class XAmzTarget1(Enum):
    AmazonML_20141212_CreateBatchPrediction = 'AmazonML_20141212.CreateBatchPrediction'


class XAmzTarget2(Enum):
    AmazonML_20141212_CreateDataSourceFromRDS = (
        'AmazonML_20141212.CreateDataSourceFromRDS'
    )


class XAmzTarget3(Enum):
    AmazonML_20141212_CreateDataSourceFromRedshift = (
        'AmazonML_20141212.CreateDataSourceFromRedshift'
    )


class XAmzTarget4(Enum):
    AmazonML_20141212_CreateDataSourceFromS3 = (
        'AmazonML_20141212.CreateDataSourceFromS3'
    )


class XAmzTarget5(Enum):
    AmazonML_20141212_CreateEvaluation = 'AmazonML_20141212.CreateEvaluation'


class XAmzTarget6(Enum):
    AmazonML_20141212_CreateMLModel = 'AmazonML_20141212.CreateMLModel'


class XAmzTarget7(Enum):
    AmazonML_20141212_CreateRealtimeEndpoint = (
        'AmazonML_20141212.CreateRealtimeEndpoint'
    )


class XAmzTarget8(Enum):
    AmazonML_20141212_DeleteBatchPrediction = 'AmazonML_20141212.DeleteBatchPrediction'


class XAmzTarget9(Enum):
    AmazonML_20141212_DeleteDataSource = 'AmazonML_20141212.DeleteDataSource'


class XAmzTarget10(Enum):
    AmazonML_20141212_DeleteEvaluation = 'AmazonML_20141212.DeleteEvaluation'


class XAmzTarget11(Enum):
    AmazonML_20141212_DeleteMLModel = 'AmazonML_20141212.DeleteMLModel'


class XAmzTarget12(Enum):
    AmazonML_20141212_DeleteRealtimeEndpoint = (
        'AmazonML_20141212.DeleteRealtimeEndpoint'
    )


class XAmzTarget13(Enum):
    AmazonML_20141212_DeleteTags = 'AmazonML_20141212.DeleteTags'


class XAmzTarget14(Enum):
    AmazonML_20141212_DescribeBatchPredictions = (
        'AmazonML_20141212.DescribeBatchPredictions'
    )


class XAmzTarget15(Enum):
    AmazonML_20141212_DescribeDataSources = 'AmazonML_20141212.DescribeDataSources'


class XAmzTarget16(Enum):
    AmazonML_20141212_DescribeEvaluations = 'AmazonML_20141212.DescribeEvaluations'


class XAmzTarget17(Enum):
    AmazonML_20141212_DescribeMLModels = 'AmazonML_20141212.DescribeMLModels'


class XAmzTarget18(Enum):
    AmazonML_20141212_DescribeTags = 'AmazonML_20141212.DescribeTags'


class XAmzTarget19(Enum):
    AmazonML_20141212_GetBatchPrediction = 'AmazonML_20141212.GetBatchPrediction'


class XAmzTarget20(Enum):
    AmazonML_20141212_GetDataSource = 'AmazonML_20141212.GetDataSource'


class XAmzTarget21(Enum):
    AmazonML_20141212_GetEvaluation = 'AmazonML_20141212.GetEvaluation'


class XAmzTarget22(Enum):
    AmazonML_20141212_GetMLModel = 'AmazonML_20141212.GetMLModel'


class XAmzTarget23(Enum):
    AmazonML_20141212_Predict = 'AmazonML_20141212.Predict'


class XAmzTarget24(Enum):
    AmazonML_20141212_UpdateBatchPrediction = 'AmazonML_20141212.UpdateBatchPrediction'


class XAmzTarget25(Enum):
    AmazonML_20141212_UpdateDataSource = 'AmazonML_20141212.UpdateDataSource'


class XAmzTarget26(Enum):
    AmazonML_20141212_UpdateEvaluation = 'AmazonML_20141212.UpdateEvaluation'


class XAmzTarget27(Enum):
    AmazonML_20141212_UpdateMLModel = 'AmazonML_20141212.UpdateMLModel'


class AddTagsOutput(BaseModel):
    ResourceId: Optional[EntityId] = None
    ResourceType: Optional[TaggableResourceType] = None


class BatchPrediction(BaseModel):
    BatchPredictionDataSourceId: Optional[EntityId] = None
    BatchPredictionId: Optional[EntityId] = None
    ComputeTime: Optional[LongType] = None
    CreatedAt: Optional[EpochTime] = None
    CreatedByIamUser: Optional[AwsUserArn] = None
    FinishedAt: Optional[EpochTime] = None
    InputDataLocationS3: Optional[S3Url] = None
    InvalidRecordCount: Optional[LongType] = None
    LastUpdatedAt: Optional[EpochTime] = None
    MLModelId: Optional[EntityId] = None
    Message_1: Optional[Message] = Field(None, alias='Message')
    Name: Optional[EntityName] = None
    OutputUri: Optional[S3Url] = None
    StartedAt: Optional[EpochTime] = None
    Status: Optional[EntityStatus] = None
    TotalRecordCount: Optional[LongType] = None


class BatchPredictions(RootModel[List[BatchPrediction]]):
    root: List[BatchPrediction]


class CreateBatchPredictionInput(BaseModel):
    BatchPredictionDataSourceId: EntityId
    BatchPredictionId: EntityId
    BatchPredictionName: Optional[EntityName] = None
    MLModelId: EntityId
    OutputUri: S3Url


class CreateBatchPredictionOutput(BaseModel):
    BatchPredictionId: Optional[EntityId] = None


class CreateDataSourceFromRDSOutput(BaseModel):
    DataSourceId: Optional[EntityId] = None


class CreateDataSourceFromRedshiftOutput(BaseModel):
    DataSourceId: Optional[EntityId] = None


class CreateDataSourceFromS3Output(BaseModel):
    DataSourceId: Optional[EntityId] = None


class CreateEvaluationInput(BaseModel):
    EvaluationDataSourceId: EntityId
    EvaluationId: EntityId
    EvaluationName: Optional[EntityName] = None
    MLModelId: EntityId


class CreateEvaluationOutput(BaseModel):
    EvaluationId: Optional[EntityId] = None


class CreateMLModelInput(BaseModel):
    MLModelId: EntityId
    MLModelName: Optional[EntityName] = None
    MLModelType_1: MLModelType = Field(..., alias='MLModelType')
    Parameters: Optional[TrainingParameters] = None
    Recipe_1: Optional[Recipe] = Field(None, alias='Recipe')
    RecipeUri: Optional[S3Url] = None
    TrainingDataSourceId: EntityId


class CreateMLModelOutput(BaseModel):
    MLModelId: Optional[EntityId] = None


class CreateRealtimeEndpointInput(BaseModel):
    MLModelId: EntityId


class DeleteBatchPredictionInput(BaseModel):
    BatchPredictionId: EntityId


class DeleteBatchPredictionOutput(BaseModel):
    BatchPredictionId: Optional[EntityId] = None


class DeleteDataSourceInput(BaseModel):
    DataSourceId: EntityId


class DeleteDataSourceOutput(BaseModel):
    DataSourceId: Optional[EntityId] = None


class DeleteEvaluationInput(BaseModel):
    EvaluationId: EntityId


class DeleteEvaluationOutput(BaseModel):
    EvaluationId: Optional[EntityId] = None


class DeleteMLModelInput(BaseModel):
    MLModelId: EntityId


class DeleteMLModelOutput(BaseModel):
    MLModelId: Optional[EntityId] = None


class DeleteRealtimeEndpointInput(BaseModel):
    MLModelId: EntityId


class DeleteTagsInput(BaseModel):
    ResourceId: EntityId
    ResourceType: TaggableResourceType
    TagKeys: TagKeyList


class DeleteTagsOutput(BaseModel):
    ResourceId: Optional[EntityId] = None
    ResourceType: Optional[TaggableResourceType] = None


class DescribeBatchPredictionsInput(BaseModel):
    EQ: Optional[ComparatorValue] = None
    FilterVariable: Optional[BatchPredictionFilterVariable] = None
    GE: Optional[ComparatorValue] = None
    GT: Optional[ComparatorValue] = None
    LE: Optional[ComparatorValue] = None
    LT: Optional[ComparatorValue] = None
    Limit: Optional[PageLimit] = None
    NE: Optional[ComparatorValue] = None
    NextToken: Optional[StringType] = None
    Prefix: Optional[ComparatorValue] = None
    SortOrder_1: Optional[SortOrder] = Field(None, alias='SortOrder')


class DescribeBatchPredictionsOutput(BaseModel):
    NextToken: Optional[StringType] = None
    Results: Optional[BatchPredictions] = None


class DescribeDataSourcesInput(BaseModel):
    EQ: Optional[ComparatorValue] = None
    FilterVariable: Optional[DataSourceFilterVariable] = None
    GE: Optional[ComparatorValue] = None
    GT: Optional[ComparatorValue] = None
    LE: Optional[ComparatorValue] = None
    LT: Optional[ComparatorValue] = None
    Limit: Optional[PageLimit] = None
    NE: Optional[ComparatorValue] = None
    NextToken: Optional[StringType] = None
    Prefix: Optional[ComparatorValue] = None
    SortOrder_1: Optional[SortOrder] = Field(None, alias='SortOrder')


class DescribeEvaluationsInput(BaseModel):
    EQ: Optional[ComparatorValue] = None
    FilterVariable: Optional[EvaluationFilterVariable] = None
    GE: Optional[ComparatorValue] = None
    GT: Optional[ComparatorValue] = None
    LE: Optional[ComparatorValue] = None
    LT: Optional[ComparatorValue] = None
    Limit: Optional[PageLimit] = None
    NE: Optional[ComparatorValue] = None
    NextToken: Optional[StringType] = None
    Prefix: Optional[ComparatorValue] = None
    SortOrder_1: Optional[SortOrder] = Field(None, alias='SortOrder')


class DescribeMLModelsInput(BaseModel):
    EQ: Optional[ComparatorValue] = None
    FilterVariable: Optional[MLModelFilterVariable] = None
    GE: Optional[ComparatorValue] = None
    GT: Optional[ComparatorValue] = None
    LE: Optional[ComparatorValue] = None
    LT: Optional[ComparatorValue] = None
    Limit: Optional[PageLimit] = None
    NE: Optional[ComparatorValue] = None
    NextToken: Optional[StringType] = None
    Prefix: Optional[ComparatorValue] = None
    SortOrder_1: Optional[SortOrder] = Field(None, alias='SortOrder')


class DescribeTagsInput(BaseModel):
    ResourceId: EntityId
    ResourceType: TaggableResourceType


class DetailsMap(RootModel[Optional[Dict[str, DetailsValue]]]):
    root: Optional[Dict[str, DetailsValue]] = None


class GetBatchPredictionOutput(BaseModel):
    BatchPredictionDataSourceId: Optional[EntityId] = None
    BatchPredictionId: Optional[EntityId] = None
    ComputeTime: Optional[LongType] = None
    CreatedAt: Optional[EpochTime] = None
    CreatedByIamUser: Optional[AwsUserArn] = None
    FinishedAt: Optional[EpochTime] = None
    InputDataLocationS3: Optional[S3Url] = None
    InvalidRecordCount: Optional[LongType] = None
    LastUpdatedAt: Optional[EpochTime] = None
    LogUri: Optional[PresignedS3Url] = None
    MLModelId: Optional[EntityId] = None
    Message_1: Optional[Message] = Field(None, alias='Message')
    Name: Optional[EntityName] = None
    OutputUri: Optional[S3Url] = None
    StartedAt: Optional[EpochTime] = None
    Status: Optional[EntityStatus] = None
    TotalRecordCount: Optional[LongType] = None


class GetDataSourceInput(BaseModel):
    DataSourceId: EntityId
    Verbose_1: Optional[Verbose] = Field(None, alias='Verbose')


class GetMLModelInput(BaseModel):
    MLModelId: EntityId
    Verbose_1: Optional[Verbose] = Field(None, alias='Verbose')


class PerformanceMetricsProperties(
    RootModel[Optional[Dict[str, PerformanceMetricsPropertyValue]]]
):
    root: Optional[Dict[str, PerformanceMetricsPropertyValue]] = None


class Prediction(BaseModel):
    details: Optional[DetailsMap] = None
    predictedLabel: Optional[Label] = None
    predictedScores: Optional[ScoreValuePerLabelMap] = None
    predictedValue: Optional[FloatLabel] = None


class RDSDatabase(BaseModel):
    DatabaseName: RDSDatabaseName
    InstanceIdentifier: RDSInstanceIdentifier


class RDSDatabaseCredentials(BaseModel):
    Password: RDSDatabasePassword
    Username: RDSDatabaseUsername


class RDSMetadata(BaseModel):
    DataPipelineId: Optional[EDPPipelineId] = None
    Database: Optional[RDSDatabase] = None
    DatabaseUserName: Optional[RDSDatabaseUsername] = None
    ResourceRole: Optional[EDPResourceRole] = None
    SelectSqlQuery: Optional[RDSSelectSqlQuery] = None
    ServiceRole: Optional[EDPServiceRole] = None


class RealtimeEndpointInfo(BaseModel):
    CreatedAt: Optional[EpochTime] = None
    EndpointStatus: Optional[RealtimeEndpointStatus] = None
    EndpointUrl: Optional[VipURL] = None
    PeakRequestsPerSecond: Optional[IntegerType] = None


class Record(RootModel[Optional[Dict[str, VariableValue]]]):
    root: Optional[Dict[str, VariableValue]] = None


class RedshiftDatabase(BaseModel):
    ClusterIdentifier: RedshiftClusterIdentifier
    DatabaseName: RedshiftDatabaseName


class RedshiftDatabaseCredentials(BaseModel):
    Password: RedshiftDatabasePassword
    Username: RedshiftDatabaseUsername


class RedshiftMetadata(BaseModel):
    DatabaseUserName: Optional[RedshiftDatabaseUsername] = None
    RedshiftDatabase_1: Optional[RedshiftDatabase] = Field(
        None, alias='RedshiftDatabase'
    )
    SelectSqlQuery: Optional[RedshiftSelectSqlQuery] = None


class S3DataSpec(BaseModel):
    DataLocationS3: S3Url
    DataRearrangement_1: Optional[DataRearrangement] = Field(
        None, alias='DataRearrangement'
    )
    DataSchema_1: Optional[DataSchema] = Field(None, alias='DataSchema')
    DataSchemaLocationS3: Optional[S3Url] = None


class Tag(BaseModel):
    Key: Optional[TagKey] = None
    Value: Optional[TagValue] = None


class TagList(RootModel[List[Tag]]):
    root: List[Tag] = Field(..., max_length=100)


class AddTagsInput(BaseModel):
    ResourceId: EntityId
    ResourceType: TaggableResourceType
    Tags: TagList


class CreateDataSourceFromS3Input(BaseModel):
    ComputeStatistics_1: Optional[ComputeStatistics] = Field(
        None, alias='ComputeStatistics'
    )
    DataSourceId: EntityId
    DataSourceName: Optional[EntityName] = None
    DataSpec: S3DataSpec


class CreateRealtimeEndpointOutput(BaseModel):
    MLModelId: Optional[EntityId] = None
    RealtimeEndpointInfo_1: Optional[RealtimeEndpointInfo] = Field(
        None, alias='RealtimeEndpointInfo'
    )


class DataSource(BaseModel):
    ComputeStatistics_1: Optional[ComputeStatistics] = Field(
        None, alias='ComputeStatistics'
    )
    ComputeTime: Optional[LongType] = None
    CreatedAt: Optional[EpochTime] = None
    CreatedByIamUser: Optional[AwsUserArn] = None
    DataLocationS3: Optional[S3Url] = None
    DataRearrangement_1: Optional[DataRearrangement] = Field(
        None, alias='DataRearrangement'
    )
    DataSizeInBytes: Optional[LongType] = None
    DataSourceId: Optional[EntityId] = None
    FinishedAt: Optional[EpochTime] = None
    LastUpdatedAt: Optional[EpochTime] = None
    Message_1: Optional[Message] = Field(None, alias='Message')
    Name: Optional[EntityName] = None
    NumberOfFiles: Optional[LongType] = None
    RDSMetadata_1: Optional[RDSMetadata] = Field(None, alias='RDSMetadata')
    RedshiftMetadata_1: Optional[RedshiftMetadata] = Field(
        None, alias='RedshiftMetadata'
    )
    RoleARN_1: Optional[RoleARN] = Field(None, alias='RoleARN')
    StartedAt: Optional[EpochTime] = None
    Status: Optional[EntityStatus] = None


class DataSources(RootModel[List[DataSource]]):
    root: List[DataSource]


class DeleteRealtimeEndpointOutput(BaseModel):
    MLModelId: Optional[EntityId] = None
    RealtimeEndpointInfo_1: Optional[RealtimeEndpointInfo] = Field(
        None, alias='RealtimeEndpointInfo'
    )


class DescribeDataSourcesOutput(BaseModel):
    NextToken: Optional[StringType] = None
    Results: Optional[DataSources] = None


class DescribeTagsOutput(BaseModel):
    ResourceId: Optional[EntityId] = None
    ResourceType: Optional[TaggableResourceType] = None
    Tags: Optional[TagList] = None


class GetDataSourceOutput(BaseModel):
    ComputeStatistics_1: Optional[ComputeStatistics] = Field(
        None, alias='ComputeStatistics'
    )
    ComputeTime: Optional[LongType] = None
    CreatedAt: Optional[EpochTime] = None
    CreatedByIamUser: Optional[AwsUserArn] = None
    DataLocationS3: Optional[S3Url] = None
    DataRearrangement_1: Optional[DataRearrangement] = Field(
        None, alias='DataRearrangement'
    )
    DataSizeInBytes: Optional[LongType] = None
    DataSourceId: Optional[EntityId] = None
    DataSourceSchema: Optional[DataSchema] = None
    FinishedAt: Optional[EpochTime] = None
    LastUpdatedAt: Optional[EpochTime] = None
    LogUri: Optional[PresignedS3Url] = None
    Message_1: Optional[Message] = Field(None, alias='Message')
    Name: Optional[EntityName] = None
    NumberOfFiles: Optional[LongType] = None
    RDSMetadata_1: Optional[RDSMetadata] = Field(None, alias='RDSMetadata')
    RedshiftMetadata_1: Optional[RedshiftMetadata] = Field(
        None, alias='RedshiftMetadata'
    )
    RoleARN_1: Optional[RoleARN] = Field(None, alias='RoleARN')
    StartedAt: Optional[EpochTime] = None
    Status: Optional[EntityStatus] = None


class GetMLModelOutput(BaseModel):
    ComputeTime: Optional[LongType] = None
    CreatedAt: Optional[EpochTime] = None
    CreatedByIamUser: Optional[AwsUserArn] = None
    EndpointInfo: Optional[RealtimeEndpointInfo] = None
    FinishedAt: Optional[EpochTime] = None
    InputDataLocationS3: Optional[S3Url] = None
    LastUpdatedAt: Optional[EpochTime] = None
    LogUri: Optional[PresignedS3Url] = None
    MLModelId: Optional[EntityId] = None
    MLModelType_1: Optional[MLModelType] = Field(None, alias='MLModelType')
    Message_1: Optional[Message] = Field(None, alias='Message')
    Name: Optional[MLModelName] = None
    Recipe_1: Optional[Recipe] = Field(None, alias='Recipe')
    Schema: Optional[DataSchema] = None
    ScoreThreshold_1: Optional[ScoreThreshold] = Field(None, alias='ScoreThreshold')
    ScoreThresholdLastUpdatedAt: Optional[EpochTime] = None
    SizeInBytes: Optional[LongType] = None
    StartedAt: Optional[EpochTime] = None
    Status: Optional[EntityStatus] = None
    TrainingDataSourceId: Optional[EntityId] = None
    TrainingParameters_1: Optional[TrainingParameters] = Field(
        None, alias='TrainingParameters'
    )


class MLModel(BaseModel):
    Algorithm_1: Optional[Algorithm] = Field(None, alias='Algorithm')
    ComputeTime: Optional[LongType] = None
    CreatedAt: Optional[EpochTime] = None
    CreatedByIamUser: Optional[AwsUserArn] = None
    EndpointInfo: Optional[RealtimeEndpointInfo] = None
    FinishedAt: Optional[EpochTime] = None
    InputDataLocationS3: Optional[S3Url] = None
    LastUpdatedAt: Optional[EpochTime] = None
    MLModelId: Optional[EntityId] = None
    MLModelType_1: Optional[MLModelType] = Field(None, alias='MLModelType')
    Message_1: Optional[Message] = Field(None, alias='Message')
    Name: Optional[MLModelName] = None
    ScoreThreshold_1: Optional[ScoreThreshold] = Field(None, alias='ScoreThreshold')
    ScoreThresholdLastUpdatedAt: Optional[EpochTime] = None
    SizeInBytes: Optional[LongType] = None
    StartedAt: Optional[EpochTime] = None
    Status: Optional[EntityStatus] = None
    TrainingDataSourceId: Optional[EntityId] = None
    TrainingParameters_1: Optional[TrainingParameters] = Field(
        None, alias='TrainingParameters'
    )


class MLModels(RootModel[List[MLModel]]):
    root: List[MLModel]


class PerformanceMetrics(BaseModel):
    Properties: Optional[PerformanceMetricsProperties] = None


class PredictInput(BaseModel):
    MLModelId: EntityId
    PredictEndpoint: VipURL
    Record_1: Record = Field(..., alias='Record')


class PredictOutput(BaseModel):
    Prediction_1: Optional[Prediction] = Field(None, alias='Prediction')


class RDSDataSpec(BaseModel):
    DataRearrangement_1: Optional[DataRearrangement] = Field(
        None, alias='DataRearrangement'
    )
    DataSchema_1: Optional[DataSchema] = Field(None, alias='DataSchema')
    DataSchemaUri: Optional[S3Url] = None
    DatabaseCredentials: RDSDatabaseCredentials
    DatabaseInformation: RDSDatabase
    ResourceRole: EDPResourceRole
    S3StagingLocation: S3Url
    SecurityGroupIds: EDPSecurityGroupIds
    SelectSqlQuery: RDSSelectSqlQuery
    ServiceRole: EDPServiceRole
    SubnetId: EDPSubnetId


class RedshiftDataSpec(BaseModel):
    DataRearrangement_1: Optional[DataRearrangement] = Field(
        None, alias='DataRearrangement'
    )
    DataSchema_1: Optional[DataSchema] = Field(None, alias='DataSchema')
    DataSchemaUri: Optional[S3Url] = None
    DatabaseCredentials: RedshiftDatabaseCredentials
    DatabaseInformation: RedshiftDatabase
    S3StagingLocation: S3Url
    SelectSqlQuery: RedshiftSelectSqlQuery


class CreateDataSourceFromRDSInput(BaseModel):
    ComputeStatistics_1: Optional[ComputeStatistics] = Field(
        None, alias='ComputeStatistics'
    )
    DataSourceId: EntityId
    DataSourceName: Optional[EntityName] = None
    RDSData: RDSDataSpec
    RoleARN_1: RoleARN = Field(..., alias='RoleARN')


class CreateDataSourceFromRedshiftInput(BaseModel):
    ComputeStatistics_1: Optional[ComputeStatistics] = Field(
        None, alias='ComputeStatistics'
    )
    DataSourceId: EntityId
    DataSourceName: Optional[EntityName] = None
    DataSpec: RedshiftDataSpec
    RoleARN_1: RoleARN = Field(..., alias='RoleARN')


class DescribeMLModelsOutput(BaseModel):
    NextToken: Optional[StringType] = None
    Results: Optional[MLModels] = None


class Evaluation(BaseModel):
    ComputeTime: Optional[LongType] = None
    CreatedAt: Optional[EpochTime] = None
    CreatedByIamUser: Optional[AwsUserArn] = None
    EvaluationDataSourceId: Optional[EntityId] = None
    EvaluationId: Optional[EntityId] = None
    FinishedAt: Optional[EpochTime] = None
    InputDataLocationS3: Optional[S3Url] = None
    LastUpdatedAt: Optional[EpochTime] = None
    MLModelId: Optional[EntityId] = None
    Message_1: Optional[Message] = Field(None, alias='Message')
    Name: Optional[EntityName] = None
    PerformanceMetrics_1: Optional[PerformanceMetrics] = Field(
        None, alias='PerformanceMetrics'
    )
    StartedAt: Optional[EpochTime] = None
    Status: Optional[EntityStatus] = None


class Evaluations(RootModel[List[Evaluation]]):
    root: List[Evaluation]


class GetEvaluationOutput(BaseModel):
    ComputeTime: Optional[LongType] = None
    CreatedAt: Optional[EpochTime] = None
    CreatedByIamUser: Optional[AwsUserArn] = None
    EvaluationDataSourceId: Optional[EntityId] = None
    EvaluationId: Optional[EntityId] = None
    FinishedAt: Optional[EpochTime] = None
    InputDataLocationS3: Optional[S3Url] = None
    LastUpdatedAt: Optional[EpochTime] = None
    LogUri: Optional[PresignedS3Url] = None
    MLModelId: Optional[EntityId] = None
    Message_1: Optional[Message] = Field(None, alias='Message')
    Name: Optional[EntityName] = None
    PerformanceMetrics_1: Optional[PerformanceMetrics] = Field(
        None, alias='PerformanceMetrics'
    )
    StartedAt: Optional[EpochTime] = None
    Status: Optional[EntityStatus] = None


class DescribeEvaluationsOutput(BaseModel):
    NextToken: Optional[StringType] = None
    Results: Optional[Evaluations] = None
