"""Python client for Timeseer Flows."""

import time
from datetime import datetime
from typing import Dict, List, Optional

from kukur import SeriesSelector

from timeseer_client.internal import JSONFlightClient, TimeseerClientException


class FlowEvaluationFailedException(TimeseerClientException):
    """Thrown when a flow evaluation fails."""

    def __init__(self, flow_name: Optional[str]):
        if flow_name is None:
            super().__init__("flow evaluation failed.")
        else:
            super().__init__(f'evaluation for flow "{flow_name}" failed.')


class Flows:
    """Flows run modules to process time series data.

    Args:
        client: the Timeseer Client
    """

    __client: JSONFlightClient

    def __init__(self, client: JSONFlightClient):
        self.__client = client

    def list(self) -> List[str]:
        """Return a list containing all the flow names."""
        return self.__client.do_action("flows/list", {})

    def evaluate(self, flow_name: str, *, block=True):
        """Evaluate a flow.

        Args:
            flow_name: the name of the flow to evaluate
            block: block until the evaluation completes (keyword-only, default True)

        Raises:
            FlowEvaluationFailedException when a failure is reported.
        """
        evaluate_flow(self.__client, flow_name, block=block)

    def duplicate(  # noqa: PLR0913
        self,
        existing_flow_name: str,
        new_flow_name: str,
        *,
        series_set_names: Optional[List[str]] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        data_set_name: Optional[str] = None,
    ):
        """Duplicate an existing flow.

        Args:
            existing_flow_name: the name of the flow to duplicate.
            new_flow_name: the name of the duplicated flow.
            series_set_names: the names of the existing series sets to be used in the flow. (Optional).
            start_date: the start date of the flow (Optional).
            end_date: the end date of the flow (Optional).
            data_set_name: the name of the data set to use for the flow (Optional).
        """
        body: Dict = {
            "existingFlowName": existing_flow_name,
            "newFlowName": new_flow_name,
            "seriesSetNames": series_set_names,
            "dataSetName": data_set_name,
        }
        if start_date is not None:
            body["startDate"] = start_date.isoformat()
        if end_date is not None:
            body["endDate"] = end_date.isoformat()
        self.__client.do_action("flows/duplicate", body)


def evaluate_flow(
    client: JSONFlightClient,
    flow_name: str,
    *,
    limitations: Optional[List[SeriesSelector]] = None,
    block=True,
):
    """Trigger an evaluation of the flow with the given name."""
    flow: Dict = {"flowName": flow_name}
    if limitations is not None:
        flow["limitations"] = [selector.to_data() for selector in limitations]
    response = client.do_action("flows/evaluate", flow)
    if block:
        wait_for_flow_evaluation(client, response, flow_name)


def wait_for_flow_evaluation(
    client: JSONFlightClient, response: Dict, flow_name: Optional[str] = None
):
    """Repeatedly query for the flow evaluation state of the given flow evaluation group."""
    while True:
        state = client.do_action("flows/get_evaluation_state", response)
        if (
            state["completed"] == state["total"]
            and state["blockCompleted"] == state["blockTotal"]
        ):
            if (
                state["failed"] > 0
                or state["blockFailed"] > 0
                or state["currentBlockFailed"] > 0
            ):
                raise FlowEvaluationFailedException(flow_name)
            break
        time.sleep(0.2)
