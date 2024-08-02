from django.urls import reverse
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile
from io import BytesIO
from PIL import Image
from rest_framework.test import APITestCase
from .models import Meme
import os


class MemeTests(APITestCase):

    def setUp(self):
        def image_create():
            image = BytesIO()
            Image.new('RGB', (100, 100)).save(image, 'PNG')
            image.seek(0)
            return image

        self.uploaded_image = SimpleUploadedFile(
            name='test_image.png',
            content=image_create().read(),
            content_type='image/png'
        )

        self.updated_image = SimpleUploadedFile(
            name='test_image_update.png',
            content=image_create().read(),
            content_type='image/png'
        )

    def test_create_meme(self):
        url = reverse('memes:memes-list')
        data = {'title': 'Test Meme', 'image': self.uploaded_image, 'text': 'Test Meme'}
        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Meme.objects.get().title, 'Test Meme')

    def test_get_meme(self):
        meme = Meme.objects.create(title='Test Meme', image=self.uploaded_image, text='Test Meme')
        url = reverse('memes:memes-detail', args=[meme.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Meme')

    def test_update_meme(self):
        meme = Meme.objects.create(title='Test Meme', image=self.uploaded_image, text='Test Meme')
        url = reverse('memes:memes-detail', args=[meme.id])

        data = {
            'title': 'Updated Meme',
            'image': self.updated_image,
            'text': 'Test Meme'
        }
        response = self.client.put(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Meme.objects.get(id=meme.id).title, 'Updated Meme')

    def test_delete_meme(self):
        meme = Meme.objects.create(title='Test Meme', image=self.uploaded_image, text='Test Meme')
        url = reverse('memes:memes-detail', args=[meme.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Meme.objects.count(), 0)
