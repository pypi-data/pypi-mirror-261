from zeep import Client
from zeep.helpers import serialize_object

from .service import Service
from ..utils.nmbrs_exception_handler import nmbrs_exception_handler
from ..utils.return_list import return_list
from ..data_classes.company.company import Company
from ..data_classes.company.wage_tax import WageTax
from ..data_classes.company.wage_tax_xml import WageTaxXML


class CompanyService(Service):
    """
    A class representing Company Service for interacting with Nmbrs company-related functionalities.
    """

    def __init__(self, sandbox: bool = True) -> None:
        """
        Constructor method for CompanyService class.

        Args:
            sandbox (bool (optional)): A boolean indicating whether to use the sandbox environment (default: True).
        """
        super().__init__(sandbox)
        self.auth_header: dict | None = None

        # Initialize nmbrs services
        self.company_service = Client(f"{self.base_uri}{self.company_uri}")

    def set_auth_header(self, auth_header: dict) -> None:
        """
        Method to set the authentication.

        Args:
             auth_header (dict): A dictionary containing authentication details.
        """
        self.auth_header = auth_header

    @nmbrs_exception_handler(resources=["CompanyService:List_GetAll"])
    def get_all(self) -> list[Company]:
        """
        Retrieve all companies.

        For more information, refer to the official documentation:
            [Soap call List_GetAll](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=List_GetAll)

        Returns:
            list[Company]: A list of Company objects representing all companies.
        """
        companies = self.company_service.service.List_GetAll(
            _soapheaders=self.auth_header
        )
        companies = [Company(company) for company in serialize_object(companies)]
        return companies

    @return_list
    @nmbrs_exception_handler(resources=["CompanyService:WageTax_GetList"])
    def get_all_wagetax(self, company_id: int, year: int) -> list[WageTax]:
        """
        Retrieve all wage taxes for a specific company and year.

        For more information, refer to the official documentation:
            [Soap call WageTax_GetList](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageTax_GetList)

        Args:
            company_id (int): The ID of the company.
            year (int): The year for which wage taxes are retrieved.

        Returns:
            list[WageTax]: A list of WageTax objects representing all wage taxes for the specified company and year.
        """
        data = {"CompanyId": company_id, "intYear": year}
        wage_taxes = self.company_service.service.WageTax_GetList(
            **data, _soapheaders=self.auth_header
        )
        wage_taxes = [WageTax(wage_tax) for wage_tax in serialize_object(wage_taxes)]
        return wage_taxes

    @nmbrs_exception_handler(resources=["CompanyService:WageTax_GetXML"])
    def get_wagetax_details(self, company_id: int, loonaangifte_id) -> WageTaxXML:
        """
        Retrieve wage tax details for a specific company and loonaangifte ID.

        For more information, refer to the official documentation:
            [Soap call WageTax_GetXML](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageTax_GetXML)

        Args:
            company_id (int): The ID of the company.
            loonaangifte_id: The loonaangifte ID.

        Returns:
            WageTaxXML: An object representing the wage tax details for the specified company and loonaangifte ID.
        """
        data = {"CompanyId": company_id, "LoonaangifteID": loonaangifte_id}
        wage_tax_details = self.company_service.service.WageTax_GetXML(
            **data, _soapheaders=self.auth_header
        )
        wage_tax_details = WageTaxXML(wage_tax_details)
        return wage_tax_details
