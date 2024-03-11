import datetime
from typing import get_type_hints
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
    
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        hints = get_type_hints(self)
        # Sonra tarih tipindekileri dönüştürün
        for key, hint_type in hints.items():
            if hint_type == datetime.datetime:
                attr_value = getattr(self, key, None)  # Varsayılan olarak None dön
                if attr_value and isinstance(attr_value, str):  # Değer string ve atanmışsa
                    try:
                        # Tarih formatı kontrolü ve dönüştürme
                        setattr(self, key, datetime.datetime.fromisoformat(attr_value))
                    except ValueError:
                        # Geçersiz tarih formatı, uygun bir hata yönetimi ekleyin
                        pass
