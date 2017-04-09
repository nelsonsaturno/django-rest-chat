from channels_api.bindings import ResourceBinding

from .models import Question
from .serializers import QuestionSerializer


class QuestionBinding(ResourceBinding):

    model = Question
    stream = "questions"
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
