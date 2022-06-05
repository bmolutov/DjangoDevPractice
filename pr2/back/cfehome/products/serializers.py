from rest_framework import serializers 
from rest_framework.reverse import reverse

from .models import Product 
from .validators import validate_title


class ProductSerializer(serializers.ModelSerializer):

    # my_discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)
    email = serializers.EmailField(write_only=True)
    title = serializers.CharField(validators=[validate_title])
    class Meta:
        model = Product
        fields = [
                'url',
                'email',
                'pk',
                'title',
                'content',
                'price',
                'sale_price',
                # 'my_discount',
                ]

        # def validated_data(self, value):
        #     qs = Product.objects.filter(title__exact=value)
        #     if qs.exists():
        #         raise serializers.ValidationError(f"{value} is already a product name")
        #     return value
    
    def create(self, validated_data):
        # return Product.objects.create(**validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        email = validated_data.pop('email')
        return super().update(instance, validated_data)

    def get_url(self, obj):
        # return f"/api/products/{obj.pk}/"
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-detail", kwargs={"pk": obj.pk}, request=request)

    # def get_my_discount(self, obj):
    #     if not hasattr(obj, 'id'):
    #         return None
    #     if not isinstance(obj, Product):
    #         return None
    #     return obj.get_my_discount()

