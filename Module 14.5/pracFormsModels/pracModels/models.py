from django.db import models

# Create your models here.
class MyModel(models.Model):
    title = models.CharField(max_length = 200)
    auto_field = models.AutoField(primary_key=True)
    #big_auto_field = models.BigAutoField(primary_key=True)
    big_int_field = models.BigIntegerField()
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    char_field = models.CharField(max_length=255)
    # comma_separated_field = models.CharField(
    #     validators=[comma_separated_validator],
    #     max_length=255,
    # )
    date_field = models.DateField()
    datetime_field = models.DateTimeField()
    decimal_field = models.DecimalField(max_digits=10, decimal_places=2)
    email_field = models.EmailField()
    #file_field = models.FileField()  # Represents a file upload
    float_field = models.FloatField() # Store floating point values
    #file_path_field = models.FilePathField(path='/path/to/files/')  #Represents a file path on the file system.
    duration_field = models.DurationField() #used to store a duration of time
    image_field = models.ImageField(upload_to='images/') #Similar toFileField, but optimized for image uploads 
    generic_ip_address_field = models.GenericIPAddressField()  # Stores the IP address, either IPv4 or IPv6
    integer_field = models.IntegerField() # Stores the integer values
    json_field = models.JSONField() # Stores the JSON values
    #null_boolean_field = models.NullBooleanField() # Stores a boolean value, can be NULL
    positive_integer_field = models.PositiveIntegerField() # Stores a positive integer value
    positive_small_integer_field = models.PositiveSmallIntegerField() # Stores a positive small integer value
    positive_big_integer_field = models.PositiveBigIntegerField() # Stores a positive big integer value
    slug_field = models.SlugField() # A field type used to store a short label or identifier suitable for use in URLs.
    small_integer_field = models.SmallIntegerField() # Stores the small integer values
    text_field = models.TextField() # Stores a large amount of text without a specific length restriction
    time_field = models.TimeField() # Stores the time value
    #timezone_field = models.DateTimeField(tzinfo=None) # Stores a datetime value with timezone information
    url_field = models.URLField() # store and validate URLs (Uniform Resource Locators) as strings.
    uuid_field = models.UUIDField() # Stores a 128-bit unique identifier as a string.

    def __str__(self):
        return self.title