from gt.models import Consoles

def consoles_processor(request):
    consoles = Consoles.objects.all()
    return {'consoles': consoles}
