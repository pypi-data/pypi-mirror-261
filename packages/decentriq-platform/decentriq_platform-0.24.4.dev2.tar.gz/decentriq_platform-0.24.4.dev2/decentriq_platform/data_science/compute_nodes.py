from dataclasses import dataclass, asdict
from enum import Enum
import json
from typing import Dict, List, Optional
from .high_level_node import ComputationNode
from .script import Script, ScriptingLanguage
from .data_nodes import ColumnDataFormat
from decentriq_dcr_compiler.schemas.data_science_data_room import (
    ScriptingComputationNode,
    SqlComputationNode,
    SqliteComputationNode,
    S3SinkComputationNode,
    MatchingComputationNode,
    SyntheticDataComputationNode,
    PreviewComputationNode,
)
from typing_extensions import Self


@dataclass
class ScriptingNodeConfig:
    """
    Class representing the configuration of a Scripting node.
    """

    main_script: Script
    dependencies: Optional[List[str]] = None
    additional_scripts: Optional[List[Script]] = None
    enable_logs_on_error: Optional[bool] = False
    enable_logs_on_success: Optional[bool] = False
    output: Optional[str] = "/output"

    @staticmethod
    def from_dict(dictionary: Dict[str, str]) -> Self:
        """
        Instantiate a `ScriptingNodeConfig` from the dictionary representation.

        **Parameters**:
        - `dictionary`: Dictionary representation of the `ScriptingNodeConfig`.
        """
        scripting_language = (
            ScriptingLanguage.python
            if dictionary["scriptingLanguage"] == "python"
            else ScriptingLanguage.r
        )
        main_script = Script(
            name=dictionary["mainScript"]["name"],
            content=dictionary["mainScript"]["content"],
            language=scripting_language,
        )
        return ScriptingNodeConfig(
            main_script=main_script,
            dependencies=dictionary["dependencies"],
            additional_scripts=dictionary["additionalScripts"],
            enable_logs_on_error=dictionary["enableLogsOnError"],
            enable_logs_on_success=dictionary["enableLogsOnSuccess"],
            output=dictionary["output"],
        )


PythonConfig = ScriptingNodeConfig


class PythonComputeNode(ComputationNode):
    """
    Class representing a Python Computation node.
    """

    def __init__(
        self,
        name: str,
        config: PythonConfig,
        analysts: List[str],
        id: Optional[str] = None,
    ) -> None:
        """
        Initialise a `PythonComputeNode`:

        **Parameters**:
        `name`: Name of the `PythonComputeNode`.
        `config`: Configuration of the `PythonComputeNode`.
        `analysts`: List of analysts for the `PythonComputeNode`.
        `id`: Optional ID of the `PythonComputeNode`. If omitted, an ID is auto generated.
        """
        language = config.main_script.get_scripting_language()
        if language != ScriptingLanguage.python:
            raise Exception(
                f"Python compute node cannot support the {language} scripting language"
            )
        super().__init__(name, analysts, id)
        self.cfg = config
        self.scripting_specification_id = "decentriq.python-ml-worker-32-64"
        self.static_content_specification_id = "decentriq.driver"

    def get_high_level_representation(self) -> Dict[str, str]:
        """
        Retrieve the high level representation of the `PythonComputeNode`.
        """
        dependencies = [] if not self.cfg.dependencies else self.cfg.dependencies
        additional_scripts = []
        if self.cfg.additional_scripts:
            additional_scripts = [
                {
                    "name": script.name,
                    "content": script.content,
                }
                for script in self.cfg.additional_scripts
            ]
        computation_node = {
            "id": self.id,
            "name": self.name,
            "kind": {
                "computation": {
                    "kind": {
                        "scripting": {
                            "additionalScripts": additional_scripts,
                            "dependencies": dependencies,
                            "enableLogsOnError": self.cfg.enable_logs_on_error,
                            "enableLogsOnSuccess": self.cfg.enable_logs_on_success,
                            "mainScript": {
                                "name": self.cfg.main_script.get_name(),
                                "content": self.cfg.main_script.get_content(),
                            },
                            "output": self.cfg.output,
                            "scriptingLanguage": self.cfg.main_script.get_scripting_language(),
                            "scriptingSpecificationId": self.scripting_specification_id,
                            "staticContentSpecificationId": self.static_content_specification_id,
                        }
                    }
                },
            },
        }
        return computation_node

    def get_computation_id(self) -> str:
        """
        Retrieve the ID of the node corresponding to the computation.
        """
        return f"{self.id}_container"

    def from_high_level(
        id: str, name: str, node: ScriptingComputationNode, analysts: List[str]
    ) -> Self:
        """
        Instantiate a `PythonComputeNode` from its high level representation.

        **Parameters**:
        - `id`: ID of the `PythonComputeNode`.
        - `name`: Name of the `PythonComputeNode`.
        - `node`: Pydantic model of the `PythonComputeNode`.
        - `analysts`: List of analysts for the `PythonComputeNode`.
        """
        config = PythonConfig.from_dict(json.loads(node.model_dump_json()))
        return PythonComputeNode(
            name=name,
            id=id,
            config=config,
            analysts=analysts,
        )


RConfig = ScriptingNodeConfig


class RComputeNode(ComputationNode):
    """
    Class representing an R Computation node.
    """

    def __init__(
        self,
        name: str,
        config: RConfig,
        analysts: List[str],
        id: Optional[str] = None,
    ) -> None:
        """
        Initialise a `RComputeNode`:

        **Parameters**:
        `name`: Name of the `RComputeNode`.
        `config`: Configuration of the `RComputeNode`.
        `analysts`: List of analysts for the `RComputeNode`.
        `id`: Optional ID of the `RComputeNode`. If omitted, an ID is auto generated.
        """
        language = config.main_script.get_scripting_language()
        if language != ScriptingLanguage.r:
            raise Exception(
                f"R compute node cannot support the {language} scripting language"
            )
        super().__init__(name, analysts, id)
        self.cfg = config
        self.scripting_specification_id = "decentriq.r-latex-worker-32-32"
        self.static_content_specification_id = "decentriq.driver"

    def get_high_level_representation(self) -> Dict[str, str]:
        """
        Retrieve the high level representation of the `RComputeNode`.
        """
        dependencies = [] if not self.cfg.dependencies else self.cfg.dependencies
        additional_scripts = []
        if self.cfg.additional_scripts:
            additional_scripts = [
                {
                    "name": script.name,
                    "content": script.content,
                }
                for script in self.cfg.additional_scripts
            ]
        computation_node = {
            "id": self.id,
            "name": self.name,
            "kind": {
                "computation": {
                    "kind": {
                        "scripting": {
                            "additionalScripts": additional_scripts,
                            "dependencies": dependencies,
                            "enableLogsOnError": self.cfg.enable_logs_on_error,
                            "enableLogsOnSuccess": self.cfg.enable_logs_on_success,
                            "mainScript": {
                                "name": self.cfg.main_script.get_name(),
                                "content": self.cfg.main_script.get_content(),
                            },
                            "output": self.cfg.output,
                            "scriptingLanguage": self.cfg.main_script.get_scripting_language(),
                            "scriptingSpecificationId": self.scripting_specification_id,
                            "staticContentSpecificationId": self.static_content_specification_id,
                        }
                    }
                },
            },
        }
        return computation_node

    def get_computation_id(self) -> str:
        """
        Retrieve the ID of the node corresponding to the computation.
        """
        return f"{self.id}_container"

    def from_high_level(
        id: str, name: str, node: ScriptingComputationNode, analysts: List[str]
    ) -> Self:
        """
        Instantiate a `RComputeNode` from its high level representation.

        **Parameters**:
        - `id`: ID of the `RComputeNode`.
        - `name`: Name of the `RComputeNode`.
        - `node`: Pydantic model of the `RComputeNode`.
        - `analysts`: List of analysts for the `RComputeNode`.
        """
        node_json = json.loads(node.model_dump_json())
        config = RConfig.from_dict(node_json)
        return RComputeNode(
            name=name,
            id=id,
            config=config,
            analysts=analysts,
        )


@dataclass
class TableMapping:
    nodeId: str
    tableName: str


@dataclass
class SqlNodeConfig:
    sql_statement: str
    dependencies: Optional[List[TableMapping]] = None
    minimum_rows_count: Optional[int] = None

    @staticmethod
    def from_dict(dictionary: Dict[str, str]) -> Self:
        """
        Instantiate a `SqlNodeConfig` from the dictionary representation.

        **Parameters**:
        - `dictionary`: Dictionary representation of the `SqlNodeConfig`.
        """
        minimum_rows_count = (
            None
            if not dictionary["privacyFilter"]
            else dictionary["privacyFilter"]["minimumRowsCount"]
        )
        return SqlNodeConfig(
            dependencies=dictionary["dependencies"],
            sql_statement=dictionary["statement"],
            minimum_rows_count=minimum_rows_count,
        )


class SqlComputeNode(ComputationNode):
    """
    Class representing an SQL Computation node.
    """

    def __init__(
        self,
        name: str,
        config: SqlNodeConfig,
        analysts: List[str],
        id: Optional[str] = None,
    ) -> None:
        """
        Initialise a `SqlComputeNode`:

        **Parameters**:
        `name`: Name of the `SqlComputeNode`.
        `config`: Configuration of the `SqlComputeNode`.
        `analysts`: List of analysts for the `SqlComputeNode`.
        `id`: Optional ID of the `SqlComputeNode`. If omitted, an ID is auto generated.
        """
        super().__init__(name, analysts, id)
        self.cfg = config
        self.specification_id = "decentriq.sql-worker"

    def get_high_level_representation(self) -> Dict[str, str]:
        """
        Retrieve the high level representation of the `SqlComputeNode`.
        """
        dependencies = []
        if self.cfg.dependencies:
            for dependency in self.cfg.dependencies:
                dependencies.append(
                    {
                        "nodeId": dependency.nodeId,
                        "tableName": dependency.tableName,
                    }
                )

        sql = {
            "dependencies": dependencies,
            "specificationId": self.specification_id,
            "statement": self.cfg.sql_statement,
        }
        if self.cfg.minimum_rows_count:
            sql["privacyFilter"]["minimumRowsCount"] = self.cfg.minimum_rows_count

        computation_node = {
            "id": self.id,
            "name": self.name,
            "kind": {
                "computation": {
                    "kind": {
                        "sql": sql,
                    }
                },
            },
        }
        return computation_node

    def get_computation_id(self) -> str:
        """
        Retrieve the ID of the node corresponding to the computation.
        """
        return self.id

    def from_high_level(
        id: str, name: str, node: SqlComputationNode, analysts: List[str]
    ) -> Self:
        """
        Instantiate a `SqlComputeNode` from its high level representation.

        **Parameters**:
        - `id`: ID of the `SqlComputeNode`.
        - `name`: Name of the `SqlComputeNode`.
        - `node`: Pydantic model of the `SqlComputeNode`.
        - `analysts`: List of analysts for the `SqlComputeNode`.
        """
        node_json = json.loads(node.model_dump_json())
        config = SqlNodeConfig.from_dict(node_json)
        return SqlComputeNode(
            name=name,
            id=id,
            config=config,
            analysts=analysts,
        )


@dataclass
class SqliteNodeConfig:
    sqlite_statement: str
    dependencies: Optional[List[TableMapping]] = None
    enable_logs_on_error: Optional[bool] = False
    enable_logs_on_success: Optional[bool] = False

    @staticmethod
    def from_dict(dictionary: Dict[str, str]) -> Self:
        """
        Instantiate a `SqliteNodeConfig` from the dictionary representation.

        **Parameters**:
        - `dictionary`: Dictionary representation of the `SqliteNodeConfig`.
        """
        return SqliteNodeConfig(
            dependencies=dictionary["dependencies"],
            sqlite_statement=dictionary["statement"],
            enable_logs_on_error=dictionary["enableLogsOnError"],
            enable_logs_on_success=dictionary["enableLogsOnSuccess"],
        )


class SqliteComputeNode(ComputationNode):
    """
    Class representing an SQLite Computation node.
    """

    def __init__(
        self,
        name: str,
        config: SqliteNodeConfig,
        analysts: List[str],
        id: Optional[str] = None,
    ) -> None:
        """
        Initialise a `SqliteComputeNode`:

        **Parameters**:
        `name`: Name of the `SqliteComputeNode`.
        `config`: Configuration of the `SqliteComputeNode`.
        `analysts`: List of analysts for the `SqliteComputeNode`.
        `id`: Optional ID of the `SqliteComputeNode`. If omitted, an ID is auto generated.
        """
        super().__init__(name, analysts, id)
        self.cfg = config
        # SQLite computations use the Python worker under the hood.
        self.specification_id = "decentriq.python-ml-worker-32-64"
        self.static_content_specification_id = "decentriq.driver"

    def get_high_level_representation(self) -> Dict[str, str]:
        """
        Retrieve the high level representation of the `SqliteComputeNode`.
        """
        dependencies = []
        if self.cfg.dependencies:
            for dependency in self.cfg.dependencies:
                dependencies.append(
                    {
                        "nodeId": dependency.nodeId,
                        "tableName": dependency.tableName,
                    }
                )
        computation_node = {
            "id": self.id,
            "name": self.name,
            "kind": {
                "computation": {
                    "kind": {
                        "sqlite": {
                            "dependencies": dependencies,
                            "enableLogsOnError": self.cfg.enable_logs_on_error,
                            "enableLogsOnSuccess": self.cfg.enable_logs_on_success,
                            "sqliteSpecificationId": self.specification_id,
                            "statement": self.cfg.sqlite_statement,
                            "staticContentSpecificationId": self.static_content_specification_id,
                        }
                    }
                },
            },
        }
        return computation_node

    def get_computation_id(self) -> str:
        """
        Retrieve the ID of the node corresponding to the computation.
        """
        return f"{self.id}_container"

    def from_high_level(
        id: str, name: str, node: SqliteComputationNode, analysts: List[str]
    ) -> Self:
        """
        Instantiate a `SqliteComputeNode` from its high level representation.

        **Parameters**:
        - `id`: ID of the `SqliteComputeNode`.
        - `name`: Name of the `SqliteComputeNode`.
        - `node`: Pydantic model of the `SqliteComputeNode`.
        - `analysts`: List of analysts for the `SqliteComputeNode`.
        """
        node_json = json.loads(node.model_dump_json())
        config = SqliteNodeConfig.from_dict(node_json)
        return SqliteComputeNode(
            name=name,
            id=id,
            config=config,
            analysts=analysts,
        )


class MaskType(str, Enum):
    GENERIC_STRING = "genericString"
    GENERIC_NUMBER = "genericNumber"
    NAME = "name"
    ADDRESS = "address"
    POSTCODE = "postcode"
    PHONE_NUMBER = "phoneNumber"
    SOCIAL_SECURITY_NUMBER = "socialSecurityNumber"
    EMAIL = "email"
    DATE = "date"
    TIMESTAMP = "timestamp"
    IBAN = "iban"


@dataclass
class SyntheticNodeColumn:
    dataFormat: ColumnDataFormat
    index: int
    maskType: MaskType
    shouldMaskColumn: bool
    name: Optional[Optional[str]] = None


@dataclass
class SyntheticNodeConfig:
    columns: List[SyntheticNodeColumn]
    dependency: str
    epsilon: float
    output_original_data_statistics: Optional[bool] = False
    enable_logs_on_error: Optional[bool] = False
    enable_logs_on_success: Optional[bool] = False

    @staticmethod
    def from_dict(dictionary: Dict[str, str]) -> Self:
        """
        Instantiate a `SyntheticNodeConfig` from the dictionary representation.

        **Parameters**:
        - `dictionary`: Dictionary representation of the `SyntheticNodeConfig`.
        """
        return SqliteNodeConfig(
            columns=dictionary["columns"],
            dependency=dictionary["dependency"],
            epsilon=dictionary["epsilon"],
            output_original_data_statistics=dictionary["outputOriginalDataStatistics"],
            enable_logs_on_error=dictionary["enableLogsOnError"],
            enable_logs_on_success=dictionary["enableLogsOnSuccess"],
        )


class SyntheticDataComputeNode(ComputationNode):
    """
    Class representing a Synthetic Data Computation node.
    """

    def __init__(
        self,
        name: str,
        config: SyntheticNodeConfig,
        analysts: List[str],
        id: Optional[str] = None,
    ) -> None:
        """
        Initialise a `SyntheticDataComputeNode`:

        **Parameters**:
        `name`: Name of the `SyntheticDataComputeNode`.
        `config`: Configuration of the `SyntheticDataComputeNode`.
        `analysts`: List of analysts for the `SyntheticDataComputeNode`.
        `id`: Optional ID of the `SyntheticDataComputeNode`. If omitted, an ID is auto generated.
        """
        super().__init__(name, analysts, id)
        self.cfg = config
        self.specification_id = "decentriq.python-synth-data-worker-32-64"
        self.static_content_specification_id = "decentriq.driver"

    def get_high_level_representation(self) -> Dict[str, str]:
        """
        Retrieve the high level representation of the `SyntheticDataComputeNode`.
        """
        columns = [asdict(column) for column in self.cfg.columns]
        computation_node = {
            "id": self.id,
            "name": self.name,
            "kind": {
                "computation": {
                    "kind": {
                        "syntheticData": {
                            "columns": columns,
                            "dependency": self.cfg.dependency,
                            "enableLogsOnError": self.cfg.enable_logs_on_error,
                            "enableLogsOnSuccess": self.cfg.enable_logs_on_success,
                            "epsilon": self.cfg.epsilon,
                            "outputOriginalDataStatistics": self.cfg.output_original_data_statistics,
                            "staticContentSpecificationId": self.static_content_specification_id,
                            "synthSpecificationId": self.specification_id,
                        }
                    }
                },
            },
        }
        return computation_node

    def get_computation_id(self) -> str:
        """
        Retrieve the ID of the node corresponding to the computation.
        """
        return f"{self.id}_container"

    def from_high_level(
        id: str, name: str, node: SyntheticDataComputationNode, analysts: List[str]
    ) -> Self:
        """
        Instantiate a `SyntheticDataComputeNode` from its high level representation.

        **Parameters**:
        - `id`: ID of the `SyntheticDataComputeNode`.
        - `name`: Name of the `SyntheticDataComputeNode`.
        - `node`: Pydantic model of the `SyntheticDataComputeNode`.
        - `analysts`: List of analysts for the `SyntheticDataComputeNode`.
        """
        node_json = json.loads(node.model_dump_json())
        config = SqliteNodeConfig.from_dict(node_json)
        return SyntheticDataComputeNode(
            name=name,
            id=id,
            config=config,
            analysts=analysts,
        )


class S3Provider(str, Enum):
    AWS = "Aws"
    GCS = "Gcs"


@dataclass
class S3SinkNodeConfig:
    credentials_dependency_id: str
    endpoint: str
    region: str
    upload_dependency_id: str
    s3_provider: Optional[S3Provider] = S3Provider.AWS

    @staticmethod
    def from_dict(dictionary: Dict[str, str]) -> Self:
        """
        Instantiate a `S3SinkNodeConfig` from the dictionary representation.

        **Parameters**:
        - `dictionary`: Dictionary representation of the `S3SinkNodeConfig`.
        """
        return SqliteNodeConfig(
            credentials_dependency_id=dictionary["credentialsDependencyId"],
            endpoint=dictionary["endpoint"],
            region=dictionary["region"],
            upload_dependency_id=dictionary["uploadDependencyId"],
            s3_provider=dictionary["s3Provider"],
        )


class S3SinkComputeNode(ComputationNode):
    """
    Class representing an S3 Sink Computation node.
    """

    def __init__(
        self,
        name: str,
        config: S3SinkNodeConfig,
        analysts: List[str],
        id: Optional[str] = None,
    ) -> None:
        """
        Initialise a `S3SinkComputeNode`:

        **Parameters**:
        `name`: Name of the `S3SinkComputeNode`.
        `config`: Configuration of the `S3SinkComputeNode`.
        `analysts`: List of analysts for the `S3SinkComputeNode`.
        `id`: Optional ID of the `S3SinkComputeNode`. If omitted, an ID is auto generated.
        """
        super().__init__(name, analysts, id)
        self.cfg = config
        self.specification_id = "decentriq.s3-sink-worker"

    def get_high_level_representation(self) -> Dict[str, str]:
        """
        Retrieve the high level representation of the `S3SinkComputeNode`.
        """
        computation_node = {
            "id": self.id,
            "name": self.name,
            "kind": {
                "computation": {
                    "kind": {
                        "s3Sink": {
                            "credentialsDependencyId": self.cfg.credentials_dependency_id,
                            "endpoint": self.cfg.endpoint,
                            "region": self.cfg.region,
                            "s3Provider": self.cfg.s3_provider.value,
                            "specificationId": self.specification_id,
                            "uploadDependencyId": self.cfg.upload_dependency_id,
                        }
                    }
                },
            },
        }
        return computation_node

    def get_computation_id(self) -> str:
        """
        Retrieve the ID of the node corresponding to the computation.
        """
        return self.id

    def from_high_level(
        id: str, name: str, node: S3SinkComputationNode, analysts: List[str]
    ) -> Self:
        """
        Instantiate a `S3SinkComputeNode` from its high level representation.

        **Parameters**:
        - `id`: ID of the `S3SinkComputeNode`.
        - `name`: Name of the `S3SinkComputeNode`.
        - `node`: Pydantic model of the `S3SinkComputeNode`.
        - `analysts`: List of analysts for the `S3SinkComputeNode`.
        """
        node_json = json.loads(node.model_dump_json())
        config = S3SinkNodeConfig.from_dict(node_json)
        return S3SinkComputeNode(
            name=name,
            id=id,
            config=config,
            analysts=analysts,
        )


@dataclass
class MatchingComputeNodeConfig:
    query: List[str]
    round: int
    epsilon: int
    sensitivity: int
    dependency_paths: List[str]


@dataclass
class MatchingNodeConfig:
    config: MatchingComputeNodeConfig
    dependencies: List[str]
    enable_logs_on_error: Optional[bool] = False
    enable_logs_on_success: Optional[bool] = False
    output: Optional[str] = "/output"

    @staticmethod
    def from_dict(dictionary: Dict[str, str]) -> Self:
        """
        Instantiate a `MatchingNodeConfig` from the dictionary representation.

        **Parameters**:
        - `dictionary`: Dictionary representation of the `MatchingNodeConfig`.
        """
        config = json.loads(dictionary["config"])
        return MatchingNodeConfig(
            config=MatchingComputeNodeConfig(**config),
            dependencies=dictionary["dependencies"],
            enable_logs_on_error=dictionary["enableLogsOnError"],
            enable_logs_on_success=dictionary["enableLogsOnSuccess"],
            output=dictionary["output"],
        )


class MatchingComputeNode(ComputationNode):
    """
    Class representing a Matching Computation node.
    """

    def __init__(
        self,
        name: str,
        config: MatchingNodeConfig,
        analysts: List[str],
        id: Optional[str] = None,
    ) -> None:
        """
        Initialise a `MatchingComputeNode`:

        **Parameters**:
        `name`: Name of the `MatchingComputeNode`.
        `config`: Configuration of the `MatchingComputeNode`.
        `analysts`: List of analysts for the `MatchingComputeNode`.
        `id`: Optional ID of the `MatchingComputeNode`. If omitted, an ID is auto generated.
        """
        super().__init__(name, analysts, id)
        self.cfg = config
        self.specification_id = "decentriq.python-ml-worker-32-64"
        self.static_content_specification_id = "decentriq.driver"

    def get_high_level_representation(self) -> Dict[str, str]:
        """
        Retrieve the high level representation of the `MatchingComputeNode`.
        """
        dependencies = [] if not self.cfg.dependencies else self.cfg.dependencies
        computation_node = {
            "id": self.id,
            "name": self.name,
            "kind": {
                "computation": {
                    "kind": {
                        "match": {
                            "config": json.dumps(asdict(self.cfg.config)),
                            "dependencies": dependencies,
                            "enableLogsOnError": self.cfg.enable_logs_on_error,
                            "enableLogsOnSuccess": self.cfg.enable_logs_on_success,
                            "output": self.cfg.output,
                            "specificationId": self.specification_id,
                            "staticContentSpecificationId": self.static_content_specification_id,
                        }
                    }
                },
            },
        }
        return computation_node

    def get_computation_id(self) -> str:
        """
        Retrieve the ID of the node corresponding to the computation.
        """
        return f"{self.id}_match_filter_node"

    def from_high_level(
        id: str, name: str, node: MatchingComputationNode, analysts: List[str]
    ) -> Self:
        """
        Instantiate a `MatchingComputeNode` from its high level representation.

        **Parameters**:
        - `id`: ID of the `MatchingComputeNode`.
        - `name`: Name of the `MatchingComputeNode`.
        - `node`: Pydantic model of the `MatchingComputeNode`.
        - `analysts`: List of analysts for the `MatchingComputeNode`.
        """
        node_json = json.loads(node.model_dump_json())
        config = MatchingNodeConfig.from_dict(node_json)
        return MatchingComputeNode(
            name=name,
            id=id,
            config=config,
            analysts=analysts,
        )


@dataclass
class PreviewNodeConfig:
    dependency: str
    quota_bytes: Optional[int] = 0

    @staticmethod
    def from_dict(dictionary: Dict[str, str]) -> Self:
        """
        Instantiate a `PreviewNodeConfig` from the dictionary representation.

        **Parameters**:
        - `dictionary`: Dictionary representation of the `PreviewNodeConfig`.
        """
        return PreviewNodeConfig(
            dependency=dictionary["dependency"],
            quota_bytes=dictionary["quotaBytes"],
        )


class PreviewComputeNode(ComputationNode):
    """
    Class representing a Preview (Airlock) Computation node.
    """

    def __init__(
        self,
        name: str,
        config: PreviewNodeConfig,
        analysts: List[str],
        id: Optional[str] = None,
    ) -> None:
        """
        Initialise a `PreviewComputeNode`:

        **Parameters**:
        `name`: Name of the `PreviewComputeNode`.
        `config`: Configuration of the `PreviewComputeNode`.
        `analysts`: List of analysts for the `PreviewComputeNode`.
        `id`: Optional ID of the `PreviewComputeNode`. If omitted, an ID is auto generated.
        """
        super().__init__(name, analysts, id)
        self.cfg = config
        self.specification_id = "decentriq.python-ml-worker-32-64"

    def get_high_level_representation(self) -> Dict[str, str]:
        """
        Retrieve the high level representation of the `PreviewComputeNode`.
        """
        computation_node = {
            "id": self.id,
            "name": self.name,
            "kind": {
                "computation": {
                    "kind": {
                        "preview": {
                            "dependency": self.cfg.dependency,
                            "quotaBytes": self.cfg.quota_bytes,
                        }
                    }
                },
            },
        }
        return computation_node

    def get_computation_id(self) -> str:
        """
        Retrieve the ID of the node corresponding to the computation.
        """
        return self.id

    def from_high_level(
        id: str, name: str, node: PreviewComputationNode, analysts: List[str]
    ) -> Self:
        """
        Instantiate a `PreviewComputeNode` from its high level representation.

        **Parameters**:
        - `id`: ID of the `PreviewComputeNode`.
        - `name`: Name of the `PreviewComputeNode`.
        - `node`: Pydantic model of the `PreviewComputeNode`.
        - `analysts`: List of analysts for the `PreviewComputeNode`.
        """
        node_json = json.loads(node.model_dump_json())
        config = PreviewNodeConfig.from_dict(node_json)
        return PreviewComputeNode(
            name=name,
            id=id,
            config=config,
            analysts=analysts,
        )
