from core.model_factories import ProfileFactory
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.reverse import reverse
from core.util.utils import to_dict
import json


# Create your tests here.
class CreateProfileTest(APITestCase):


    def setUp(self) -> None:

        return super().setUp()

    def test_can_create_profile(self):
        #profile = ProfileFactory()  
        #profile_dic = to_dict(profile)
        #print(profile_dic)
        #serialized = json.dumps(profile_dic)
        #self.data = serialized 
        #print(self.data)
        value = '{"first_name": "Jo\u00e3o Miguel", "last_name": "Mendes", "age": 0, "sex": "F"}',
        response = self.client.post(reverse('profile_list'), data=value)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
