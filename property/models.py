from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'types'

class Property(models.Model):
    type            = models.ForeignKey('Type', on_delete=models.CASCADE, null=True)
    property_image  = models.ForeignKey('PropertyImage', on_delete=models.CASCADE)
    title           = models.CharField(max_length=100)
    host            = models.ForeignKey('Host', on_delete=models.CASCADE)
    price           = models.DecimalField(max_digits=11, decimal_places=3)
    attribute       = models.ManyToManyField('Attribute', through='PropertyAttribute')
    capacity        = models.IntegerField()
    refund          = models.ForeignKey('Refund', on_delete=models.CASCADE)
    price_per_guest = models.DecimalField(max_digits=11, decimal_places=3)
    latitude        = models.DecimalField(max_digits=11, decimal_places=3)
    longitude       = models.DecimalField(max_digits=11, decimal_places=3)
    country         = models.ForeignKey('.Country', on_delete=models.CASCADE)
    province        = models.ForeignKey('.Province', on_delete=models.CASCADE)
    city            = models.ForeignKey('.City', on_delete=models.CASCADE)
    district        = models.ForeignKey('.District', on_delete=models.CASCADE)
    street          = models.ForeignKey('.Street', on_delete=models.CASCADE)
    content         = models.TextField()
    size            = models.ManyToManyField('Size', through='PropertySize')
    facility        = models.ManyToManyField('Facility', through='PropertyFacility')

    class Meta:
        db_table = 'properties'

class PropertyImage(models.Model):
    url = models.CharField(max_length=1000)

    class Meta:
        db_table = 'property_images'

class Host(models.Model):
    name = models.CharField(max_length=100)
    is_super = models.BooleanField(null=True)

    class Meta:
        db_table = 'hosts'

class Attribute(models.Model):
    title   = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        db_table = 'attributes'

class PropertyAttribute(models.Model):
    property  = models.ForeignKey('Property', on_delete=models.CASCADE)
    attribute = models.ForeignKey('Attribute', on_delete=models.CASCADE)

class Refund(models.Model):
    title   = models.CharField(max_length=100)
    content = models.TextField()

class Size(models.Model):
    name    = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        db_table = 'sizes'

class PropertySize(models.Model):
    property = models.ForeignKey('Property', on_delete=models.CASCADE)
    size     = models.ForeignKey('Size', on_delete=models.CASCADE)

class Facility(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'facilities'

class PropertyFacility(models.Model):
    property = models.ForeignKey('Property', on_delete=models.CASCADE)
    facility = models.ForeignKey('Facility', on_delete=models.CASCADE)

class Review(models.Model):
    user          = models.ForeignKey('user.User', on_delete=models.CASCADE)
    property      = models.ForeignKey('Property', on_delete=models.CASCADE)
    content       = models.TextField()
    cleanliness   = models.DecimalField(max_digits=11, decimal_places=3)
    communication = models.DecimalField(max_digits=11, decimal_places=3)
    check_in      = models.DecimalField(max_digits=11, decimal_places=3)
    accuracy      = models.DecimalField(max_digits=11, decimal_places=3)
    location      = models.DecimalField(max_digits=11, decimal_places=3)
    affordability = models.DecimalField(max_digits=11, decimal_places=3)

    class Meta:
        db_table = 'reviews'

class Safety(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'safeties'

class PropertySafety(models.Model):
    property = models.ForeignKey('Property', on_delete=models.CASCADE)
    safety   = models.ForeignKey('Safety', on_delete=models.CASCADE)

class Rule(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'rules'

class PropertyRule(models.Model):
    property = models.ForeignKey('Property', on_delete=models.CASCADE)
    rule = models.ForeignKey('Rule', on_delete=models.CASCADE)

class Comment(models.Model):
    review = models.ForeignKey('Review', on_delete=models.CASCADE)
    host = models.ForeignKey('Host', on_delete=models.CASCADE)

    class Meta:
        db_table = 'comments'
