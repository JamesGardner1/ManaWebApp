from django.test import TestCase
from django.urls import reverse
import views
import game_data_store

# Create your tests here.


class TestHomePageIsEmptyList(TestCase):

    def test_load_home_page(self):
        response = self.client.get(reverse('load_game'))
        self.assertContains(response, 'text_game/home.html')


class TestNextTextSetup(TestCase):
    
    def setup(self):
        pass
    
    def test_next_data_loaded(self):
        views.load_game(request)
        self.assertTrue(data != null)
    
    def tearDown(self):
        pass
    
class TestNextTextSequence(TestCase):
    def setup(self):
        pass

    def test_next_text_sequence(self):
        views.load_game(request)
        next_text = 1
        assert(choices[1].text("GrandMaster?"))

    def tearDown(self):
        pass


    
    
class TestRestartGame(TestCase):
        def setup(self):
        pass

    def test_next_text_sequence(self):
        views.load_game(request)
        next_text = 0
        assert(choices[0].text("Restart Game"))

    def tearDown(self):
        pass

    
    
    
    
    
    
    
class TestStoryBoolean(TestCase):
    
