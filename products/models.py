from django.db import models
import os,random
from medical_store.utils import unique_slug_generator
from  django.db.models.signals import pre_save
from django.urls import reverse
# Create your models here.


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext  = os.path.splitext(base_name)
    return name,ext

def upload_image_path(instance,filename):
    new_filename = random.randint(1,2141512411)
    name,ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)

    return 'products/{new_filename}/{final_filename}'.format(new_filename=new_filename,final_filename=final_filename)

##Product manager

class ProductQuerySet(models.query.QuerySet):
    def featured(self):
        return self.filter(featured=True,active=True)

    def active(self):
        return self.filter(active=True)

    def search(self,query):
        lookups =( Q(title__icontains=query)| Q(description__icontains=query) | Q(tag__title__icontains=query) )
        return self.filter(lookups).distinct()

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self):
        return self.get_queryset().featured()

    def search(self,query):
        
        return self.get_queryset().active().search(query)


class D_category(models.Model):
    title                   = models.CharField(max_length=120,verbose_name='Disease category')
    slug                    = models.SlugField(unique=True,blank=True,null=True,editable=False)
    active                  = models.BooleanField(default=True)
    timestamp               = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.title)



class M_category(models.Model):
    d_title         = models.ForeignKey(D_category,on_delete='DO_NOTHING',null=True,blank=True,verbose_name="Disease category")
    title           = models.CharField(max_length=120,verbose_name='Phase of Disease')
    slug            = models.SlugField(unique=True,blank=True,null=True,editable=False)

    # answer          = models.TextField()
    timestamp       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("medical_product:category", kwargs={"slug": self.slug})
    






class Product(models.Model):
    m_title         = models.ForeignKey(M_category,on_delete='DO_NOTHING',null=True,blank=True,verbose_name="Medicine Category")

    title           = models.CharField(max_length=120)
    description     = models.TextField()
    price           = models.DecimalField(max_digits=20, decimal_places=2, default=00.00)
    image           = models.ImageField(upload_to=upload_image_path,null=True,blank=True)
    featured        = models.BooleanField(default=False)
    active          = models.BooleanField(default=True)
    slug            = models.SlugField(blank=True,unique=True,editable=False)


    objects     = ProductManager()



    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("medical_product:product_detail", kwargs={"slug": self.slug})
    

from django.db import models


class Contact_admin(models.Model):
    # user                    = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete='DO_NOTHING')
    title                   = models.CharField(max_length=120)
    email                   = models.EmailField()
    
    description             = models.TextField()
    # slug                    = models.SlugField(unique=True,blank=True,null=True)
    # active                  = models.BooleanField(default=False)
    
    timestamp               = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.title)



def product_presave_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(product_presave_receiver,sender=Product)
    


def d_category_presave_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(d_category_presave_receiver,sender=D_category)



def m_category_presave_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(m_category_presave_receiver,sender=M_category)