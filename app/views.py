from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
def display(request):
              LOT=Topic.objects.all()
              d={'topics':LOT}

              return render(request,'display.html',d)
def web(request):
              WO=Webpage.objects.all()
              WO=Webpage.objects.order_by('name')
              WO=Webpage.objects.order_by('-name')
              WO=Webpage.objects.filter(name__startswith='X')
              WO=Webpage.objects.filter(Q(topic_name='cricket') & Q(name='dhoni'))
           
              d={'webpage':WO}
              return render(request,'web.html',d)
def access(request):
              AO=AccessRecord.objects.all()
              AO=AccessRecord.objects.filter(date__year='2023')
              AO=AccessRecord.objects.filter(date__month='02')
              AO=AccessRecord.objects.filter(date__day='02')
              AO=AccessRecord.objects.all() 
              AO=AccessRecord.objects.filter(date__gt='2022-10-10')
              
              d={'access':AO}
              return render(request,'access.html',d)
