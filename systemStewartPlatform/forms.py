# from .models import system_stewart_platform
# from django.forms import ModelForm, TextInput, Textarea
#
#
# class Create_sytemForm(ModelForm):
#     class Meta:
#         model = system_stewart_platform
#         fields = ["title", "discription_system", 'law_system', 'x_max_matrix', 'y_max_matrix']
#         widgets = {
#             "title": TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Введите название'
#             }),
#             "discription_system": Textarea(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Введите описание системы'
#             }),
#             "law_system": Textarea(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Введите закон системы'
#             }),
#             "x_max_matrix": Textarea(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Укажите размер матрицы по оси х'
#             }),
#             "y_max_matrix": Textarea(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Укажите размер матрицы по оси у'
#             }),
#         }