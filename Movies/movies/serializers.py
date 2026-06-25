from rest_framework import serializers
from .models import Category, Cast, Movie, Series

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    casts = CastSerializer(many=True)

    
    class Meta:
        model = Movie
        fields = "__all__"
        
    def create(self, validated_data):
        categories_data = validated_data.pop("categories",[])
        casts_data = validated_data.pop("casts",[])

        movie = Movie.objects.create(**validated_data)
        for category_data in categories_data:
            category,created = Category.objects.get_or_create(**category_data)
            movie.categories.add(category)
        for cast_data in casts_data:
            cast,created = Cast.objects.get_or_create(**cast_data)
            movie.casts.add(cast)
        return movie
    
    def update(self, instance, validated_data):

        categories_data = validated_data.pop("categories",None)
        casts_data = validated_data.pop("casts", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        if categories_data is not None:

            categories = []

            for category_data in categories_data:

                category, created = Category.objects.get_or_create(
                    **category_data
                )

                categories.append(category)


            instance.categories.set(categories)



        if casts_data is not None:

            casts = []

            for cast_data in casts_data:

                cast, created = Cast.objects.get_or_create(
                    **cast_data
                )

                casts.append(cast)
            instance.casts.set(casts)

        return instance

class SeriesSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True,read_only=True)
    casts = CastSerializer(many=True,read_only=True )
    
    class Meta:
        model = Series
        fields = '__all__'