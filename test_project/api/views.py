from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from music.models import Album
from .serializers import AlbumSerializer


class AlbumView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request, pk=None):
        sorting = self.request.GET.get('sorting')
        if sorting:
            albums = Album.objects.all().order_by(sorting)
        else:
            albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        item = {'data': serializer.data}
        return Response({'item': item})
