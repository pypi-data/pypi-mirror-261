from typing import List

from idoitapi.Request import Request


class CMDBReports(Request):
    """
    Requests for API namespace 'cmdb.reports'
    """

    def list_reports(self) -> List:
        """
        Lists all reports

        :return: list of reports
        :rtype: list
        :raises: :py:exc:`~idoitapi.APIException.APIException` on error
        """
        return self._api.request(
            'cmdb.reports'
        )

    def read(self, report_id: int) -> List:
        """
        Fetches the result of a report

        :param int report_id: Report identifier
        :return: list
        :rtype: list
        :raises: :py:exc:`~idoitapi.APIException.APIException` on error
        """
        result = self._api.request(
            'cmdb.reports',
            {
                'id': report_id
            }
        )

        if not isinstance(result, list):
            return []

        return result

    def batch_read(self, report_ids: List[int]) -> List[List]:
        """
        Fetches the result of one or more reports

        :param list[int] report_ids: List of report identifiers as integers
        :return: list of lists
        :rtype: list[list]
        """
        requests = []

        for report_id in report_ids:
            requests.append({
                'method': 'cmdb.reports',
                'params': {
                    'id': report_id,
                }
            })

        batch_results = self._api.batch_request(requests)
        results = []

        for result in batch_results:
            if isinstance(result, list):
                results.append(result)
            else:
                results.append([])

        return results
