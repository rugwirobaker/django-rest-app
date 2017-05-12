from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetSerializer(serializers.Serializer):

    #The first part of the serializer class defines 
    # the fields that get serialized/deserialized. 
    # The create() and update() methods 
    # define how fully fledged instances are created or modified 
    # when calling serializer.save()
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)

    #The field flags can also control how the serializer should be displayed 
    # in certain circumstances, such as when rendering to HTML. 
    # The {'base_template': 'textarea.html'} flag above is equivalent 
    # to using widget=widgets.Textarea on a Django Form class. 
    # This is particularly useful for controlling how the browsable API should be displayed, 
    # as we'll see later in the tutorial.
    code =  serializers.CharField(style={'base_template': 'text_area.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """

        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance