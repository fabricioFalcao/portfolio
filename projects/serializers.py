from rest_framework import serializers
from projects.models import Profile, Project, CertifyingInstitution, Certificate

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = "__all__"


class NestedCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['name', 'timestamp']


class CertifyingInstitutionSerializer(serializers.ModelSerializer):
    certificates = NestedCertificateSerializer(many=True)

    class Meta:
        model = CertifyingInstitution
        fields = ["id", "name", "url", "certificates"]

    def create(self, validated_data):
        certificates_data = validated_data.pop('certificates')
        certifying_institution = CertifyingInstitution.objects.create(**validated_data)
        
        for certificate_data in certificates_data:
            certificate_data['certifying_institution'] = certifying_institution
            CertificateSerializer().create(validated_data=certificate_data)
        
        return certifying_institution