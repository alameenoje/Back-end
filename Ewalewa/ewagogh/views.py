from django.shortcuts import render
from rest_framework import viewsets
import replicate
from IPython.display import Image

from .serializers import PeepSerializer
from .models import Peeps


def HeroViewSet(request):
    queryset = Peeps.objects.all()
    pic = replicate.run(
  "stability-ai/sdxl:d830ba5dabf8090ec0db6c10fc862c6eb1c929e1a194a5411852d25fd954ac82",
  input={"prompt": request.POST.get('prompt')}
    )
    serializer_class = PeepSerializer
    

# class OrderViewSet(viewsets.ModelViewSet):
#     queryset = Peeps.objects.all(
#     pic = replicate.run(
#   "stability-ai/sdxl:d830ba5dabf8090ec0db6c10fc862c6eb1c929e1a194a5411852d25fd954ac82",
#   input={"prompt": " An oil painting of 'Segun is a young African boy who hails from a traditional background. He has a strong sense of culture and heritage, which is reflected in his appearance and demeanor. His hair is styled in a neat Afro, which is a symbol of his cultural identity and pride. His skin is a deep, rich brown, a testament to his African ancestry.Segun's facial features are striking, with high cheekbones and a sharp jawline that gives him' by Leonardo da Vinci and Frederic Edwin Church"}
# )
#     serializer_class = PeepSerializer

# Create your views here.
