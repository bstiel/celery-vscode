import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response


logger = logging.getLogger(__name__)


from .worker import app


@api_view(["GET"])
def stats():
    inspector = app.control.inspect()
    stats = inspector.stats()
    return Response(stats)
