from rest_framework_simplejwt.serializers import TokenObtainPairSerializer,TokenObtainSerializer




class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
 def validate(self, attrs):
        # # The default result (access/refresh tokens)
        """ Outra forma de fazer o mesmo retorno:
        data = super().validate(attrs)
        # Add custom data from your user model here
        user = self.user
        data['user_id'] = user.id
        data['user_username'] = user.username
        # Add more custom data fields as needed
        """
        
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        # Custom data you want to include
        data.update({'id': self.user.id})
        data.update({'fullname': self.user.first_name + ' '+self.user.last_name})
        # and everything else you want to send in the response
        return data