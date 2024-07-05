
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from .models import Patient
from rest_framework.parsers import JSONParser


from .serializers import PatientSerializer

class PatientView(APIView):

# list view
    def get(self, reqeust):
        list = Patient.objects.all()
        serializer = PatientSerializer(list, many=True)
        # print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def post(self, request):
        new_patient = request.data
        print(new_patient)
        serializer = PatientSerializer(data=new_patient)
        if serializer.is_valid():
            serializer.save()
            return Response('Patient added successfully', 
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, 
                            status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request):
        patient_id = request.data.get('id')
        try: 
            patient = Patient.objects.get(id=patient_id)
        except Exception as e:
            print(e)
            return Response({'message':'unable to find the patient'}, 
                            status=status.HTTP_400_BAD_REQUEST)

        patient.delete()
        return Response({'message':'patient details deleted'}, 
                        status=status.HTTP_200_OK) 

# updating 
    def put(self, request):
        try: 
            patient_id = request.get('id')
            patient = Patient.object.get(id = patient_id)
            new_patient = request.get('patient')
            patient_serializer = PatientSerializer(patient, data=new_patient)
            if patient_serializer.is_vaid():
                patient_serializer.save()
                return Response({'message':'updated successfully'}, 
                                status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
        
