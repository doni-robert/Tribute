from django.db import models
from django.core.validators import RegexValidator

class County(models.Model):
    """Model representing a county."""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Constituency(models.Model):
    """Model representing a constituency within a county."""
    name = models.CharField(max_length=100)
    county = models.ForeignKey(County, related_name='constituencies', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.county.name})"

class Ward(models.Model):
    """Model representing a ward within a constituency."""
    name = models.CharField(max_length=100)
    constituency = models.ForeignKey(Constituency, related_name='wards', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.constituency.name})"

class PollingStation(models.Model):
    """Model representing a polling station within a ward."""
    name = models.CharField(max_length=100)
    ward = models.ForeignKey(Ward, related_name='polling_stations', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.ward.name})"
    
class Entry(models.Model):
    """Model representing an entry with user details for PDF generation.

    Attributes:
        first_name: A CharField storing the first name of the person.
        second_name: A CharField storing the second name of the person
        third_name: A CharField storing the third name of the person
        fourth_name: A CharField storing the fourth name of the person
        id_or_passport_number: A CharField storing the ID or Passport number.
        county: A ForeignKey to the County model.
        constituency: A ForeignKey to the Constituency model.
        ward: A ForeignKey to the Ward model.
        polling_station: A ForeignKey to the PollingStation model.
        mobile_number: An IntegerField storing the mobile number.
        signature: An ImageField storing the signature image.
        created_at: A DateTimeField storing the timestamp when the entry was created.
    """
    NAME_MAX_LENGTH = 25
    ID_MAX_LENGTH = 10

    name = models.CharField(max_length=NAME_MAX_LENGTH, default="No Name")
    id_or_passport_number = models.CharField(max_length=ID_MAX_LENGTH)
    county = models.ForeignKey(County, on_delete=models.PROTECT)
    constituency = models.ForeignKey(Constituency, on_delete=models.PROTECT)
    ward = models.ForeignKey(Ward, on_delete=models.PROTECT)
    polling_station = models.ForeignKey(PollingStation, on_delete=models.PROTECT)
    mobile_number = models.IntegerField(
        validators=[
            RegexValidator(r'^[0-9]{7,15}$', message='Phone number must be between 7 and 15 digits.')
        ]
    )
    signature = models.ImageField(upload_to='signatures/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns a string representation of the Entry."""
        return f"{self.name} - {self.id_or_passport_number}"