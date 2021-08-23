from rest_framework import serializers, viewsets

from actives.models import ActiveModel, ActiveGoodsModel

from .goods import GoodsSerializer


class ActiveGoodsSerializer(serializers.HyperlinkedModelSerializer):
    # 一个活动商品对应着一个商品的信息，many=False
    goods = GoodsSerializer(many=False)

    class Meta:
        model = ActiveGoodsModel
        fields = ('goods', 'rate')


class ActiveSerializer(serializers.HyperlinkedModelSerializer):
    # 一个活动对应的多个活动商品，所以many=True
    actives = ActiveGoodsSerializer(many=True)

    class Meta:
        model = ActiveModel
        fields = ('title', 'start_time', 'end_time', 'img1', 'actives')


class ActiveAPIView(viewsets.ModelViewSet):
    queryset = ActiveModel.objects.all()
    serializer_class = ActiveSerializer


class ActiveGoodsAPIView(viewsets.ModelViewSet):
    queryset = ActiveGoodsModel.objects.all()
    serializer_class = ActiveGoodsSerializer
