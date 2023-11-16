from app.papers.contract.service.abstract import ContractService
from app.utils.dev.response import success_message


class PapersContractDoAdd(ContractService):
    def handle(self, **kwargs):
        json = dict(
            pdfUrl="",
        )
        return success_message(json=json)
