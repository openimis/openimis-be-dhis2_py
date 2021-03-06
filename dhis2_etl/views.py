from django.shortcuts import render, redirect
from .services.claimServices import *
from .services.insureeServices import *
from .services.locationServices import *
from .services.optionSetServices import *
# import the logging library
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)
# Create your views here.

def startThreadTask(request):
    startDate = request.GET.get('startDate')
    stopDate = request.GET.get('stopDate')
    scope = request.GET.get('scope')
    if scope is None:
        scope = "all"
    if startDate != None and stopDate != None:

        logger.debug("Start SyncDHIS2")
        SyncDHIS2(startDate, stopDate, scope)
        return JsonResponse({'Status':"Done"})
    else:
        return "Please specify startDate and stopDate using yyyy-mm-dd format"

def checkThreadTask(request,id):
    task = ThreadTask.objects.get(pk=id)
    return JsonResponse({'is_done':task.is_done})

def SyncDHIS2(startDate, stopDate, scope):
    logger.debug("Received task")
    responses = []
    ##task = ThreadTask.objects.get(pk=id)
    if scope == "all" or scope == "insuree":
        logger.debug("start Insuree sync")
        insureeResponse = syncInsuree(startDate,stopDate)
    if scope == 'enroll':
        logger.debug("start Insuree enroll")
        insureeResponse = enrollInsuree(startDate,stopDate)
        #responses.insert(insureeResponse)
    if scope == "all" or scope == "policy":
        logger.debug("start Policy sync")
        policyResponse = syncPolicy(startDate,stopDate)


        #responses.insert(policyResponse)
    if scope == "all" or scope == "claim":
        logger.debug("start Claim sync")
        claimResponse = syncClaim(startDate,stopDate)
 

    if  scope == "insureepolicies":
        logger.debug("start Insuree & policy sync")
        insureePolicyResponse = syncInsureePolicy(startDate,stopDate)


    if  scope == "orgunit":
        logger.debug("start orgUnit sync")
        syncRegionResponse = syncRegion(startDate,stopDate)
        syncDistrictResponse = syncDistrict(startDate,stopDate)
        syncWardResponse = syncWard(startDate,stopDate)
        syncVillageResponse = syncVillage(startDate,stopDate)
        syncHospitalResponse = syncHospital(startDate,stopDate)
        syncDispensaryResponse = syncDispensary(startDate,stopDate)
        syncHealthCenterResponse = syncHealthCenter(startDate,stopDate)

    if  scope == "optionset":
        logger.debug("start OptionSets sync")
        syncProductResponse = syncProduct(startDate,stopDate)
        syncGenderResponse = syncGender(startDate,stopDate)
        syncProfessionResponse = syncProfession(startDate,stopDate)
        syncEducationResponse = syncEducation(startDate,stopDate)
        syncGroupTypeResponse = syncGroupType(startDate,stopDate)
        syncDiagnosisResponse = syncDiagnosis(startDate,stopDate)
    logger.debug("Finishing task")

