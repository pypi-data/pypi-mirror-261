from enum import Enum
import io, json
from typing import Dict, Optional, List, BinaryIO
import zipfile
from .high_level_node import DataNode
from dataclasses import dataclass
from ..storage import Key
from decentriq_dcr_compiler.schemas.data_science_data_room import (
    RawLeafNode,
    TableLeafNodeV2,
)
from typing_extensions import Self


class RawDataNode(DataNode):
    """
    Class representing a Raw Data node.
    """

    def __init__(
        self,
        name: str,
        data_owners: List[str],
        is_required: bool,
        id: Optional[str] = None,
    ) -> None:
        """
        Initialise a `RawDataNode` instance.

        **Parameters**:
        - `name`: Name of the `RawDataNode`
        - `data_owners`: List of users that are permitted to upload/publish data to the `RawDataNode`.
        - `is_required`: Flag determining if the `RawDataNode` must be present for dependent computations.
        - 'id': Optional ID of the `RawDataNode`. If omitted an ID is auto generated.
        """
        super().__init__(name, is_required, data_owners, id)
        self.data_owners = data_owners

    def get_high_level_representation(self) -> Dict[str, str]:
        """
        Retrieve the high level representation of the `RawDataNode`.
        """
        raw_node = {
            "id": self.id,
            "name": self.name,
            "kind": {"leaf": {"isRequired": self.is_required, "kind": {"raw": {}}}},
        }
        return raw_node

    def from_high_level(
        id: str,
        name: str,
        _node: RawLeafNode,
        is_required: bool,
        data_owners: List[str],
    ) -> Self:
        """
        Instantiate a `RawDataNode` from its high level representation.

        **Parameters**:
        - `id`: ID of the `RawDataNode`.
        - `name`: Name of the `RawDataNode`.
        - `_node`: Pydantic model of the `RawLeafNode`.
        - `is_required`: Flag determining if the `RawDataNode` must be present for dependent computations.
        - `data_owners`: List of users that are permitted to upload/publish data to the `RawDataNode`.
        """
        return RawDataNode(
            name=name, id=id, is_required=is_required, data_owners=data_owners
        )


class ColumnDataType(str, Enum):
    INTEGER = "integer"
    FLOAT = "float"
    STRING = "string"


@dataclass
class ColumnDataFormat:
    dataType: ColumnDataType
    isNullable: bool


class FormatType(str, Enum):
    STRING = "STRING"
    INTEGER = "INTEGER"
    FLOAT = "FLOAT"
    EMAIL = "EMAIL"
    DATE_ISO8601 = "DATE_ISO8601"
    PHONE_NUMBER_E164 = "PHONE_NUMBER_E164"
    HASH_SHA256_HEX = "HASH_SHA256_HEX"

    @staticmethod
    def from_column_data_type(fmt: ColumnDataType) -> str:
        if fmt == ColumnDataType.INTEGER:
            return FormatType.INTEGER.value
        elif fmt == ColumnDataType.FLOAT:
            return FormatType.FLOAT.value
        elif fmt == ColumnDataType.STRING:
            return FormatType.STRING.value
        else:
            raise Exception(
                f"Unable to convert column data type {fmt.value} to a format type"
            )


class HashingAlgorithm(str, Enum):
    SHA256_HEX = "SHA256_HEX"


class NumericRangeRule:
    greaterThan: Optional[float] = None
    greaterThanEquals: Optional[float] = None
    lessThan: Optional[float] = None
    lessThanEquals: Optional[float] = None


@dataclass
class Column:
    dataFormat: ColumnDataFormat
    name: str
    hashWith: Optional[HashingAlgorithm] = None
    inRange: Optional[NumericRangeRule] = None


class TableDataNode(DataNode):
    """
    Class representing a Table Data node.
    """

    def __init__(
        self,
        name: str,
        columns: List[Column],
        data_owners: List[str],
        is_required: bool,
        id: Optional[str] = None,
    ) -> None:
        """
        Initialise a `TableDataNode` instance.

        **Parameters**:
        - `name`: Name of the `TableDataNode`
        - `columns`: Definition of the columns that make up the `TableDataNode`.
        - `data_owners`: List of users that are permitted to upload/publish data to the `RawDataNode`.
        - `is_required`: Flag determining if the `RawDataNode` must be present for dependent computations.
        - 'id': Optional ID of the `RawDataNode`. If omitted an ID is auto generated.
        """
        super().__init__(name, is_required, data_owners, id)
        self.columns = columns

    def get_high_level_representation(self) -> Dict[str, str]:
        """
        Retrieve the high level representation of the `TableDataNode`.
        """
        column_entries = []
        for column in self.columns:
            validation = {
                "name": column.name,
                "formatType": FormatType.from_column_data_type(
                    column.dataFormat.dataType
                ),
                "allowNull": column.dataFormat.isNullable,
            }
            if column.hashWith:
                validation["hashWith"] = column.hashWith.value
            if column.inRange:
                validation["inRange"] = column.inRange.value
            column_entries.append(
                {
                    "name": column.name,
                    "dataFormat": {
                        "isNullable": column.dataFormat.isNullable,
                        "dataType": column.dataFormat.dataType.value,
                    },
                    "validation": validation,
                }
            )

        table_node = {
            "id": self.id,
            "name": self.name,
            "kind": {
                "leaf": {
                    "isRequired": self.is_required,
                    "kind": {
                        "table": {
                            "columns": column_entries,
                            "validationNode": {
                                "staticContentSpecificationId": "decentriq.driver",
                                "pythonSpecificationId": "decentriq.python-ml-worker-32-64",
                                "validation": {},
                            },
                        }
                    },
                }
            },
        }
        return table_node

    # This data node needs to override the `super` implementation because
    # the leaf ID requires the "_leaf" suffix.
    def publish_data(self, manifest_hash: str, key: Key):
        """
        Publish data to the `TableDataNode`.

        **Parameters**:
        - `manifest_hash`: Hash identifying the dataset to be published.
        - `key`: Encryption key used to decrypt the dataset.
        """
        self.session.publish_dataset(
            self.dcr_id, manifest_hash, leaf_id=f"{self.id}_leaf", key=key
        )

    def get_name(self) -> str:
        """
        Retrive the name of the `TableDataNode`.
        """
        return self.name

    def from_high_level(
        id: str,
        name: str,
        node: TableLeafNodeV2,
        is_required: bool,
        data_owners: List[str],
    ) -> Self:
        """
        Instantiate a `TableDataNode` from its high level representation.

        **Parameters**:
        - `id`: ID of the `TableDataNode`.
        - `name`: Name of the `TableDataNode`.
        - `node`: Pydantic model of the `TableDataNode`.
        - `is_required`: Flag determining if the `TableDataNode` must be present for dependent computations.
        - `data_owners`: List of users that are permitted to upload/publish data to the `TableDataNode`.
        """
        node_dict = json.loads(node.model_dump_json())
        columns = [
            Column(
                dataFormat=ColumnDataFormat(**column["dataFormat"]),
                name=column["name"],
                hashWith=column["validation"]["hashWith"],
                inRange=column["validation"]["inRange"],
            )
            for column in node_dict["columns"]
        ]
        return TableDataNode(
            name=name,
            columns=columns,
            data_owners=data_owners,
            id=id,
            is_required=is_required,
        )

    def get_validation_report(self) -> Dict[str, str]:
        """
        Retrieve the validation report corresponding to this `TableDataNode`.
        """
        validation_node_id = f"{self.id}_validation_report"
        result = self.session.run_computation_and_get_results(
            self.dcr_id, validation_node_id, interval=1
        )

        validation_report = {}
        zip = zipfile.ZipFile(io.BytesIO(result), "r")
        if "validation-report.json" in zip.namelist():
            validation_report = json.loads(zip.read("validation-report.json").decode())
        return validation_report
