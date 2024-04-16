import pymysql
import threading

from django.core.files.storage import default_storage
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly

from algorithms.models import Task
from web_scoring import settings
from .serializers import TaskSerializer

from .task import create_process_task


class TaskViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Task.objects.all().order_by('-id')
    serializer_class = TaskSerializer


class ProcessFilesAPIView(APIView):
    authentication_classes = []
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request):
        file_list = []
        file_path_list = []
        for key in request.FILES.keys():
            files = request.FILES.getlist(key)
            for file in files:
                file_name = default_storage.save(file.name, file)
                file_path = default_storage.path(file_name)
                file_list.append(file_path)
                file_path_list.append(settings.MEDIA_URL + file_name)
        task_instance = Task.objects.create(status=False)
        task_instance.file_path = str(file_path_list)
        task_instance.save()
        task_thread = threading.Thread(target=create_process_task,
                                       args=(task_instance.id, file_list))
        task_thread.start()

        return Response({'message': 'Process tasks have been pushed successfully'}, status=status.HTTP_200_OK)


class GetProcessedDataAPIView(APIView):
    authentication_classes = []
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        # Connect to the MySQL database
        conn = pymysql.connect(host='CHANGE_ME_HERE', port=1181, user='CHANGE_ME_HERE', password='CHANGE_ME_HERE', database='comp_test')
        cursor = conn.cursor()

        # Fetch the required columns from the web_data table
        query = (
            "SELECT user_experience_score, bounce_rate_score, loading_speed_score, network_feedback_score, first_input_delay_score, click_error_score, page_load_error_score, blank_page_score, total_score, average_score,eventName FROM web_data")
        cursor.execute(query)
        rows = cursor.fetchall()

        # Convert the fetched data to a list of dictionaries
        data = []
        for row in rows:
            data.append({
                'user_experience_score': row[0],
                'bounce_rate_score': row[1],
                'loading_speed_score': row[2],
                'network_feedback_score': row[3],
                'first_input_delay_score': row[4],
                'click_error_score': row[5],
                'page_load_error_score': row[6],
                'blank_page_score': row[7],
                'total_score': row[8],
                'average_score': row[9],
                'eventName': row[10]
            })
        # Close the cursor and connection
        cursor.close()
        conn.close()
        return Response(data, status=status.HTTP_200_OK)
