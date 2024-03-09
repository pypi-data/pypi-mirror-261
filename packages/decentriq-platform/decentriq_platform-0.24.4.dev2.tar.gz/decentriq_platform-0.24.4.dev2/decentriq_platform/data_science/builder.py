import base64
from enum import Enum
from typing import Dict, List, Optional
from typing_extensions import Self
import uuid
from ..client import Client
from ..attestation import SPECIFICATIONS, EnclaveSpecifications
from decentriq_dcr_compiler import compiler
from decentriq_dcr_compiler.schemas.data_science_data_room import DataScienceDataRoom
from decentriq_dcr_compiler.schemas.data_science_commit import DataScienceCommit
from ..session import (
    LATEST_WORKER_PROTOCOL_VERSION,
    Session,
)
from ..proto.length_delimited import parse_length_delimited, serialize_length_delimited
from ..proto import DataRoom, CreateDcrKind, ConfigurationCommit
from .compute_nodes import ComputationNode
from .data_nodes import DataNode
from .commits import ComputationCommit
from .existing_builder import ExistingDataScienceDcrBuilder


__all__ = [
    "DataScienceDcrBuilder",
]


class DataScienceDcrType(str, Enum):
    STATIC = "STATIC"
    INTERACTIVE = "INTERACTIVE"


class ParticipantPermission(Enum):
    DATA_OWNER = 1
    ANALYST = 2


class DataScienceDcrBuilder:
    """
    A builder for constructing Data Science data clean rooms.
    """

    def __init__(
        self,
        client: Client,
        enclave_specs: Optional[Dict[str, EnclaveSpecifications]] = None,
    ) -> None:
        """
        Initialise a Data Science DCR builder.

        **Parameters**:
        - `client`: A `Client` object which can be used to perform operations such as uploading data
            and retrieving computation results.
        - `enclave_specs`: Determines the types of enclaves that are supported by this data clean room.
            If not specified, the latest enclave specifications will be used.
        """
        self.client = client
        self.enclave_specs = enclave_specs
        self.name = None
        self.description = ""
        self.owner = None
        self.data_nodes = []
        self.compute_nodes = []
        self.dcr_id = None
        self.enable_development = False
        self.enable_airlock = False
        self.participants = None
        self.enable_auto_merge_feature = False
        self.compile_context = None
        self.existing = False

    @staticmethod
    def from_existing(
        dcr_id: str,
        client: Client,
        enclave_specs: Optional[Dict[str, EnclaveSpecifications]] = None,
    ) -> Self:
        """
        Create a Data Science DCR builder from an existing Data Science data clean room.
        The returned builder allows the underlying computation nodes and data nodes to be
        retrieved by calling `get_compute_nodes` and `get_data_nodes` respectively.

        **Parameters**:
        - `dcr_id`: The ID of the existing Data Science data clean room.
        - `client`: A `Client` object which can be used to perform operations such as uploading data
            and retrieving computation results.
        - `enclave_specs`: Determines the types of enclaves that are supported by this data clean room.
            If not specified, the latest enclave specifications will be used.
        """
        builder = DataScienceDcrBuilder(client, enclave_specs)
        builder.dcr_id = dcr_id
        builder.existing = True
        return builder

    def get_compute_nodes(self) -> List[ComputationNode]:
        """
        Retrieve the list of computation nodes in the data clean room.
        """
        return self.compute_nodes

    def get_data_nodes(self) -> List[DataNode]:
        """
        Retrieve the list of data nodes in the data clean room.
        """
        return self.data_nodes

    def with_name(self, name: str) -> Self:
        """
        Set the name of the data clean room.

        **Parameters**:
        - `name`: Name to be used for the data clean room.
        """
        self.name = name
        return self

    def with_description(self, description: str) -> Self:
        """
        Set the description of the data clean room.

        **Parameters**:
        - `description`: Description of the data clean room.
        """
        self.description = description
        return self

    def with_participants(self, participants: List[str]) -> Self:
        """
        Set the participants of the data clean room. This should also include
        the DCR owner.

        **Parameters**:
        - `participants`: Participants of the data clean room.
        """
        self.participants = participants
        return self

    def with_auto_merge(self) -> Self:
        """
        Allow auto-merging of commits.
        """
        self.enable_auto_merge_feature = True
        return self

    def with_owner(self, owner: str) -> Self:
        """
        Set the owner of the data clean room.

        **Parameters**:
        - `owner`: The owner of the data clean room.
        """
        self.owner = owner
        return self

    def with_development_mode(self) -> Self:
        """
        Enable development mode in the data clean room.
        """
        self.enable_development = True
        return self

    def with_airlock(self) -> Self:
        """
        Enable the Airlock feature in the data clean room.
        This requires Development mode to be enabled.
        """
        self.enable_airlock = True

    def add_data_node(self, node: DataNode) -> str:
        """
        Add a data node to the data clean room.

        **Parameters**:
        - `node`: Data node to be added to the data clean room.

        **Returns**:
        The ID of the Data node.
        """
        self.data_nodes.append(node)
        return node.get_id()

    def add_compute_node(self, node: ComputationNode) -> str:
        """
        Add a computation node to the data clean room.

        **Parameters**:
        - `node`: Computation node to be added to the data clean room.

        **Returns**:
        The ID of the Computation node.
        """
        self.compute_nodes.append(node)
        return node.get_id()

    def build(self):
        """
        Build the data clean room.
        If the builder was configured to interact with an existing data clean room
        calling this function will allow the Computation nodes and Data nodes to be
        subsequently retrieved.
        """
        if self.existing:
            return self._from_existing()
        else:
            return self._build_new()

    def _from_existing(self):
        if not self.dcr_id:
            raise Exception("Existing DCR ID not specified")

        data_room_descriptions = self.client.get_data_room_descriptions()
        existing_data_room_description = [
            description
            for description in data_room_descriptions
            if description["id"] == self.dcr_id
        ]
        if len(existing_data_room_description) != 1:
            raise Exception(
                f"Unable to retrieve data room description for data room with ID {self.dcr_id}"
            )

        specs = (
            EnclaveSpecifications(self.enclave_specs) if self.enclave_specs else None
        )
        session = self.client.create_session_from_data_room_description(
            existing_data_room_description[0], specs
        )
        existing_dcr_builder = ExistingDataScienceDcrBuilder(
            self.dcr_id, self.client, session
        )
        existing_cfg = existing_dcr_builder.get_configuration()
        self.name = existing_cfg.name
        self.description = existing_cfg.description
        self.owner = existing_cfg.owner
        self.data_nodes = existing_cfg.data_nodes
        self.compute_nodes = existing_cfg.compute_nodes
        self.dcr_id = existing_cfg.dcr_id
        self.enable_development = existing_cfg.enable_development
        self.enable_airlock = existing_cfg.enable_airlock
        self.participants = existing_cfg.participants
        self.enable_auto_merge_feature = existing_cfg.enable_auto_merge_feature

        return self.dcr_id

    def _build_new(self):
        if not self.owner:
            raise Exception("The data room owner must be specified")
        permissions = self._get_participant_permissions()
        all_nodes = self.compute_nodes + self.data_nodes
        nodes = [node.get_high_level_representation() for node in all_nodes]
        ds_dcr = {
            "v6": {
                # Only interactive DCRs are supported.
                "interactive": {
                    "commits": [],
                    "enableAutomergeFeature": self.enable_auto_merge_feature,
                    "initialConfiguration": {
                        "description": self.description,
                        "enableAirlock": self.enable_airlock,
                        "enableAllowEmptyFilesInValidation": False,
                        "enableDevelopment": self.enable_development,
                        "enablePostWorker": False,
                        "enableSafePythonWorkerStacktrace": True,
                        "enableServersideWasmValidation": True,
                        "enableSqliteWorker": False,
                        "enableTestDatasets": False,
                        "enclaveRootCertificatePem": self.client.decentriq_ca_root_certificate.decode(),
                        "enclaveSpecifications": self._get_hl_specs(),
                        "id": self._generate_id(),
                        "nodes": nodes,
                        "participants": permissions,
                        "title": self.name,
                    },
                }
            }
        }

        data_room = DataScienceDataRoom.model_validate(ds_dcr)
        compiled_data_room = compiler.compile_data_science_data_room(data_room)
        self.compile_context = compiled_data_room.compile_context

        session = self._get_new_dcr_session()
        low_level_data_room = DataRoom()
        parse_length_delimited(compiled_data_room.data_room, low_level_data_room)
        self.dcr_id = session.publish_data_room(
            low_level_data_room,
            kind=CreateDcrKind.DATASCIENCE,
            high_level_representation=compiled_data_room.datascience_data_room_encoded,
        )

        for node in all_nodes:
            # Associate the node with this DCR.
            node.set_dcr_id(self.dcr_id)
            # Set the session for future node operations.
            node.set_session(session)
            # Set the client for future node operations.
            node.set_client(self.client)

        return self.dcr_id

    def add_computation_to_existing_dcr(
        self,
        node: ComputationNode,
    ) -> ComputationCommit:
        """
        Add a new Computation node to the existing data clean room.

        **Parameters**:
        - `node`: The Computation node to add to the existing data clean room.
        """
        if not self.dcr_id:
            raise Exception("Data room must be built before it can be modified.")
        elif not self.enable_development:
            raise Exception("Data room does not have development mode enabled")
        elif not self.compile_context:
            raise Exception("Data room compile context not initialised")

        # Associate the node with the DCR.
        node.set_dcr_id(self.dcr_id)

        session = self._get_existing_dcr_session()
        (_current_config, history_pin) = (
            session.retrieve_current_data_room_configuration(self.dcr_id)
        )
        computation_commit = ComputationCommit(
            history_pin=history_pin,
            node=node,
        )
        computation_commit.set_dcr_id(self.dcr_id)
        computation_commit.set_session(session)
        computation_commit.set_client(self.client)
        hl = {"v6": computation_commit.get_high_level_representation()}
        ds_commit = DataScienceCommit.model_validate(hl)
        compiled_commit = compiler.compile_data_science_commit(
            ds_commit, self.compile_context
        )
        # Update the context.
        self.compile_context = compiled_commit.compile_context

        cfg_commit = ConfigurationCommit()
        parse_length_delimited(compiled_commit.commit, cfg_commit)
        commit_id = session.publish_data_room_configuration_commit(cfg_commit)
        computation_commit.set_commit_id(commit_id)
        return computation_commit

    def _get_existing_dcr_session(self) -> Session:
        data_room_descriptions = self.client.get_data_room_descriptions()
        existing_data_room_description = [
            description
            for description in data_room_descriptions
            if description["id"] == self.dcr_id
        ]
        if len(existing_data_room_description) != 1:
            raise Exception(
                f"Unable to retrieve data room description for data room with ID {self.dcr_id}"
            )

        specs = (
            EnclaveSpecifications(self.enclave_specs) if self.enclave_specs else None
        )
        session = self.client.create_session_from_data_room_description(
            existing_data_room_description[0], specs
        )
        return session


    def _get_new_dcr_session(self) -> Session:
        enclave_specs = (
            SPECIFICATIONS if self.enclave_specs is None else self.enclave_specs
        )
        auth, _ = self.client.create_auth_using_decentriq_pki(enclave_specs)
        session = self.client.create_session(auth, enclave_specs)
        return session

    def _get_hl_specs(self):
        enclave_specs = (
            SPECIFICATIONS if self.enclave_specs is None else self.enclave_specs
        )
        specs = [
            {
                "attestationProtoBase64": base64.b64encode(
                    serialize_length_delimited(spec["proto"])
                ).decode(),
                "id": name,
                "workerProtocol": LATEST_WORKER_PROTOCOL_VERSION,
            }
            for name, spec in enclave_specs.items()
        ]
        return specs

    def _get_participant_permissions(self):
        if not self.participants:
            raise Exception("Data room does not have any participants")

        participants = []
        for participant in self.participants:
            hl_permissions = []
            for node in self.data_nodes:
                if node.is_data_owner(participant):
                    hl_permissions.append({"dataOwner": {"nodeId": node.get_id()}})
            for node in self.compute_nodes:
                if node.is_analyst(participant):
                    hl_permissions.append({"analyst": {"nodeId": node.get_id()}})
            if self.owner == participant:
                hl_permissions.append({"manager": {}})
            participants.append(
                {
                    "user": participant,
                    "permissions": hl_permissions,
                }
            )
        return participants

    @staticmethod
    def _generate_id():
        return str(uuid.uuid4())
