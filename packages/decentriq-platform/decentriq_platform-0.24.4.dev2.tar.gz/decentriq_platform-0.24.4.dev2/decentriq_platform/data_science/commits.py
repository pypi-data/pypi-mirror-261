import base64
from dataclasses import dataclass, asdict
from .high_level_node import ComputationNode
from ..types import EnclaveSpecification
from ..proto.length_delimited import serialize_length_delimited
from typing import List, Dict, Optional


class ComputationCommit(ComputationNode):
    """
    Class representing a Computation that has been added to an existing data clean room.
    """

    def __init__(
        self,
        history_pin: str,
        node: ComputationNode,
        enclave_specs: Optional[Dict[str, EnclaveSpecification]] = None,
        name: Optional[str] = "",
    ) -> None:
        """
        Initialise a `ComputationCommit`:

        **Parameters**:
        - `history_pin`: A pin of the commit history.
        - `node`: A `ComputationNode` that should be added to a data clean room.
        - `enclave_specs`: Determines the types of enclaves that are supported by this data clean room.
            If not specified, the latest enclave specifications will be used.
        - `name`: The name of the `ComputationCommit`.
        """
        super().__init__(name, node.get_analysts(), None)
        self.history_pin = history_pin
        self.node = node
        self.enclave_specs = enclave_specs
        self.commit_id = None

    def get_high_level_representation(self) -> Dict[str, str]:
        """
        Retrieve the high level representation of the `ComputationCommit`.
        """
        enclave_specs = [] if not self.enclave_specs else self._map_enclave_specs()
        return {
            "enclaveDataRoomId": self.dcr_id,
            "historyPin": self.history_pin,
            "id": self.id,
            "kind": {
                "addComputation": {
                    "analysts": self.analysts,
                    "enclaveSpecifications": enclave_specs,
                    "node": self.node.get_high_level_representation(),
                }
            },
            "name": self.name,
        }

    def get_computation_id(self) -> str:
        """
        Retrieve the ID of the node corresponding to the computation commit.
        """
        return self.id

    def run_computation_and_get_results(self):
        """
        This is a blocking call to run a computation and get the results.
        """
        if not self.commit_id:
            raise Exception("Commit ID must be set before the computatin can be run")

        # Run a dev computation against this computation commit.
        job_id = self.session.run_dev_computation(
            self.dcr_id, self.commit_id, self.node.get_computation_id()
        )
        results = self.session.get_computation_result(job_id)
        return results

    def set_commit_id(self, commit_id: str):
        """
        Set the ID of the computation commit.

        **Parameters**:
        - `commit_id`: ID to be used for the computation commit.
        """
        self.commit_id = commit_id

    def _map_enclave_specs(self) -> List[Dict[str, str]]:
        @dataclass
        class EnclaveSpec:
            attestationProtoBase64: str
            id: str
            workerProtocol: int

        enclave_specs = []
        for spec_id, spec in self.enclave_specs.items():
            enclave_specs.append(
                asdict(
                    EnclaveSpec(
                        attestationProtoBase64=base64.b64encode(
                            serialize_length_delimited(spec["proto"])
                        ).decode(),
                        id=spec_id,
                        workerProtocol=spec["workerProtocols"][0],
                    )
                )
            )
        return enclave_specs
