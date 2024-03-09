from abc import ABC, abstractmethod
from typing import Dict, BinaryIO, List, Optional
import uuid
from ..session import Session
from ..client import Client
from ..storage import Key
from ..types import JobId

__all__ = ["HighLevelNode"]


class HighLevelNode(ABC):
    """
    Abstract class representing a High Level Node.
    Any subclass must implement the method for retrieving the
    high level representation.
    """

    def __init__(self, name: str, id=Optional[str]) -> None:
        super().__init__()
        self.id = str(uuid.uuid4()) if not id else id
        self.name = name
        self.dcr_id = None
        self.client = None
        self.session = None

    @abstractmethod
    def get_high_level_representation(self) -> Dict[str, str]:
        """
        Retrieve the high level representation of the `HighLevelNode`.
        """
        pass

    def get_id(self) -> str:
        return self.id

    def get_name(self) -> str:
        return self.name

    def set_dcr_id(self, dcr_id: str):
        self.dcr_id = dcr_id

    def get_dcr_id(self) -> Optional[str]:
        return self.dcr_id

    def set_client(self, client: Client):
        self.client = client

    def set_session(self, session: Session):
        self.session = session


class ComputationNode(HighLevelNode, ABC):
    """
    Class representing a Computation node.

    Computation nodes allow a permitted analyst to run a computation and
    retrieve the results of a computation.
    """

    def __init__(self, name: str, analysts: List[str], id=Optional[str]) -> None:
        """
        Initialise an instance of a `ComputationNode`.

        **Parameters**:
        - `name`: Name of the `ComputationNode`.
        - `analysts`: List of users that are permitted to run computations and retrieve results.
        - 'id': Optional ID of the `DataNode`. If omitted an ID is auto generated.
        """
        super().__init__(name, id)
        self.analysts = analysts
        self.job_id = None

    def run_computation(self):
        """
        Run the computation associated with this node.
        """
        if not self.session:
            raise Exception(
                f"Unable to run computation. Node {self.id} does not have an associated session"
            )
        self.job_id = self.session.run_computation(
            self.dcr_id, self.get_computation_id()
        )

    def get_results(
        self,
        interval: Optional[int] = 5,
        timeout: Optional[int] = None,
    ) -> Optional[bytes]:
        """
        Retrieve the results of a computation.

        **Parameters**:
        - `interval`: Time interval (in seconds) to check for results.
        - `timeout`: Time (in seconds) after which results are no longer checked.
        """
        if not self.job_id:
            raise Exception("A computation must be run before results can be retrieved")
        return self.session.get_computation_result(
            self.job_id, interval=interval, timeout=timeout
        )

    def run_computation_and_get_results(self):
        """
        This is a blocking call to run a computation and get the results.
        """
        if not self.session:
            raise Exception(
                f"Unable to run computation. Node {self.id} does not have an associated session"
            )
        return self.session.run_computation_and_get_results(
            self.dcr_id, self.get_computation_id(), interval=1
        )

    @abstractmethod
    def get_computation_id(self) -> str:
        """
        Retrieve the ID of the node corresponding to the computation.
        """
        pass

    def is_analyst(self, user_email: str) -> bool:
        """
        Check if the given user is an analyst of this `ComputationNode`.

        **Parameters**:
        - `user_email`: Email address of the user.
        """
        return user_email in self.analysts

    def get_analysts(self) -> List[str]:
        """
        Retrieve the list of analysts of this `ComputationNode`.
        """
        return self.analysts


class DataNode(HighLevelNode, ABC):
    """
    Class representing a Data node.

    Data nodes allow a permitted data owner to upload and publish dataset to the node.
    """

    def __init__(
        self, name: str, is_required: bool, data_owners: List[str], id=Optional[str]
    ) -> None:
        """
        Initialise an instance of a `DataNode`.

        **Parameters**:
        - `name`: Name of the `DataNode`.
        - `is_required`: Flag determining if the `DataNode` must be present for dependent computations.
        - `data_owners`: List of users that are permitted to upload/publish data to the `DataNode`.
        - 'id': Optional ID of the `DataNode`. If omitted an ID is auto generated.
        """
        super().__init__(name, id)
        self.is_required = is_required
        self.data_owners = data_owners

    def publish_data(self, manifest_hash: str, key: Key):
        """
        Publish data to the `DataNode`.

        **Parameters**:
        - `manifest_hash`: Hash identifying the dataset to be published.
        - `key`: Encryption key used to decrypt the dataset.
        """
        self.session.publish_dataset(
            self.dcr_id, manifest_hash, leaf_id=self.id, key=key
        )

    def upload_and_publish_data(self, data: BinaryIO, key: Key, file_name: str):
        """
        Upload data to the Decentriq Platform and publish it to the `DataNode`.

        **Parameters**:
        - `data`: Binary representation of the data to be uploaded.
        - `key`: Key to be used for encrypting the data.
        - `file_name`: Name of the file.
        """
        if not self.dcr_id:
            raise Exception("Data node is not part of a data room")

        manifest_hash = self.client.upload_dataset(data, key, file_name)
        self.publish_data(manifest_hash, key)

    def is_data_owner(self, user_email: str) -> bool:
        """
        Check if the given user is a data owner for this `DataNode`.

        **Parameters**:
        - `user_email`: Email address of the user.
        """
        return user_email in self.data_owners
