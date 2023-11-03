from rest_framework import serializers

from api_multimedia.models import Track, Album


class MultimediaSerializer(serializers.Serializer):

    alb = serializers.CharField()
    name = serializers.CharField()
    artist_name = serializers.CharField()
    track_list = serializers.SerializerMethodField()

    def get_track_list(self, instance):
        tr = Track.objects.filter(album=instance)
        return [t.track for t in tr]
