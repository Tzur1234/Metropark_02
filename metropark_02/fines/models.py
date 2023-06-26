from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator


class IsraeliIDField(models.IntegerField):
    """
    RegexValidator: This validator checks if the input consists of 13 digits using the regular expression ^[0-9]{13}$.

    MinLengthValidator: This validator ensures that the input has a minimum length of 13 digits.

    MaxLengthValidator: This validator ensures that the input has a maximum length of 13 digits.

    unique = True : make the field unique.
    """

    default_validators = [
        RegexValidator(
            regex=r'^[0-9]{13}$',
            message='The Israeli ID number must consist of 13 digits.',
        ),
        MinLengthValidator(13),
        MaxLengthValidator(13),
    ]
    unique = True

STATUS_CHOICES = [
        ('O', 'Open'),
        ('C', 'Close'),
    ]

TYPE_CHOICES = [
        ('1', 'Cash'),
        ('2', 'Credit Card'),
        ('3', 'Check'),
    ]

class Fine(models.Model):
    # israeli_id = IsraeliIDField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    description = models.TextField()
    amount_in_pennies = models.PositiveIntegerField()

class Payment(models.Model):
    fine = models.ForeignKey("Fine", on_delete=models.CASCADE, related_name='fines')
    date_created = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    amount_in_pennies = models.PositiveIntegerField()


