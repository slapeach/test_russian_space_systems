from rest_framework import serializers

from music.models import Album


class AlbumSerializer(serializers.ModelSerializer):
    album = serializers.SerializerMethodField()
    tracks = serializers.SerializerMethodField()
    artist = serializers.CharField(source='artist.name')

    class Meta:
        model = Album
        fields = ['album', 'name', 'artist', 'tracks']
    
    def get_album(self, obj):
        return f"{obj.name}[{obj.year}]"
    
    def get_tracks(self, obj):
        return obj.tracks.values_list('name', flat=True)
