from core import BaseModel


class Payment(BaseModel):
    pass

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
        db_table = 'payments'
