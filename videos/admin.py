from django.contrib import admin
from .models import VideoAllProxy, VideoPublishedProxy


class VideoAllAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'video_id', 'active', 'state', 'is_published']
    search_fields = ['title']
    list_filter = ['active', 'state']
    readonly_fields = ['id', 'publish_timestamp']
    class Meta:
        model = VideoAllProxy

    # def published(self, obj, *args, **kwargs):
    #     return obj.active

admin.site.register(VideoAllProxy, VideoAllAdmin)


class VideoPublishedProxyAdmin(admin.ModelAdmin):
    list_display = ['title', 'video_id']
    search_fields = ['title']
    # list_filter = ['video_id']
    class Meta:
        model = VideoPublishedProxy

    def get_queryset(self, request):
        return VideoPublishedProxy.objects.filter(active=True)

admin.site.register(VideoPublishedProxy, VideoPublishedProxyAdmin)