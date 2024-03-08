from zeep import Client
from zeep.helpers import serialize_object

from .service import Service
from ..data_classes.employee.employee import Employee
from ..utils.nmbrs_exception_handler import nmbrs_exception_handler
from ..utils.return_list import return_list


class EmployeeService(Service):
    """
    A class representing Employee Service for interacting with Nmbrs employee-related functionalities.
    """

    def __init__(self, auth_header: dict, sandbox: bool) -> None:
        """
        Constructor method for EmployeeService class.

        Initializes EmployeeService instance with authentication and sandbox settings.

        Args:
            auth_header (dict): A dictionary containing authentication details.
            sandbox (bool): A boolean indicating whether to use the sandbox environment.
        """
        super().__init__()
        self.auth_header = auth_header
        self.sandbox = sandbox

        # Initialize nmbrs services
        base_uri = self.nmbrs_base_uri
        if sandbox:
            base_uri = self.nmbrs_sandbox_base_uri
        self.employee_service = Client(f"{base_uri}{self.employee_uri}")

    def set_auth_header(self, auth_header: dict) -> None:
        """
        Method to set the authentication.

        Args:
            auth_header (dict): A dictionary containing authentication details.
        """
        self.auth_header = auth_header

    @return_list
    @nmbrs_exception_handler(resources=["EmployeeService:List_GetByCompany"])
    def get_all_by_company(self, company_id: int, employee_type: int) -> list[Employee]:
        """
        Retrieve all employees in a company, based on the given employment types.

        For more information, refer to the official documentation:
            [Soap call List_GetByCompany](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=List_GetByCompany)

        Args:
            company_id (int): The ID of the company.
            employee_type (int): The ID of the [employee type](https://support.nmbrs.com/hc/en-us/articles/360015523160-Nmbrs-API-enumerations#h_01EEWM3YE1CM82J337Q02C18AT).

        Returns:
            list[Employee]: A list of Employee objects representing all employees.
        """
        data = {"CompanyId": company_id, "EmployeeType": employee_type}
        employees = self.employee_service.service.List_GetByCompany(**data, _soapheaders=self.auth_header)
        employees = [Employee(employee) for employee in serialize_object(employees)]
        return employees
