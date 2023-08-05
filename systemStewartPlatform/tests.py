#  python manage.py test

# from django.contrib.auth import get_user_model
# from django.test import TestCase
# from django.urls import reverse
#
# from .models import system_stewart_platform
#
#
# class systemTest(TestCase):
#
#     def setUp(self):
#         self.user = get_user_model().objects.create_user(
#             username='testuser',
#             email='test@email.com',
#             password='secret'
#         )
#
#         self.system_stewart_platform = system_stewart_platform.objects.create(
#             title = 'Test System',
#             discription_system ='Test discription system',
#             law_system = 'Test law system',
#             x_max_matrix = 5,
#             y_max_matrix = 4,
#         )
#
#     def test_string_representation(self):
#         system_stewart_platform = system_stewart_platform(title = 'Test System')
#         self.assertEqual(str(system), system.title)
#
#     def test_system_stewart_platform_content(self):
#         self.assertEqual(f'{self.system_stewart_platform.title}', 'A good title')
#         self.assertEqual(f'{self.system_stewart_platform.discription_system}', 'A good discription')
#         self.assertEqual(f'{self.system_stewart_platform.law_system}', 'A good law')
#         self.assertEqual(f'{self.system_stewart_platform.x_max_matrix}', 'A good x max matrix')
#         self.assertEqual(f'{self.system_stewart_platform.y_max_matrix}', 'A good y max matrix')
#
#     def test_post_list_view(self):
#         response = self.client.get(reverse('systemListView'))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'Nice body content')
#         self.assertTemplateUsed(response, 'systemListView.html')
#
#     def test_post_detail_view(self):
#         response = self.client.get('/systemDetailView/1/')
#         no_response = self.client.get('/systemDetailView/100000/')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(no_response.status_code, 404)
#         self.assertContains(response, 'A good title')
#         self.assertTemplateUsed(response, 'systemDetailView.html')
#
#     def test_post_create_view(self):
#         response = self.client.system_stewart_platform(reverse('system_new'), {
#             'title': 'New title',
#             'discription_system' ='Test discription system',
#             'law_system' = 'Test law system',
#             'x_max_matrix' = '5'',
#             'y_max_matrix' = '4',
#         })
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'New title')
#         self.assertContains(response, 'New text')
#
#     def test_post_update_view(self):
#         response = self.client.post(reverse('system_edit', args='1'), {
#             'title': 'New title',
#             'discription_system' ='Test discription system',
#             'law_system' = 'Test law system',
#             'x_max_matrix' = '5'',
#             'y_max_matrix' = '4',
#         })
#         self.assertEqual(response.status_code, 302)
#
#     def test_post_delete_view(self):
#         response = self.client.system_stewart_platform(
#             reverse('system_delete', args='1'))
#         self.assertEqual(response.status_code, 302)

