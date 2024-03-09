import json
import pickle
import uuid

import string
import random
import pandas
import wizata_dsapi
from enum import Enum

from .dataframe_toolkit import df_to_json, df_from_json
from .api_dto import ApiDto
from .ds_dataframe import DSDataFrame
from .mlmodel import MLModel
from .plot import Plot
from .request import Request
from .script import Script
from .pipeline import Pipeline
from .experiment import Experiment


class AbortedException(Exception):
    pass


class ExecutionStatus(Enum):
    RECEIVED = "received"
    QUEUED = "queued"
    STARTED = "started"
    COMPLETED = "completed"
    FAILED = "failed"
    ABORTED = "aborted"


class ExecutionStepLog(ApiDto):
    """
    Execution Step Log defining an results and status of pipeline step execution.
    """

    def __init__(self, execution_step_log_id=None, step_id=None, execution_id=None, content=None, status=None):
        if execution_step_log_id is None:
            execution_step_log_id = uuid.uuid4()
        self.execution_step_log_id = execution_step_log_id
        self.execution_id = execution_id
        self.step_id = step_id
        self.content = content
        self.status = status
        self.createdById = None
        self.createdDate = None
        self.updatedById = None
        self.updatedDate = None

    def api_id(self) -> str:
        """
        Id of the execution (execution_step_log_id)
        :return: string formatted UUID of the Execution.
        """
        return str(self.execution_step_log_id).upper()

    def endpoint(self) -> str:
        """
        Name of the endpoints used to manipulate execution.
        :return: Endpoint name.
        """
        return "ExecutionStepLogs"

    def to_json(self, target: str = None):
        """
        Convert to a json version of Execution definition.
        By default, use DS API format.
        """
        obj = {
            "id": str(self.execution_step_log_id)
        }
        if self.execution_id is not None:
            obj["executionId"] = str(self.execution_id)
        if self.step_id is not None:
            obj["stepId"] = str(self.step_id)
        if self.content is not None:
            obj["content"] = json.dumps(self.content)
        if self.createdById is not None:
            obj["createdById"] = self.createdById
        if self.createdDate is not None:
            obj["createdDate"] = self.createdDate
        if self.updatedById is not None:
            obj["updatedById"] = self.updatedById
        if self.updatedDate is not None:
            obj["updatedDate"] = self.updatedDate
        if self.status is not None and isinstance(self.status, ExecutionStatus):
            obj["status"] = self.status.value
        return obj

    def from_json(self, obj):
        """
        Load an execution from a stored JSON model.
        :param obj: dictionary representing an execution.
        """
        if "id" in obj.keys():
            self.execution_step_log_id = uuid.UUID(obj["id"])
        if "executionId" in obj.keys() and obj["executionId"] is not None:
            self.execution_id = uuid.UUID(obj["executionId"])
        if "stepId" in obj.keys() and obj["stepId"] is not None:
            self.step_id = uuid.UUID(obj["stepId"])
        if "content" in obj.keys() and obj["content"] is not None:
            if isinstance(obj["content"], str):
                self.content = json.loads(obj["content"])
            else:
                self.content = obj["content"]
        if "status" in obj.keys():
            self.status = ExecutionStatus(str(obj["status"]))
        if "createdById" in obj.keys() and obj["createdById"] is not None:
            self.createdById = obj["createdById"]
        if "createdDate" in obj.keys() and obj["createdDate"] is not None:
            self.createdDate = obj["createdDate"]
        if "updatedById" in obj.keys() and obj["updatedById"] is not None:
            self.updatedById = obj["updatedById"]
        if "updatedDate" in obj.keys() and obj["updatedDate"] is not None:
            self.updatedDate = obj["updatedDate"]


class Execution(ApiDto):
    """
    Execution Context defining an experimentation historical run.

    Execution can be run in the platform or directly within your script.
    Used also as context within a Script function, used the following method:
        - append_model - To store a generated model
        - append_plot - To store a plot
        - result_dataframe - To set the panda Dataframe as output

    :ivar execution_id: UUID of the Execution on Wizata App.
    :ivar experiment_id: UUID of the Experiment on which this Experiment is linked.
    :ivar warnings: Warning about the Execution.

    Data

    :ivar request: Request or JSON formatted object to fecth data on Wizata App.
    :ivar input_ds_dataframe: DS Dataframe containing the panda Dataframe input.
    :ivar dataframe: shortcut to Pandas DataFrame used as input.

    Inputs

    :ivar script: Script to execute against the input data.
    :ivar ml_model: Trained ML Model to use against the input data.
    :ivar function: Name of a Wizata built-in function.
    :ivar isAnomalyDetection: True if this execution triggers integrated Anomaly Detection within Wizata.
    :ivar properties: configuration and variables.

    Outputs

    :ivar models: Trained Machine Learning Models.
    :ivar plots: Figures generated with Plotly.
    :ivar anomalies: Anomalies detected.
    :ivar output_ds_dataframe: Output dataframe generated by the Script or Model.
    """

    @classmethod
    def route(cls):
        return "executions"

    @classmethod
    def from_dict(cls, data):
        obj = Execution()
        obj.from_json(data)
        return obj

    keys = [
        'target_feat',
        'sensitivity',
        'aggregations',
        'restart_filter',
        'interval'
    ]

    def __init__(self, execution_id=None, properties: dict = None, pipeline: Pipeline = None, experiment: Experiment = None):

        # Id
        if execution_id is None:
            execution_id = uuid.uuid4()
        self.execution_id = execution_id

        # Experiment
        if experiment is not None:
            self.experiment_id = experiment.experiment_id
        else:
            self.experiment_id = None

        # Inputs Properties (load)
        self.script = None
        self.request = None

        if properties is None:
            properties = {}
        self.properties = properties

        self.input_ds_dataframe = None
        self.ml_model = None
        self.function = None
        self.isAnomalyDetection = False
        self.pipeline = pipeline
        self.status = None

        # created/updated
        self.createdById = None
        self.createdDate = None
        self.updatedById = None
        self.updatedDate = None

        # telemetry
        self.started_date = None
        self.execution_time = None
        self.waiting_time = None

        # Outputs Properties (generated by Execution)
        self.models = []
        self.anomalies = []
        self.plots = []
        self.dataframes = []
        self.output_ds_dataframe = None
        self.warnings = None

    def _get_dataframe(self):
        if self.input_ds_dataframe is None:
            return None
        else:
            return self.input_ds_dataframe.dataframe

    def _set_dataframe(self, value):
        if not isinstance(value, pandas.DataFrame):
            raise ValueError("dataframe must be a panda dataframe.")
        self.input_ds_dataframe = DSDataFrame()
        self.input_ds_dataframe.dataframe = value

    def _del_dataframe(self):
        del self.input_ds_dataframe

    dataframe = property(
        fget=_get_dataframe,
        fset=_set_dataframe,
        fdel=_del_dataframe,
        doc="Input Pandas Dataframe (for id fetch 'input_ds_dataframe.df_id')"
    )

    def _get_result_dataframe(self):
        if self.output_ds_dataframe is None:
            return None
        else:
            return self.output_ds_dataframe.dataframe

    def _set_result_dataframe(self, value):
        if not isinstance(value, pandas.DataFrame):
            raise ValueError("dataframe must be a panda dataframe.")
        self.output_ds_dataframe = DSDataFrame()
        self.output_ds_dataframe.dataframe = value

    def _del_result_dataframe(self):
        del self.output_ds_dataframe

    result_dataframe = property(
        fget=_get_result_dataframe,
        fset=_set_result_dataframe,
        fdel=_del_result_dataframe,
        doc="Output Pandas Dataframe (for id fetch 'output_ds_dataframe.df_id')"
    )

    def append_plot(self, figure, name="Unkwown"):
        """
        Append a plot to the context.

        :param figure: Plotly figure.
        :param name: Name of the plot.
        :return: Plot object prepared.
        """
        plot = Plot()
        plot.name = name
        plot.experiment_id = self.experiment_id
        plot.figure = figure
        self.plots.append(plot)
        return plot

    def append_model(self, trained_model, input_columns, key=None, output_columns=None, has_anomalies=False, scaler=None):
        """
        Append a Trained ML Model to the context.

        :param key: Model key to logically identify the model - if not provided a random
        :param trained_model: Trained Model to be stored as a pickled object.
        :param input_columns: List of str defining input columns to call the model (df.columns)
        :param output_columns: List of output columns - Optional as can be detected automatically during validation.
        :param has_anomalies: False by default, define if the model set anomalies
        :param scaler: Scaler to be stored if necessary.
        :return: ML Model object prepared.
        """
        ml_model = MLModel()

        if key is None:
            key = generate_key()
        ml_model.key = key
        ml_model.trained_model = trained_model
        ml_model.scaler = scaler

        ml_model.input_columns = input_columns
        ml_model.output_columns = output_columns

        ml_model.has_anomalies = has_anomalies

        self.models.append(ml_model)
        return ml_model

    def api_id(self) -> str:
        """
        Id of the execution (execution_id)

        :return: string formatted UUID of the Execution.
        """
        return str(self.execution_id).upper()

    def endpoint(self) -> str:
        """
        Name of the endpoints used to manipulate execution.
        :return: Endpoint name.
        """
        return "Executions"

    def to_json(self, target: str = None):
        """
        Convert to a json version of Execution definition.
        By default, use DS API format.
        """
        obj = {
            "id": str(self.execution_id)
        }
        if self.experiment_id is not None:
            obj["experimentId"] = str(self.experiment_id)
        if self.request is not None:
            obj["request"] = json.dumps(self.request.to_json())
        if self.properties is not None:
            obj["properties"] = json.dumps(self.properties)

        if target is None or target != '◊':
            if self.dataframe is not None:
                obj["dataframe"] = df_to_json(self.dataframe)

        if self.script is not None:
            obj["scriptId"] = str(self.script.script_id)
        if self.ml_model is not None:
            obj["mlModelId"] = str(self.ml_model.model_id)
        if self.pipeline is not None:
            obj["pipelineId"] = str(self.pipeline.pipeline_id)
            obj["pipelineJson"] = json.dumps(self.pipeline.to_json())
        if self.function is not None:
            obj["function"] = self.function
        if self.isAnomalyDetection:
            obj["isAnomalyDetection"] = str(True)
        if self.plots is not None:
            plots_ids = []
            for plot in self.plots:
                plots_ids.append(
                    {
                        "id": str(plot.plot_id)
                    }
                )
            obj["plots"] = plots_ids
        if self.models is not None:
            models_json = []
            for ml_model in self.models:
                models_json.append({"id": str(ml_model.model_id)})
            obj["models"] = models_json
        if self.anomalies is not None:
            obj["anomaliesList"] = json.dumps(self.anomalies)
        # if self.result_dataframe is not None:
        #     obj["resultDataframe"] = {
        #         "id": str(self.output_ds_dataframe.df_id)
        #     }
        if self.createdById is not None:
            obj["createdById"] = self.createdById
        if self.createdDate is not None:
            obj["createdDate"] = self.createdDate
        if self.updatedById is not None:
            obj["updatedById"] = self.updatedById
        if self.updatedDate is not None:
            obj["updatedDate"] = self.updatedDate
        if self.started_date is not None:
            obj["startedDate"] = self.started_date
        if self.execution_time is not None:
            obj["executionTime"] = self.execution_time
        if self.waiting_time is not None:
            obj["waitingTime"] = self.waiting_time
        if self.warnings is not None:
            obj["warnings"] = self.warnings
        if self.status is not None and isinstance(self.status, ExecutionStatus):
            obj["status"] = self.status.value
        return obj

    def from_json(self, obj):
        """
        Load an execution from a stored JSON model.
        :param obj: dictionnary representing an execution.
        """
        if "id" in obj.keys():
            self.execution_id = uuid.UUID(obj["id"])
        if "experimentId" in obj.keys() and obj["experimentId"] is not None:
            self.experiment_id = uuid.UUID(obj["experimentId"])
        if "request" in obj.keys() and obj["request"] is not None:
            self.request = Request()
            if isinstance(obj["request"], str):
                self.request.from_json(json.loads(obj["request"]))
                self.copy_properties(json.loads(obj["request"]))
            else:
                self.request.from_json(obj["request"])
                self.copy_properties(obj["request"])
        if "properties" in obj.keys() and obj["properties"] is not None:
            if isinstance(obj["properties"], str):
                self.add_properties(json.loads(obj["properties"]))
            else:
                self.add_properties(obj["properties"])
        if "dataframe" in obj.keys() and obj["dataframe"] is not None:
            if isinstance(obj["dataframe"], str):
                self.request.from_json(json.loads(obj["dataframe"]))
            else:
                self.dataframe = df_from_json(obj["dataframe"])
        # elif "dataframeId" in obj.keys() and obj["dataframeId"] is not None:
        #     self.input_ds_dataframe = DSDataFrame(df_id=uuid.UUID(obj["dataframeId"]))
        if "scriptId" in obj.keys() and obj["scriptId"] is not None:
            self.script = Script()
            self.script.script_id = uuid.UUID(obj["scriptId"])
        if "pipelineId" in obj.keys() and obj["pipelineId"] is not None:
            self.pipeline = Pipeline()
            if "pipelineJson" in obj.keys() and obj["pipelineJson"] is not None:
                self.pipeline.from_json(json.loads(obj["pipelineJson"]))
            self.pipeline.pipeline_id = uuid.UUID(obj["pipelineId"])
        if "mlModelId" in obj.keys() and obj["mlModelId"] is not None:
            self.ml_model = MLModel()
            self.ml_model.model_id = uuid.UUID(obj["mlModelId"])
        if "function" in obj.keys() and obj["function"] is not None:
            self.function = obj["function"]
        if "isAnomalyDetection" in obj.keys() and obj["isAnomalyDetection"] is not None:
            if isinstance(obj["isAnomalyDetection"], bool):
                self.isAnomalyDetection = obj["isAnomalyDetection"]
            else:
                self.isAnomalyDetection = obj["isAnomalyDetection"] == 'True'
        if "createdById" in obj.keys() and obj["createdById"] is not None:
            self.createdById = obj["createdById"]
        if "createdDate" in obj.keys() and obj["createdDate"] is not None:
            self.createdDate = obj["createdDate"]
        if "updatedById" in obj.keys() and obj["updatedById"] is not None:
            self.updatedById = obj["updatedById"]
        if "updatedDate" in obj.keys() and obj["updatedDate"] is not None:
            self.updatedDate = obj["updatedDate"]
        if "startedDate" in obj.keys() and obj["startedDate"] is not None:
            self.started_date = int(obj["startedDate"])
        if "waitingTime" in obj.keys() and obj["waitingTime"] is not None:
            self.waiting_time = int(obj["waitingTime"])
        if "executionTime" in obj.keys() and obj["executionTime"] is not None:
            self.execution_time = int(obj["executionTime"])
        if "warnings" in obj.keys() and obj["warnings"] is not None:
            self.warnings = obj["warnings"]
        if "anomaliesList" in obj.keys() and obj["anomaliesList"] is not None:
            if isinstance(obj["anomaliesList"], str):
                self.anomalies = json.loads(obj["anomaliesList"])
            else:
                self.anomalies = obj["anomaliesList"]
        if "status" in obj.keys():
            self.status = ExecutionStatus(str(obj["status"]))

    def to_pickle(self):
        """
        Convert the Execution to a pickle object.
        :return: Pickle object.
        """
        return pickle.dumps(self)

    def add_properties(self, obj: dict):
        """
        load properties from a dictionary

        :param obj: dictionary with potential properties
        """
        for key in obj.keys():
            if self.properties is None:
                self.properties = {}
            self.properties[key] = obj[key]

    def copy_properties(self, obj: dict):
        """
        copy properties from a dictionary originating from a Request object.
        filtering on specific properties (Execution.keys)

        :param obj: dictionary with potential properties
        """
        for key in Execution.keys:
            if key in obj:
                if self.properties is None:
                    self.properties = {}
                self.properties[key] = obj[key]

    def get_interval(self) -> int:
        """
        Determine interval from either request, properties or loaded dataframe.
        :return:
        """
        if self.request is not None:
            interval = self.request.interval
        elif self.properties['aggregations'] is not None \
                and self.properties['aggregations']['interval'] is not None:
            interval = int(self.properties["aggregations"]["interval"] / 1000)
        elif self.properties['interval'] is not None:
            interval = int(self.properties['interval'] / 1000)
        else:
            raise KeyError("No interval have been loaded - please set an interval in properties.")
        return interval


def generate_key():
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(10))
    return result_str
