import datetime
from Metrik.models.ORMModel import Model
class Tickets(Model):
    Id: int
    LastUpdateTime: datetime.datetime
    TicketVersion: datetime.datetime
    TicketUid: str
    TicketNumber: str
    Date: datetime.datetime
    LastOrderDate: datetime.datetime
    LastPaymentDate: datetime.datetime
    PreOrder: bool
    IsClosed: bool
    IsLocked: bool
    RemainingAmount: float
    TotalAmount: float
    DepartmentId: int
    TerminalId: int
    TicketTypeId: int
    Note: str
    LastModifiedUserName: str
    TicketTags: str
    TicketStates: str
    TicketLogs: str
    LineSeparators: str
    ExchangeRate: float
    TaxIncluded: bool
    Name: str
    TransactionDocument_Id: int
    IsOpened: bool
    TotalAmountPreTax: float
    
    